from datetime import datetime, timedelta
import time
import sys
import json

from dotenv import load_dotenv
load_dotenv()

from IPython.display import display

# Maple Frog Studio Packages (TODO: Implement as a real package)
import stocks
import dmaco


def show_menu():
    print(f"\nDual Margin Average Cross Over Indicators ( © Maple Frog Studio, 2021, Alpha v0.1)")
    print(f"--- SMA30 vs SMA100")
    print(f"--- Historical pricing from Yahho Finance ---\n")
    print(f"Usage: 'py cli.py --option [<ticker> <days>]'")
    print(f"     --nasdaq                   : Get list of nasdaq companies")
    print(f"     --info <ticker>            : Get company info for ticker (data from yahoo finance)")
    print(f"     --hist <ticker> <days>     : Show historical stock prices, days = 1000 by default")
    print(f"     --candle <ticker> <days>   : Show Candlestick graph with volumes and 3 SMA?, days = 1000 by default")
    print(f"     --dmaco <ticker> <days>    : Show Dual Moving Average Cross Over (SMA30 vs SMA100), days = 1000 by default")
    print(f"  [optional values]:") 
    print(f"     <ticker> : Stock ticker of file to load")
    print(f"     <days>   : Negative Number of days to show from latest stock price value (default = -1000 days)")
    
    print(f"\n")

def default_help():
    print(f"\nDual Margin Average Cross Over Indicators ( © Maple Frog Studio, 2021, Alpha v0.1)")
    print(f"Usage: py cli.py --help")
    print(f"\n")



def execute_command():
    # TODO: Implement a DRY (Don't Repeat Yourself) code style :)
    if sys.argv[1] == '--go':
        prices = stocks.GrabPricesFromQuandl("TSLA", 500)
        print(prices)

    elif sys.argv[1] == '--help':
        show_menu()

    elif sys.argv[1] == '--nasdaq':
        companies = stocks.NasdaqSymbols()
        print(companies)

    elif sys.argv[1] == '--info':
        if (len(sys.argv) > 2):
            ticker = sys.argv[2]
            companies = stocks.NasdaqSymbols()
            info = companies[companies['NASDAQ Symbol'] == ticker]
            info_dict = dict(zip(info.columns.values,info.values[0]))
            print(json.dumps(info_dict, indent=2))
            #print(info.to_json(indent=True))   # Not very pretty

    elif sys.argv[1] == '--hist':
        if (len(sys.argv) > 2):
            ticker = sys.argv[2]
            end = datetime.today()
            days = 1000
            if (len(sys.argv) > 3):
                days = int(sys.argv[3])
            start = datetime.today() - timedelta(int(days))
            prices = stocks.GrabPrices(ticker, start, end)
            print(prices)
            stocks.plot_prices(prices, ticker)

    elif sys.argv[1] == '--candle':
        if (len(sys.argv) > 2):
            ticker = sys.argv[2]
            end = datetime.today()
            days = 1000
            if (len(sys.argv) > 3):
                days = int(sys.argv[3])
            start = datetime.today() - timedelta(int(days))                
            prices = stocks.GrabPrices(ticker, start, end)
            print(prices)
            stocks.plot_candlestick(prices) 

    elif sys.argv[1] == '--dmaco':
        if (len(sys.argv) > 2):
            ticker = sys.argv[2]
            end = datetime.today()
            days = 1000
            if (len(sys.argv) > 3):
                days = int(sys.argv[3])
            start = datetime.today() - timedelta(int(days))                                
            prices = stocks.GrabPrices(ticker, start, end)
            print(prices)
            dmaco.plot_kpis(prices, ticker)
#
# Show menu if executed from command line
if __name__ == '__main__':
    if len(sys.argv) > 1:
        execute_command()
    else:
        default_help()
        
