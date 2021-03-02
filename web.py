# Stock market dashboard to show chatrs and data on stocks
# streamlit run "./web.py"
import streamlit as st
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt

import stocks

nasdaq = stocks.NasdaqSymbols()

def get_input():
    start_date = st.sidebar.text_input("Start date", "2020-01-01")
    end_date = st.sidebar.text_input("End date", "2021-01-31")
    stock_symbol = st.sidebar.text_input("Stock Symbol", "AMZN")
    return start_date, end_date, stock_symbol

def get_company_name(stock_symbol):
    # Global nasdaq ticker symbols and information
    name = nasdaq.loc[stock_symbol].loc['Security Name']
    name = name[0:name.find('-')]
    return name

def load_stock_data(ticker, _start, _end):
    # Grab historic data from yahoo
    data = stocks.GrabPrices(ticker, _start, _end)
    return data


# my_ticker = 'AMZN'
# print(get_company_name(my_ticker))
# print(load_stock_data(my_ticker, '2020-01-01', '2021-01-31'))


st.write("""
# Stock Market Web Application 
""")

image = Image.open("./candles.jpg")
st.image(image, use_column_width=True)
st.sidebar.header('User input')

# Get the user's input data rom stream
start, end, symbol = get_input()
df_data = load_stock_data(symbol, start, end)
name = get_company_name(symbol)

# Dislay the close price
st.header(name+" Close Price\n")
#st.line_chart(data['Close'])


fig = plt.figure(figsize=(15,6))
plt.plot(df_data['Close'], label=symbol, alpha = 0.5, color='black')
plt.legend(loc='upper left')
#plt.show()
st.pyplot(fig)