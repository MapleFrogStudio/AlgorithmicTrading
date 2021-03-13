import plotly.graph_objects as go
import pandas as pd
import stocks



def create_chart(df):
    fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                            open  = df['Open'],
                            high  = df['High'],
                            low   = df['Low'],
                            close = df['Close'])
    ])

    fig.show()


if __name__ == '__main__':
    prices = stocks.GrabPrices("MSFT", "2020-06-01", "2021-01-31")
    prices.reset_index(inplace=True)
    prices = prices.rename(columns = {'index':'Date'})
    create_chart(prices)



