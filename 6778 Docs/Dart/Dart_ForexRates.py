import yfinance as yf

# ticker for the USD/CAD currency pair
ticker = yf.Ticker("USDCAD=X")

# exchange rate for USD/CAD
x = ticker.info["regularMarketPrice"]

# ticker for the CAD/USD currency pair
ticker = yf.Ticker("CADUSD=X")

# exchange rate for CAD/USD
y = ticker.info["regularMarketPrice"]

# Print values
print(f"The exchange rate for USD/CAD is {x}")
print(f"The exchange rate for CAD/USD is {y}")