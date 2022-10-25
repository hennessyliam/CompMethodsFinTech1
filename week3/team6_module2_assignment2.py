# Group 6 - Liam Hennessy, Anna Zheng
# PID: Liam - 5499630, Anna - 4397893
# Submission Date: Sep 18, 2022
# A program to demonstrate how to create classes, sub-classes, instances, methods, and how to call information from objects

# Parent class
class Asset:
	def __init__(self, ticker, price, high, low, volume):  # initiates attributes of class
		self.ticker = ticker
		self.price = price
		self.high = high
		self.low = low
		self.volume = volume

	def basic_info(self):  # prints basic Asset's instance basic info
		print("Ticker: {ticker}. Price: {price}. High: {high}. Low: {low}. Volume: {volume}".format(ticker=self.ticker,
																									price=self.price,
																									high=self.high,
																									low=self.low,
																									volume=self.volume))


# child class Stock
class Stock(Asset):
	def __init__(self, ticker, price, high, low, volume, open_p, close_p, earnings):  # initiates attributes of Stock subclass
		super().__init__(ticker, price, high, low, volume)  # pulls these attributes from parent class Asset
		self.open_p = open_p
		self.close_p = close_p
		self.earnings = earnings
		self.rate_return = (self.close_p / self.open_p) - 1

	def update(self, open_p, close_p):  # function/method to update val of open_p and close_p and return rate_return
		self.open_p = open_p
		self.close_p = close_p
		self.rate_return = (close_p / open_p) - 1

	def print_return(self):  # method to print the rate_return value calculated above
		print("The rate of return is: ", self.rate_return)

	def p_e_ratio(self):  # calculates PE ratio based on close_p and earnings instance attributes
		print("The PE ratio is: ", self.close_p / self.earnings)

	def info(self):  # prints info of instance in Stock class
		print("Ticker: ", self.ticker, "Price: ", self.price, "High: ", self.high, "Low: ", self.low,
			  "Volume: ", self.volume, "Opening Price: ", self.open_p, "Closing Price: ", self.close_p, "EPS: ",
			  self.earnings)


# child class Crypto
class Crypto(Asset):
	def __init__(self, ticker, price, high, low, volume, circulating_supply):		# initializes attributes
		super().__init__(ticker, price, high, low, volume)		# pulls these attributes from parent class Asset
		self.circulating_supply = circulating_supply

	def info(self):		# method to print attribute info for an instance
		print("Ticker: ", self.ticker, "Price: ", self.price, "High: ", self.high, "Low: ", self.low,
			  "Volume: ", self.volume, "Circulating Supply: ", self.circulating_supply)


# Driver Code:
# Create the apple object from the Asset class:
apple = Asset('AAPL', 180.5, 200.3, 168.2, 68000000)
print(apple.ticker)  # This returns: AAPL
print(apple.price)  # This returns: 180.5
apple.basic_info()  # This prints: AAPL 180.5 200.3 168.2 68000000

# Create the apple2 object from the Stock class:
apple2 = Stock(apple.ticker, apple.price, apple.high, apple.low, apple.volume, 190.3, 195.4, 6.7)
apple2.info()  # This prints: AAPL 180.5 200.3 168.2 68000000 190.3 195.4 6.7
# We can also call the basic_info() method of the Asset class even though apple2 is a Stock object:
apple2.basic_info()  # This prints: AAPL 180.5 200.3 168.2 68000000

apple2.update(188.8, 198.0)
apple2.print_return()  # This prints: Rate of Return is 0.048728813559322015
apple2.p_e_ratio()  # This prints: The P/E ratio is 29.55223880597015

# Create the bitcoin object from the Asset class:
bitcoin = Asset('BTC', 21548.59, 22534.78, 19879.34, 11700000000)
print(bitcoin.ticker)  # This returns: BTC
print(bitcoin.high)  # This returns: 22534.78
bitcoin.basic_info()  # This prints: BTC 21548.59 22534.78 19879.34 11700000000

# Create the bitcoin2 object from the Crypto class:
bitcoin2 = Crypto(bitcoin.ticker, bitcoin.price, bitcoin.high, bitcoin.low, bitcoin.volume, 19100000)
bitcoin2.info()  # This prints: BTC 21548.59 22534.78 19879.34 11700000000 19100000
# We can also call the basic_info() method of the Asset class even though bitcoin2 is a Crypto object:
bitcoin2.basic_info()  # This prints: BTC 21548.59 22534.78 19879.34 11700000000
