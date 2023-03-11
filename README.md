# ARCHIVED - Project not maintained
  

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
`git clone https://github.com/MapleFrogStudio/AlgorithmicTrading.git ` : Clone this repo to your workspace  
` python -m venv env ` : Create a virtual environment  
` env\Scripts\Activate ` :Activate the virtual environment (windows)  
` python -m pip install --upgrade pip ` : Upgrade your pip tool  
` pip install -r requirements.txt ` : Install python packages  

The selenium package controls a web browser installed on your local machine. Please follow instructions on the pypi installation page : https://pypi.org/project/selenium/ to setup correctly. In a word, you need a special program called "chromedriver.exe" that will be accessible by your app. In the TSX_Browser class located in the stocks\tsx .py module set the self.__CHROME_DRIVER_LOCATION to the location of that file. The [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) program is produced and distributed by google.

#### Usage
Once installation is complete, run ` python app.py ` to populate a SQLITE3 database named 'TSX_Data.sqlite' with historical prices for all TSX symbols between 2015-01-01 to 2020-12-31. 
To change dates for historical data download, open app.py and change the following varoables : start_date, end_date to a 'yyyy-mm-dd' format. Be careful this app does not prevent duplicate dates for historical data, so if you download the same date twice, the database will have doubles.  
  
If you want to remove duplicate rows from every table in your database, use ` python clean.py `. This will  
1- create a temporary backup of your database,  
2- create a new database with cleaned tables,  
3- delete the original database,  
4- rename the cleaned database to the originale database name 
5- remove the backup database.  
(Make sure you have enough disk space ofr this operation).


#### Viewing Data
Use a SQLITE database browser to view the downloaded data.
One free and open source tool is [DB Browser for SQLite](https://sqlitebrowser.org/).

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
