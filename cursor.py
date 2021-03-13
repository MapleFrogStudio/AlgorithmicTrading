import datetime

import matplotlib as mp
import matplotlib.pyplot as plt
from matplotlib.widgets import Cursor, Button

import numpy as np
import pandas as pd
import mplfinance as mpf

import stocks
ticker1 = "MSFT"         # Microsoft
ticker2 = "NTDOY"        # Nintendo

start = "2000-01-01"
end = "2021-02-28"
prices1 = stocks.GrabPrices(ticker1, start, end)
prices2 = stocks.GrabPrices(ticker2, start, end)

# print(prices1.tail(5).round(0))
# print(prices2.tail(5).round(0))

# https://github.com/matplotlib/mplfinance/blob/master/examples/addplot.ipynb

#ax = mpf.make_addplot(prices1['Close'].loc['2020']-50)
# ax = mpf.make_addplot(prices2['Low'].loc['2020'], type='line')
# bx = mpf.make_addplot(prices2['High'].loc['2020'], type='scatter')
# mpf.plot(prices1.loc['2020'], type='candle', style='yahoo', addplot=[ax,bx])


fig1, axe1 = plt.subplots()

#p, = plt.plot(prices1['Close'].loc['2020-02'], 'o')

p, = mpf.plot(prices1.loc['2020'], type='candle', volume=True, style='yahoo')
cursor = Cursor(axe1, 
                horizOn = True,
                vertOn = True,
                color='green',
                linewidth=2.0
               )

def onclick(event):
    x1, y1 = mp.dates.num2date(event.xdata).strftime('%Y-%m-%d'), event.ydata.round(2)
    print(f"({x1},{y1})")

fig1.canvas.mpl_connect('button_press_event', onclick)


plt.show()