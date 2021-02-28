import io
import os
import requests
import pandas as pd
from datetime import datetime, timedelta
import yfinance as yf
import matplotlib.pyplot as plt
import mplfinance as mpf

# https://pypi.org/project/mplfinance/
# https://towardsdatascience.com/using-python-to-visualize-stock-data-to-candlestick-charts-e1a5b08c8e9c


#plt.style.use('fivethirtyeight')
#plt.style.use('classic')
plt.style.use('ggplot')


def GrabCompaniesFromYahoo():
    y_url="https://pkgstore.datahub.io/core/nasdaq-listings/nasdaq-listed_csv/data/7665719fb51081ba0bd834fde71ce822/nasdaq-listed_csv.csv"
    s = requests.get(y_url).content
    companies = pd.read_csv(io.StringIO(s.decode('utf-8')))
    return companies

def GrabPricesFromYahoo(ticker, days):
    prices = []
    #_start = datetime(2020,1,1)
    #_end = datetime(2020,12,31)
    _end = datetime.today()
    _start = _end + timedelta(days = days * -1)
    _prices = yf.download(ticker,start=_start, end=_end, progress=False)
    return _prices

def MassPricesFromYahoo():
    pass    


def plot_prices(df_data, StockTicker):
    plt.figure(figsize=(15,6))
    plt.plot(df_data['Close'], label='Close', alpha = 0.35)
    plt.title('Historical  closing stock prices')
    plt.ylabel('Close price (USD$)')
    plt.legend(loc='upper left')
    plt.show()


def plot_candlestick(df_data):
    mpf.plot(df_data, mav=(30, 100), type='candle', volume=True, style='yahoo')

