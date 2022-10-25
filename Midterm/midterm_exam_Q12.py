class Client:
	def __init__(self, name, credit_score, income):
		self.name = name
		self.credit_score = credit_score
		self.income = income

	def display(self):
		print(self.name, self.credit_score, self.income)


class Account(Client):
	def __init__(self, name, credit_score, income):
		super().__init__(name, credit_score, income)
		self.balance = 0

	def deposit(self, deposit_amount):
		self.balance += deposit_amount

	def withdrawal(self, withdrawal_amount):
		if withdrawal_amount > self.balance:
			print("Insufficient balance!")
		elif withdrawal_amount >= 100:
			self.balance -= (withdrawal_amount * 0.05 + withdrawal_amount)
		else:
			self.balance -= withdrawal_amount

	def display(self):
		print(self.name, self.credit_score, self.income, self.balance)


# Driver code :
print("TEST.1:")
new_account = Account("Albert", 740, 100000)
# Display account information
new_account.display()
print("TEST.2:")
# Creating Withdrawal Test
new_account.withdrawal(300)
# Display account information
new_account.display()
print("TEST.3:")
# Create deposit test
new_account.deposit(200)
# Display account information
new_account.display()
print("TEST.4:")
# Creating Withdrawal Test
new_account.withdrawal(100)
# Display account information
new_account.display()
print("TEST.5:")
# Creating Withdrawal Test
new_account.withdrawal(20)
# Display account information
new_account.display()
