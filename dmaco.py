import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

#plt.style.use('fivethirtyeight')
plt.style.use('classic')

# Create simple moving average 30 days window
def CreateSMA30(Stocks):
    SMA30 = pd.DataFrame()
    SMA30['Close'] = Stocks['Close'].rolling(window = 30).mean()
    return SMA30

# Create a simple moving average for 100 days window
def CreateSMA100(Stocks):
    SMA100 = pd.DataFrame()
    SMA100['Close'] = Stocks['Close'].rolling(window=100).mean()
    return SMA100

# Create a new data frame to store all our data
def MergeIndicators(Stocks, SMA30, SMA100):
    data = pd.DataFrame()
    data['Close'] = Stocks['Close']
    data['SMA30'] = SMA30['Close']
    data['SMA100'] = SMA100['Close']

    return data

# Function to show BUY and SELL indicator on the stock prices graph
# TODO: Optimize this function
def BuySell(data):
    sigPriceBuy = []
    sigPriceSell = []
    flag = -1
    #for i in range(data.shape[0]-DateRange, data.shape[0]):
    for i in range(data.shape[0]):
        if data['SMA30'][i] > data['SMA100'][i]:
            if flag != 1:
                sigPriceBuy.append(data['Close'][i])
                sigPriceSell.append(np.nan)
                flag = 1
            else:
                sigPriceBuy.append(np.nan)
                sigPriceSell.append(np.nan)

        elif data['SMA30'][i] <= data['SMA100'][i]:
                if flag != 0:
                    sigPriceBuy.append(np.nan)
                    sigPriceSell.append(data['Close'][i])
                    flag = 0
                else:
                    sigPriceBuy.append(np.nan)
                    sigPriceSell.append(np.nan)
        else:
            sigPriceBuy.append(np.nan)
            sigPriceSell.append(np.nan)

    return (sigPriceBuy, sigPriceSell)

def view_data(df_data, StockTicker):
    plt.figure(figsize=(15,6))
    plt.plot(df_data['Close'], label=StockTicker, alpha = 0.5, color='black')
    plt.plot(df_data['SMA30'], label='SMA30', alpha = 0.35)
    plt.plot(df_data['SMA100'], label='SMA100', alpha = 0.35)
    plt.scatter(df_data.index, df_data['BuyFlag'], label='Buy', marker='^', color='green')
    plt.scatter(df_data.index, df_data['SellFlag'], label='Sell', marker='v', color='red')
    plt.title('Dual Margin Cross Over Indicators SMA30 vs SMA100')
    plt.xlabel('Last ' + str(df_data.shape[0]) + ' Days')
    plt.ylabel('Close price (USD$)')
    plt.legend(loc='upper left')
    plt.show()


def plot_kpis(stocks, ticker):
    SMA30 = CreateSMA30(stocks)
    SMA100 = CreateSMA100(stocks)
    df_data = MergeIndicators(stocks, SMA30, SMA100)
    buy_sell = BuySell(df_data)
    df_data['BuyFlag'] = buy_sell[0]
    df_data['SellFlag'] = buy_sell[1]
    #data = df_data.iloc[df_data.shape[0]-num_days:df_data.shape[0]]
    view_data(df_data, ticker)
