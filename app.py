import getopt
from stocks import tsx

from stocks.tsx import TSX
from stocks.gui import GUI

# TSX MODULE
#
# TSX.update_all_tickers('database') : grabs all tickers symbols listed on the TSX and TSX Venture and store them in a SQLite3 database
# TSX.get_yahoo_tickers_for('database', 'search_str') : obtain a list of tickers statring with <search_str> from the SQLite3 'database'
#
# Loop through ticker symbol list to obtain historical price data and stire values in database
# One table per ticker symbol will be created
# Be careful, extraction of same date will create duplicates.
#
# TSX.get_prices_from_yahoo(stocks, "2021-01-01", "2021-07-31")
# TSX.save_prices_to_DB('database', prices)
#

# Create a tsx object to use the functions avaiable
tsx = TSX()
gui = GUI()
tsx.dispose()
