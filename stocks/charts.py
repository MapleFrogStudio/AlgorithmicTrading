from tkinter import *
from tkinter import ttk

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import numpy as np
import mplfinance as mpf



class PriceChart:
    def __init__(self, parent, company_info) -> None:
        self.parent = parent
        self.window = Toplevel()
        # self.window.protocol("WM_DELETE_WINDOW", self.parent.quit)

        # Place icon and title on Chart Window
        self.define_window(company_info)

        yahoo_ticker = company_info.get('yahoo')
        # Get prices from local database
        self.prices = self.parent.tsx.read_historical_prices_for(yahoo_ticker)

    def define_window(self, company_info):
        company_name = company_info.get('name')
        self.window.title(company_name)
        self.window.geometry("1400x700+10+10")
        self.window.rowconfigure(0, weight=1)
        self.window.columnconfigure(0, weight=1)
        #self.label = Label(self.window, text=company_name).grid(row=0, column=0, sticky="nsew")

    def plot_chart(self):
        # https://github.com/matplotlib/mplfinance/blob/master/examples/styles.ipynb
        market_colors = mpf.make_marketcolors(
            up='limegreen',
            down='red',
            edge='',
            wick='inherit',
            volume='inherit'
        )
        style = mpf.make_mpf_style(
            base_mpf_style='mike', # binance, blueskies, brasil, charles, checkers, classic, default, mike, nightclouds, sas, starsandstrips, yahoo
            rc={'font.size': 6},
            facecolor="black",
            figcolor="black",
            gridcolor="grey",
            gridstyle="dashed", # solid, dashed, dashdot, dotted, None
            marketcolors=market_colors
        )

        self.fig, _ = mpf.plot(
            self.prices['2020-01-01':'2020-06-28'], 
            type='candle', 
            volume=True,
            style=style, 
            marketcolors=market_colors,
            datetime_format='%Y-%m-%d',
            xrotation=90,
            returnfig=True
        )
        plt.close(self.fig)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.window)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=0,column=0, sticky="nsew")

    def plot_something(self):
        N = 5
        menMeans = (20, 35, 30, 35, -27)
        womenMeans = (25, 32, 34, 20, -25)
        menStd = (2, 3, 4, 1, 2)
        womenStd = (3, 5, 2, 3, 3)
        ind = np.arange(N)    # the x locations for the groups
        width = 0.35       # the width of the bars: can also be len(x) sequence

        fig, ax = plt.subplots()

        p1 = ax.bar(ind, menMeans, width, yerr=menStd, label='Men')
        p2 = ax.bar(ind, womenMeans, width, bottom=menMeans, yerr=womenStd, label='Women')

        ax.axhline(0, color='grey', linewidth=0.8)
        ax.set_ylabel('Scores')
        ax.set_title('Scores by group and gender')
        ax.set_xticks(ind)
        ax.set_xticklabels(('G1', 'G2', 'G3', 'G4', 'G5'))
        ax.legend()       

        # Label with label_type 'center' instead of the default 'edge'
        ax.bar_label(p1, label_type='center')
        ax.bar_label(p2, label_type='center')
        ax.bar_label(p2)         

        plt.close(fig)
        self.canvas = FigureCanvasTkAgg(fig, master=self.window)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=0,column=0, sticky="nsew")


        #Label(self.window, text="Plot Something", bg="LemonChiffon3").grid(row=0, column=0, sticky="nsew")
