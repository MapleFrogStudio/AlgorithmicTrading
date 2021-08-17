import logging
from stocks import tsx

from stocks.tsx import TSX

logging.basicConfig(
    filename="logs.log",
    filemode="w",
    level=logging.INFO,
    format="{asctime} {levelname:<8} {message}",
    style='{'
)

# Date range for historical data download
start_date = "2015-01-01"
end_date   = "2020-12-31"
logging.info(f"Initiating update_all_tickers_for using (start_date : {start_date}, end_date: {end_date}) ")
# Create a TSX object

tsx = TSX()
test_db = 'TSX_Data.sqlite'
logging.info(f"Target database to store information: {test_db}) ")
# Extracte all TSX ticker symbols from the TMX website abd create a SQlogging.info(f"Initiating update_all_tickers_for with (start_date : {start_date}, end_date: {end_date}) ")LITE3 database name TSX_Data.sqlite
tsx.update_all_tickers(test_db, progess=True)
logging.info(f"Extraction and storing of all ticker symbols completed")

# Loop through all letters in the alphabet to extract prices data for 2015-01-01 to 2020-12-31
logging.info(f"Looping through all letters to scrap data from tsx website ")
alph = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
for letter in alph:
    logging.info(f"get_yahoo_tickers_for_({letter}) ")
    stocks = tsx.get_yahoo_tickers_for(test_db, letter)
    logging.info(f"get_prices_from_yahoo_for : {stocks}")
    prices = tsx.get_prices_from_yahoo(stocks, start_date, end_date)
    print(prices)
    logging.info(f"save_prices_to_DB() ")
    success = tsx.save_prices_to_DB(test_db, prices)
    print(f"\n\nLetter {letter} save status : {success}\n\n")
    logging.info(f"Save prices to DB succesful for letter : {letter}")

tsx.remove_duplicates(test_db)

logging.info(f"Disposing of tsx object ")
tsx.dispose()
