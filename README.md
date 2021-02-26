# Algorithmic Trading - Python For Fun 

![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/MapleFrogStudio/AlgorithmicTrading?logo=github&style=plastic)
![PyPI - Python Version](https://img.shields.io/badge/python-3.4%2B-blue?color=blue&style=plastic)
![GitHub](https://img.shields.io/github/license/MapleFrogStudio/AlgorithmicTrading?style=plastic)
![GitHub last commit](https://img.shields.io/github/last-commit/MapleFrogStudio/AlgorithmicTrading?style=plastic)


Algorithmic trading (also called automated trading, black-box trading, or algo-trading) uses a coded functions to implement well defined sets of instructions to place trades. This project helps to experiment with python code and theory behind these concepts.  
  
Many platforms exist on the Web to automate trading, this project is not intended to replace any of them  
  
This repo is free to fork or download, but has no value as an investment tool. Please do your own research and consult a financial advisor before buying or selling any stocks.  
   
# Data sources
This project uses the ` yfinance ` python package to extract data from the yahoo finance web site

# Algorithms
- SMA30 : Simple Average Margin over 30 days
- SMA100 : Simple Average Margin over 100 days
- Dual Cross Over : KPIs that show buy and sell indicators when SMA30 and SMA100 cross each other

# Usage
Clone this repo to your workspace ` git clone https://github.com/MapleFrogStudio/AlgorithmicTrading.git `  
Create a virtual environment ` python -m venv env `  
Upgrade your pip tool ` python -m pip install --upgrade pip `  
Install python packages ` pip install -r requirements.txt `  
Lauch app.py using ` python app.py --help ` to see available available commands

# Build as an executable file
This project installs the pyinstaller package so you can create a standalone versoon using : ` pyinstaller --onefile app.py `  
  
    
The Maple Frog Studio team hopes you will enjoy this fun learning project

