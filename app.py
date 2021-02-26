import sys

from dotenv import load_dotenv
load_dotenv()

# Maple Frog Studio Packages (TODO: Implement as a real package)
import stocks
import dmaco
#from dmaco import *

def show_menu():
    print(f"\nDual Margin Average Cross Over Indicators ( © Maple Frog Studio, 2021, Alpha v0.1)")
    print(f"--- SMA30 vs SMA100")
    print(f"--- Historical pricing from Yahho Finance ---\n")
    print(f"Usage: 'py dmaco.py --option [<ticker> <days>]'")
    print(f"     --yahoo                    : Get list of all companies on yahoo finance")
    print(f"     --info <ticker>            : Get company info for ticker (data from yahoo finance)")
    print(f"     --hist <ticker> <days>     : Show historical stock prices, days = 1000 by default")
    print(f"     --candle <ticker> <days>   : Show Candlestick graph with volumes and 3 SMA?, days = 1000 by default")
    print(f"     --dmaco <ticker> <days>    : Show Dual Margin Cross Over (SMA30 vs SMA100), days = 1000 by default")
    print(f"  [optional values]:") 
    print(f"     <ticker> : Stock ticker of file to load")
    print(f"     <days>   : Number of days to show from latest stock price value (default = 1000 days)")
    
    print(f"\n")

def default_help():
    print(f"\nDual Margin Average Cross Over Indicators ( © Maple Frog Studio, 2021, Alpha v0.1)")
    print(f"Usage: 'py dmaco.py --help'")
    print(f"\n")

def execute_command():
    # TODO: Implement a DRY (Don't Repeat Yourself) code style :)
    if sys.argv[1] == '--help':
        show_menu()
    elif sys.argv[1] == '--yahoo':
        if (len(sys.argv) > 2):
            #ticker = sys.argv[2]
            companies = stocks.GrabCompaniesFromYahoo()
            print(companies)
        else:
            print(stocks.GrabCompaniesFromYahoo())
    elif sys.argv[1] == '--info':
        if (len(sys.argv) > 2):
            ticker = sys.argv[2]
            companies = stocks.GrabCompaniesFromYahoo()
            info = companies[companies['Symbol'] == ticker]
            print(info)
    elif sys.argv[1] == '--hist':
        if (len(sys.argv) > 2):
            ticker = sys.argv[2]
            days = 1000
            if (len(sys.argv) > 3):
                days = int(sys.argv[3])
            prices = stocks.GrabPricesFromYahoo(ticker, days)
            print(prices)
            stocks.plot_prices(prices, ticker)
    elif sys.argv[1] == '--candle':
        if (len(sys.argv) > 2):
            ticker = sys.argv[2]
            days = 1000
            if (len(sys.argv) > 3):
                days = int(sys.argv[3])
            prices = stocks.GrabPricesFromYahoo(ticker, days)
            print(prices)
            stocks.plot_candlestick(prices)            
    elif sys.argv[1] == '--dmaco':
        if (len(sys.argv) > 2):
            ticker = sys.argv[2]
            days = 1000
            if (len(sys.argv) > 3):
                days = int(sys.argv[3])
            prices = stocks.GrabPricesFromYahoo(ticker, days)
            print(prices)
            dmaco.plot_kpis(prices, ticker)
#
# Show menu if executed from command line
if __name__ == '__main__':
    if len(sys.argv) > 1:
        execute_command()
    else:
        default_help()
        
