# Search the TSX web site to get a list of all listed companies
import os
import sys
import getopt
import datetime
# from numpy.lib.function_base import append
import pandas as pd
import sqlalchemy
import logging

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

import pandas_datareader.data as web

from dotenv import load_dotenv
from sqlalchemy import engine
load_dotenv()

class TSX_Browser():
    def __init__(self, chrome_driver_path=None):
        self.url_ticker= "https://www.tsx.com/listings/listing-with-us/listed-company-directory"       
        self.__OPTIONS = webdriver.ChromeOptions()
        self.__OPTIONS.add_experimental_option('excludeSwitches', ['enable-logging'])
        if chrome_driver_path is None:
            self.__CHROME_DRIVER_LOCATION = "C:\Program Files (x86)\chromedriver.exe"
        else:
            self.__CHROME_DRIVER_LOCATION = chrome_driver_path
        
        self.driver = None
        #self.driver = webdriver.Chrome(executable_path=self.__CHROME_DRIVER_LOCATION,options=self.__OPTIONS)
        self.seconds_to_wait = 10

    def close(self):
        try:
            self.driver.quit()
        except Exception as e:
            logging.critical(f"Unable to quit() Chrome Driver, Error: {e}")

    def set_exchange(self, exchange) -> bool:
        # Make sure we have a driver available
        if self.driver is None:
            try:
                self.driver = webdriver.Chrome(executable_path=self.__CHROME_DRIVER_LOCATION,options=self.__OPTIONS)
            except Exception as e:
                logging.critical(f"Unable to create Chrome Browser Driver, Error: {e}")
                raise
                return False

        self.driver.get(self.url_ticker)
        self.driver.minimize_window()
        tsx_css_selectors = {"tsx":".tsx.on", "tsxv":".tsxv.on"}
        if exchange.lower() in tsx_css_selectors.keys():
            tsx_flag = tsx_css_selectors.get(exchange)
        else:
            # Use tsx by default if bad exchange passed
            tsx_flag = tsx_css_selectors.get('tsx')
        
        # Check if TSX Browser is already on desired exchange page        
        try:
            WebDriverWait(self.driver, self.seconds_to_wait).until( EC.visibility_of_element_located((By.CSS_SELECTOR, tsx_flag)))
            return True
        except:
            # Switch Exchange using TSX Browser button
            switch_btn_xpath = '//*[@id="exchange-toggle"]'
            switch_btn = self.driver.find_element_by_xpath(switch_btn_xpath)
            switch_btn.click()
            # Make sure the switch worked correctly or fail
            try:
                WebDriverWait(self.driver, self.seconds_to_wait).until( EC.visibility_of_element_located((By.CSS_SELECTOR, tsx_flag)))
                return True
            except Exception as e:
                logging.critical(f"Unable to switch TSX Echange page, Error: {e}")
                raise
                return False

class TSX_Company_Info():
    def __init__(self, name, ticker, exchange='tsx'):
        self.name       = name.upper().strip()
        self.ticker     = ticker.upper().strip()
        self.exchange   = exchange
        self.url        = f"https://money.tmx.com/en/quote/{self.ticker}"
        self.yahoo      = self.create_yahoo_ticker(self.ticker, self.exchange)

    @property
    def dict(self) -> dict:
        data ={}
        data["ticker"]   = self.ticker
        data["name"]     = self.name
        data["exchange"] = self.exchange
        data["url"]      = self.url
        data["yahoo"]    = self.yahoo
        return data

    def create_yahoo_ticker(self, ticker, exchange):
        yahoo_ticker = ticker.replace('.','-')
        # TODO: fix the doube "-" not found on yahoo exchange
        yahoo_extension = "TO" if exchange == "tsx" else "V"
        yahoo_ticker = f"{yahoo_ticker}.{yahoo_extension}"
        return yahoo_ticker

class TSX():
    def __init__(self):
        self.chrome_browser = None

    def dispose(self):
        if self.chrome_browser is not None:
            self.chrome_browser.close()

    # Return a DataFrame with a list of TSX Company Info
    def extract_tickers_for_str(self, search_str, exchange="tsx", progress=False) -> pd.DataFrame:
        companies = []
        if self.chrome_browser is None:
            try:
                chrome_browser = TSX_Browser()
                self.chrome_browser = chrome_browser
            except Exception as e:
                logging.critical(f"Unable to create Chrome Browser, Error: {e}")
                return None
        
        # Make sur the TSX Page is on the desired stock exchange
        try:
            self.chrome_browser.set_exchange(exchange)
        except Exception as e:
            logging.critical(f"Unable to set TSX Exchange Page, Error: {e}")
            return None
        if progress:
            print(f"\n\n Extracting data for : {search_str}")       
        # Send letter into the search box of the page
        search_box_xpath = '//*[@id="query"]'
        search_box = self.chrome_browser.driver.find_element_by_xpath(search_box_xpath)
        search_box.send_keys(search_str)
        # Click the search button to send search request
        search_btn_xpath = '//*[@id="btn-search-listed-company-directory"]'
        search_btn = self.chrome_browser.driver.find_element_by_xpath(search_btn_xpath)
        search_btn.click()

        try:
            # By.ID, By.xpath, BY.cssSelector
            result_data_xpath = '//*[@id="tresults"]/tbody'
            WebDriverWait(self.chrome_browser.driver, 10).until( EC.visibility_of_element_located((By.XPATH, result_data_xpath)))
            datagrid = self.chrome_browser.driver.find_element_by_xpath(result_data_xpath)
            #progress_msg(f"Received response for letter {search_str} ")
        except TimeoutException:
            return None

        data = datagrid.find_elements_by_tag_name("tr")
        # progress_msg(f"Extracting table data for letter {search_str} ")

        companies = []
        for row in data:
            cells = row.find_elements_by_tag_name("td")
            # Skip the line with no ticker symbol
            if (cells[1].text != ""):
                ticker = cells[1].text
                name = cells[0].text
                company = TSX_Company_Info(name, ticker, exchange=exchange)
                companies.append(company.dict)
                if progress: 
                    print(f"-- Extracted : {exchange}, {ticker.ljust(10)}, {name.strip()} ")
        
        df_companies = pd.DataFrame(companies)
        df_companies.set_index('ticker')
        return df_companies

    def save_tickers_in_DB(self, DB, df_tickers, overwrite=False) -> bool:
        try:
            engine = sqlalchemy.create_engine(f"sqlite:///{DB}")
        except Exception as e:
            logging.critical(f"Unable to create DB Engine, Error: {e}")
            return False

        save_type = "append" if not overwrite else "replace"
        try:
            df_tickers.to_sql('tsx_symbols', engine, if_exists=save_type)
            saved = True
        except Exception as e:
            logging.critical(f"Unable to save DataFrame using .to_sql(), Error: {e}")
            saved = False
            # Raise an error
        finally:
            engine.dispose()
        
        return saved

    def update_all_tickers(self, DB, progess=False):
        alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0-9']
        overwrite = True
        # Extract data from TSX
        for letter in alphabet:
            df_tickers = self.extract_tickers_for_str(letter,exchange='tsx', progress=progess)
            self.save_tickers_in_DB(DB, df_tickers, overwrite=overwrite)
            overwrite = False
        # Extract data from TSX Venture
        for letter in alphabet:
            df_tickers = self.extract_tickers_for_str(letter,exchange='tsxv', progress=progess)
            self.save_tickers_in_DB(DB, df_tickers, overwrite=overwrite)

        self.cleanup_DB(DB)

    def cleanup_DB(self, DB):
        db_to_clean = DB
        db_cleaned  = DB.replace('.','_clean.')
        engine1 = sqlalchemy.create_engine(f"sqlite:///{db_to_clean}")
        engine2 = sqlalchemy.create_engine(f"sqlite:///{db_cleaned}")
        data1 = pd.read_sql_table("tsx_symbols", engine1)
        data2 = data1.drop_duplicates('ticker')
        data2.to_sql('tsx_symbols',engine2, if_exists='replace')

    def get_yahoo_tickers_for(self, DB, starts_with):
        # tickers = ["AW-UN.TO", "QUS.TO", "ARD.V"]
        try:
            engine = sqlalchemy.create_engine(f"sqlite:///{DB}")
            df_tickers = pd.read_sql(f"SELECT yahoo FROM tsx_symbols WHERE yahoo LIKE '{starts_with}%'", engine)
            tickers = df_tickers['yahoo'].tolist()
        except Exception as e:
            logging.critical(f"Unable to get list of tickers ({DB}, {starts_with}), Error: {e}")
            tickers = None
        return tickers

    def get_company_info_for(self, DB, starts_with):
        # tickers = ["AW-UN.TO", "QUS.TO", "ARD.V"]
        try:
            engine = sqlalchemy.create_engine(f"sqlite:///{DB}")
            df_companies = pd.read_sql(f"SELECT * FROM tsx_symbols WHERE name LIKE '{starts_with}%'", engine)
            df_companies = df_companies.drop(['url', 'index'], axis=1)
            df_companies.reset_index(drop=True)
            companies = df_companies.to_dict('records')
        except Exception as e:
            logging.critical(f"Unable to get list of tickers ({DB}, {starts_with}), Error: {e}")
            tickers = None
        return companies

    def get_prices_from_yahoo(self, stocks_list, start, end):
        data = web.DataReader(stocks_list,'yahoo', start, end)
        # convert data to simpler format for storing
        results = []
        for ticker in stocks_list:
            df_ticker = pd.DataFrame({'Open'  :data[('Open',ticker)],
                                      'Close' :data[('Close',ticker)],
                                      'High'  :data[('High',ticker)],
                                      'Low'   :data[('Low',ticker)],
                                      'Volume':data[('Volume',ticker)]
            })
            results.append({"symbol":ticker, "prices": df_ticker})
        
        return results

    def save_prices_to_DB(self, DB, prices):
        # Prices is a list of as obtained from "get_prices_from_yahoo"
        for company in prices:
            ticker = company.get('symbol')
            data   = company.get('prices')
            try:
                engine = sqlalchemy.create_engine(f"sqlite:///{DB}")
                data.to_sql(ticker, engine, if_exists='append')
                engine.dispose()
            except Exception as e:
                logging.critical(f"Unable to save DataFrame using .to_sql(), Error: {e}")
                return False

        return True
            




# if __name__ == '__main__':
#     logging.basicConfig(
#         level=logging.CRITICAL,
#         format="{asctime} {levelname:<8} {message}",
#         style='{'
#     )
#     # Open a tsx object
#     t = TSX()
#     if t is None:
#         sys.exit()
    
#     # Remove comment to update TSX Tickers Table
#     # t.update_all_tickers('TSX_Stocks_v2.sqlite', progess=True)
    
#     test_db = "TSX_Stocks_v3.sqlite"

#     # alph = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0-9']
#     # tick_num = []
#     # for letter in alph:
#     #     stocks = t.get_yahoo_tickers_for('TSX_Stocks_v2_clean.sqlite', letter)
#     #     tick_num.append({"letter":letter, "count":len(stocks)})
#     # print(tick_num)

#     alph = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
#     for letter in alph:
#         stocks = t.get_yahoo_tickers_for(test_db, letter)
#         prices = t.get_prices_from_yahoo(stocks, "2021-01-01", "2021-07-31")
#         print(prices)
#         success = t.save_prices_to_DB(test_db, prices)
#         print(f"\n\nLetter {letter} save status : {success}\n\n")
    
  


#     t.dispose()




    