print("Welcome to ticker program!")
ticker = input("Which ticker symbol would you like to see the price of? ")
ticker_symbols = {
 'AAPL': 46,
 'GOOG': 1,
 'HPQ': 82,
 'INTC': 54,
 'KO': 90,
 'MSFT': 34,
 'TGT': 23,
 'TXN': 10,
 'XOM': 3,
 'WOOF': 102,
 'WMT': 999,
 }
ticker_get = ticker_symbols.get(ticker, "this ticker is not found")
print(f"the price of " + ticker + " is " + str(ticker_get))