#import io
#import os
#import requests
#import yfinance as yf
from typing import Text
import pandas as pd
import pandas_datareader as web
from pandas_datareader.nasdaq_trader import get_nasdaq_symbols
from datetime import datetime, timedelta

import matplotlib.pyplot as plt
import mplfinance as mpf

# https://pypi.org/project/mplfinance/
# https://towardsdatascience.com/using-python-to-visualize-stock-data-to-candlestick-charts-e1a5b08c8e9c
# https://pandas-datareader.readthedocs.io/en/latest/remote_data.html


#plt.style.use('fivethirtyeight')
#plt.style.use('classic')
plt.style.use('ggplot')


#
# PANDAS_DATAREADER_FUNCTIONS
#
def NasdaqSymbols():
    symbols = get_nasdaq_symbols()
    return symbols

def GrabPrices(ticker, _start, _end):
    source = 'yahoo'
    ticker = ticker.upper()
    start = pd.to_datetime(_start)
    end = pd.to_datetime(_end)
    data = web.DataReader(ticker, source, start, end)
    return data


def plot_prices(df_data, ticker):
    plt.figure(figsize=(15,6))
    plt.plot(df_data['Close'], label='Close', alpha = 0.35)
    plt.title(f"Prices for {ticker}")
    plt.ylabel('Close price (USD$)')
    plt.legend(loc='upper left')
    plt.show()

def plot_candlestick(df_data):
    mpf.plot(df_data, mav=(30, 100), type='candle', volume=True, style='yahoo')

def fig_candlestick(df_data):
    fig, ax = mpf.plot(df_data, mav=(30, 100), type='candle', volume=True, style='yahoo', returnfig=Text)
    return fig, ax
