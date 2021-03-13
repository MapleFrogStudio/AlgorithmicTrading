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

    return fig

def add_fig(df, fig):
    #fig = go.Figure()
    fig.add_trace(go.Candlestick(
        x=df['Date'],
        open  = df['Open'],
        high  = df['High'],
        low   = df['Low'],
        close = df['Close']        
    ))
    return fig

def multi_stock(fig,p1,p2,p3):
    fig1 = go.Candlestick(x=p1.Date, y=p1, mode='lines', name='Apple')
    fig2 = go.Candlestick(x=p2.Date, y=p2, mode='lines+markers', name='Amazon')
    fig3 = go.Candlestick(x=p3.Date, y=p3, mode='lines', name='Google', line=dict(color='firebrick', width=2, dash='dashdot'))
    fig.add_trace(fig1)
    return fig


if __name__ == '__main__':
    p1 = stocks.GrabPrices("AAPL", "2020-06-01", "2021-01-31")
    p1.reset_index(inplace=True)
    p1 = p1.rename(columns = {'index':'Date'})
    p2 = stocks.GrabPrices("AMZN", "2020-06-01", "2021-01-31")
    p2.reset_index(inplace=True)
    p2 = p2.rename(columns = {'index':'Date'})
    p3 = stocks.GrabPrices("GOOG", "2020-06-01", "2021-01-31")
    p3.reset_index(inplace=True)
    p3 = p3.rename(columns = {'index':'Date'})
    fig = go.Figure()
    multi_stock(fig, p1, p2, p3)
    fig.show()
    

    # f = create_chart(prices)
    # f.show()






