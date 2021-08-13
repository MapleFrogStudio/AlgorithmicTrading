# NEW START 2021-08-13    
# Algorithmic Trading - Python For Fun 

![GitHub](https://img.shields.io/github/license/MapleFrogStudio/AlgorithmicTrading?style=plastic)
![GitHub last commit](https://img.shields.io/github/last-commit/MapleFrogStudio/AlgorithmicTrading?style=plastic)
![PyPI - Python Version](https://img.shields.io/badge/python-3.4%2B-blue?color=blue&style=plastic)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/MapleFrogStudio/AlgorithmicTrading?logo=github&style=plastic)  
  
  
Algorithmic trading (also called automated trading, black-box trading, or algo-trading) uses coded functions to implement well defined sets of instructions to place trades. This project helps to experiment with python code and theory behind these concepts.  

This project works with the Canadian Stocks market (more specifically TSX and TSX Venture ticker symbols).

##### Disclaimer:
This repo is free to fork or download, **but has no value as an investment tool.** 
Please do your own research and consult a financial advisor before buying or selling any stocks.

## 2021-08-13 Features
- stocks\tsx.py : offers classes and methods to populate a SQLite3 database with all ticker symbols listed on the tsx. It also provides functions to download historical data from the yahoo finance api.
` See issues for current bugs - some tickers do not return any data from yahoo finance (needs to be investigated) `  
 

#### Installation
Clone this repo to your workspace ` git clone https://github.com/MapleFrogStudio/AlgorithmicTrading.git `  
Create a virtual environment ` python -m venv env `  
Upgrade your pip tool ` python -m pip install --upgrade pip `  
Install python packages ` pip install -r requirements.txt ` 

#### Usage


# Packages
#### Python packages
` pandas ` pyhton package to work with data frames  
` pandas_datareader ` pyhton package to extract data from yahoo finance  
` sqlalchemy ` pyhton package for database management (required by some pandas fuctions)  
` logging ` pyhton package to print errors when things go wrong  
` selenium ` pyhton package to extract data from web sites  
` python-dotenv ` pyhton package to manage environment variables     

#### External Finance Packages
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pandas-datareader?label=pandas-datareader&logo=pypi&style=plastic)](https://pypi.org/project/pandas-datareader/)  

 

  
#### Usage (as of 2021-08-13)



:frog:  The Maple Frog Studio team hopes you will enjoy this learning project  :frog:  

 

