import stocks

# nasdaq = stocks.NasdaqSymbols()
# print(f"liste: {nasdaq}")

msft = stocks.GrabPrices("MSFT","2020-01-01", "2021-02-28")
print(msft)

aapl = stocks.GrabOptions("AAPL")
print(aapl)

