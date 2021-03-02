# Algorithmic Trading - Python For Fun 

![GitHub](https://img.shields.io/github/license/MapleFrogStudio/AlgorithmicTrading?style=plastic)
![GitHub last commit](https://img.shields.io/github/last-commit/MapleFrogStudio/AlgorithmicTrading?style=plastic)
![PyPI - Python Version](https://img.shields.io/badge/python-3.4%2B-blue?color=blue&style=plastic)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/MapleFrogStudio/AlgorithmicTrading?logo=github&style=plastic)  
  
  
Algorithmic trading (also called automated trading, black-box trading, or algo-trading) uses a coded functions to implement well defined sets of instructions to place trades. This project helps to experiment with python code and theory behind these concepts.  
  
This is a command line tool that simply grabs price data and displays graphs and KPIs using past historical data for a stock ticker. It is not ready for predictions or automatic trading.  
  
Many platforms exist on the Web to automate trading, this project is not intended to replace any of them  
  
This repo is free to fork or download, but has no value as an investment tool. Please do your own research and consult a financial advisor before buying or selling any stocks.  
   
## Data sources experimentation
` yfinance ` python package to extract from the decommissioned Yahoo data API  
` pandas_datareader ` pyhton package to extract data from multiple sources  
` mplfinance ` python pakkage to plot chart data  

## Algorithms and KPIs
- Candlestick graph : Simple display of candlestick graph with colors for bullish and bearish days (no time scale)
- SMA30 : Simple Moving Average - 30 days
- SMA100 : Simple Moving Average - 100 days
- Dual Cross Over Indicator : KPIs that show buy and sell indicators when SMA30 and SMA100 cross each other

## Usage
Clone this repo to your workspace ` git clone https://github.com/MapleFrogStudio/AlgorithmicTrading.git `  
Create a virtual environment ` python -m venv env `  
Upgrade your pip tool ` python -m pip install --upgrade pip `  
Install python packages ` pip install -r requirements.txt `  
Lauch app.py using ` python app.py --help ` to see available available commands

## Experimental stuff
[` streamlit `](https://docs.streamlit.io/en/stable/) open-source Python library that makes it easy to create and share beautiful, custom web apps for machine learning and data science. To launch this viewer from command line : ` streamlit run "./web.py" `  
[` PySimpleGUI `](https://pysimplegui.readthedocs.io/en/latest/) Python GUI For Humans - Transforms tkinter, Qt, Remi, WxPython into portable people-friendly Pythonic interfaces

## Build as an executable file
This project installs the pyinstaller package so you can create a standalone versoon using : ` pyinstaller --onefile app.py `  
  
##     
:frog:  The Maple Frog Studio team hopes you will enjoy this learning project  :frog:  

## External Finance Packages
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/mplfinance?label=mplfinance&logo=pypi&style=plastic)](https://pypi.org/project/mplfinance/)  
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pandas-datareader?label=pandas-datareader&logo=pypi&style=plastic)](https://pypi.org/project/pandas-datareader/)   
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/yfinance?label=yfinance&logo=pypi&style=plastic)](https://pypi.org/project/yfinance/)  
