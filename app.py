import getopt
from stocks import tsx

from stocks.tsx import TSX
from stocks.gui import GUI

# Create a TSX object
tsx = TSX()

test_db = 'TSX_Data.sqlite'
# Extracte all TSX ticker symbols from the TMX website abd create a SQLITE3 database name TSX_Data.sqlite
tsx.update_all_tickers(test_db)

# Loop through all letters in the alphabet to extract prices data for 2015-01-01 to 2020-12-31
alph = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z', '0-9']

for letter in alph:
    stocks = tsx.get_yahoo_tickers_for(test_db, letter)
    prices = tsx.get_prices_from_yahoo(stocks, "2015-01-01", "2020-12-31")
    print(prices)
    success = tsx.save_prices_to_DB(test_db, prices)
    print(f"\n\nLetter {letter} save status : {success}\n\n")

tsx.dispose()
