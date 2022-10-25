class CreditCard:
	def __init__(self, customer, bank, account, limit):
		self.customer = customer
		self.bank = bank
		self.acnt = account
		self.limit = limit
		self.balance = 0

	def get_customer(self):
		return self.customer

	def get_bank(self):
		return self.bank

	def get_acnt(self):
		return self.acnt

	def get_limit(self):
		return self.limit

	def get_balance(self):
		return self.balance

	def charge(self, price):
		# charge given price to the card

		if price + self.balance > self.limit:
			return False
		else:
			self.balance += price
			return True

	def make_payment(self, amount):
		self.balance -= amount


# Driver code:

if __name__ == '__main__':
	wallet = []
	wallet.append(CreditCard("John B", "California Sav", "1111", 2500))
	wallet.append(CreditCard("John B", "California Fed", "2222", 3500))
	wallet.append(CreditCard("John B", "California Fin", "3333", 5000))

	for val in range(1, 17):
		wallet[0].charge(val)
		wallet[1].charge(2 * val)
		wallet[2].charge(3 * val)

	# first card that has limit 2500, is charged 136 so, its balance is 136
	# second card that has limit 3500, is charged 272 so its balance is 272
	# thirs card that has limit 5000, is charge 408 so its balance is 408

	for c in range(3):
		print('Customer =', wallet[c].get_customer())
		print('Bank = ', wallet[c].get_bank())
		print('Account =', wallet[c].acnt)
		print('Limit = ', wallet[c].limit)
		print('Balance =', wallet[c].balance)
		while wallet[c].get_balance() > 100:
			wallet[c].make_payment(100)
			print('New balance =', wallet[c].get_balance())
		
