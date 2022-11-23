import random
import time
import re

class Account:
	account_number: int

	def __init__(self, account_holder, account_type, credit_score, annual_income, balance = 0):
		self.account_holder = account_holder
		self.account_type = account_type
		self.credit_score = credit_score
		self.annual_income = annual_income
		self.balance = balance

	def account_detail(self):
		print("-----Account Details-----")
		print("Account Holder: ", self.account_holder)
		print("Account Type: ", self.account_type)
		print("Credit Score: ", self.credit_score)
		print("Annual Income: ", self.annual_income)
		print("Balance: ", self.balance)
	
	def check_balance(self):
		print("Your balance is: ", self.balance)


class Debit(Account):
	def __init__(self, account_holder, account_type, credit_score, annual_income, balance, account_number):
		super ().__init__(account_holder, account_type, credit_score, annual_income, balance)
		self.account_number = account_number

	def deposit(self, amount):
		self.balance += amount
		return self.balance

	def withdraw(self, amount):
		self.balance -= amount
		return self.balance

	def account_detail(self):
		super().account_detail()
		print("Account Number: ", self.account_number)
		print("Your balance is: ", self.balance)


class Credit(Account):
	def __init__(self, account_holder, account_type, credit_score, annual_income, account_number, balance, credit_limit = 500):
		super().__init__(account_holder, account_type, credit_score, annual_income, balance)
		self.account_number = account_number
		self.credit_limit = credit_limit
		if 580 <= self.credit_score <= 669 and self.annual_income >= 60000:
			self.credit_limit = 1000
		elif 670 <= self.credit_score <= 739 and self.annual_income >= 80000:
			self.credit_limit = 2000
		elif self.credit_score >= 740 and self.annual_income >= 100000:
			self.credit_limit = 4000
		else:
			self.credit_limit = 500

	def make_purchase(self, purchase_amount):
		self.balance += purchase_amount
		return self.balance
	
	def withdraw(self, amount, balance):
		amount = 1.05 * amount
		if amount > self.credit_limit:
			print("Insufficient funds!")
		else:
			self.balance += amount
			return self.balance
	

	def pay_credit(self, payment_amount):
		self.balance -= payment_amount
		

	def check_balance(self, balance):
		print("Your balance is: ", balance)

	def account_detail(self):
		super().account_detail()
		print("Account Number: ", self.account_number)
		print("Your balance is: ", self.balance)
		print("Your credit limit is: ", self.credit_limit)
		

# def transaction_menu():

# 	print("-----Transaction Menu-----")
# 	print("Please choose from the following options: ")
# 	print("""
# 		TRANSACTION 
# 	*********************
# 		Menu:
# 		1. Account Details
# 		2. Check Balance
# 		3. Deposit (for debit card only)
# 		4. Withdraw (for debit card only)
# 		5. Make a Purchase (for credit card only)
# 		6. Withdraw from Credit Card
# 		7. Make a Payment to Your Credit Card
# 		8. Exit
# 	*********************
# 	""")
# 	menu_input = get_menu_input(input("Please enter your choice: "))


# -----EXCEPTION HANDLING-----


# Exception handling for menu input
def get_menu_input(menu_input):
	menu_dict = {
		"1": Account.account_detail,
		"2": Account.check_balance,
		"3": Debit.deposit,
		"4": Debit.withdraw,
		"5": Credit.make_purchase,
		"6": Credit.withdraw,
		"7": Credit.pay_credit,
		"8": exit
	}


	input("Please enter your choice: ")
	if not re.search(r"[1-8]", menu_input):
		print("Invalid input. Please enter a number between 1 and 8.")
		return get_menu_input(input("Please enter your choice: "))
	else:
		menu_selection = menu_dict[menu_input]
		return menu_selection()
	

# App
	# What route/task are you on
	# What account(s) do you have, type
	# call selected state
		# pass in account, set_state, set_account, go_back

# State
	# __init__
	# def go_back
	# validate
	# account
		# injected from App

# 1. Convert each transaction choice to a State subclass
# 2. Implement or copy/paste logic into subclass
	# a. on_enter = what do we want to run right at the beginning until we need to go back to the home screen
	# b. create other methods to handle each step of the transaction

class State:
	account: Account

	def __init__(self, go_to, set_account, account, go_home) -> None:
		self.go_to = go_to
		self.set_account = set_account
		self.account = account
		self.go_home = go_home
		self.on_enter()

	def on_enter(self):
		pass

	def on_exit(self):
		pass

	def go_home(self):
		pass

	def go_to(self, state: str):
		pass

	def set_account(self, account: Account):
		pass

class Home(State):
		# Exception handling for transaction input
	def get_transaction_choice_input(self, transaction_choice):
		if not re.search("[yYnN]", transaction_choice):
			print("Invalid input. Please enter either y or n.")
			return self.get_transaction_choice_input(input("Would you like to make a transaction? (Y/n): "))
		elif re.search("[nN]", transaction_choice):
			print("Thank you for banking with us!")
			print("Printing receipt...")
			time.sleep(1)
			print("********************************")
			print("Transaction is now complete.")
			print("Transaction number: " + str(random.randint(100000, 1000000)))
			print("Account holder: " + self.account.account_holder)
			print("Account number: " + self.account.account_number)
			print("Thank you for choosing FinTech as your bank!")
			print("********************************")
		elif re.search("[yY]", transaction_choice):
			return self.show_menu()

	def show_menu(self):
		print("-----Transaction Menu-----")
		print("Please choose from the following options: ")
		print("""
			TRANSACTION
		*********************
			Menu:
			1. Account Details
			2. Check Balance
			3. Deposit (for debit card only)
			4. Withdraw (for debit card only)
			5. Make a Purchase (for credit card only)
			6. Withdraw from Credit Card
			7. Make a Payment to Your Credit Card
			8. Exit
		*********************
		""")
		menu_input = get_menu_input(input("Please enter your choice: "))
		self.go_to(menu_input)	

	def on_enter(self):
		self.choose_transaction_type()
		self.show_menu()

    

class CreateAccount(State):
	title = "Create an Account"

	account_type: str
	account_holder: str
	credit_score: int
	annual_income: int

	# Exception handling for account_holder input
	def get_full_name(self, account_holder):
		if not re.search('[a-zA-Z\s]+$', account_holder):
			print("Invalid input. Please enter your full name without any special characters.")
			return self.get_full_name(input("Please enter your full name: "))
		else:
			return ("Account holder: " + account_holder.title())
		# return account_holder.title()
		
	# Exception handling for account_type input
	def get_account_type(self, account_type):
		if account_type.lower() == "debit":
			return "Account type: Debit"

		elif account_type.lower() == "credit":
			return "Account type: Credit"
		else:
			print("Invalid input. Please enter either debit or credit.")
			return self.get_account_type(input("Please enter your account type: "))


	# Exception handling for credit_score input
	def get_credit_score(self, credit_score):
		if not re.search(r"[300-850]", credit_score):
			print("Invalid input. Please enter a number between 300 and 850.")
			return self.get_credit_score(input("Please enter your credit score: "))
		else:
			credit_score = int(credit_score)
			return credit_score

	# Exception handling for annual_income input
	def get_annual_income(self, annual_income):
		if not re.search(r"[0-9]+", annual_income):
			print("Invalid input. Please enter a number greater than 0.")
			return self.get_annual_income(input("Please enter your annual income: "))
		else:
			annual_income = int(annual_income)
			return annual_income

	def new_account_creation(self) -> Account:
		inputted_account_holder = self.get_full_name(input("Please enter your full name: "))
		print(inputted_account_holder)

		inputted_account_type = self.get_account_type(input("Please enter your account type (Debit/Credit): "))
		print(inputted_account_type)

		inputted_credit_score = self.get_credit_score(input("Please enter your credit score: "))
		print(inputted_credit_score)

		inputted_annual_income = self.get_annual_income(input("Please enter your annual income: $"))
		print(inputted_annual_income)

		if self.account_type == "Account type: Debit":
			account_number = random.randint(444400000000, 444499999999)
			new_account = Debit(inputted_account_holder, inputted_account_type, inputted_credit_score, inputted_annual_income, 0, account_number)
			print("Congratulations! Account created successfully.....")
			return new_account
		else:
			account_number = str(random.randint(555500000000, 555599999999))
			new_account = Credit(inputted_account_holder, inputted_account_type, inputted_credit_score, inputted_annual_income, account_number, 0, 500)
			print("Congratulations! Account created successfully.....")
			return new_account

	def select_account_type(self):
		inputted_account_type = self.get_account_type(input("Please enter your account type (Debit/Credit): "))
		print(inputted_account_type)
		self.account_type = inputted_account_type


	def on_enter(self):
		if self.account != None:
			self.go_to('home')

		print('create an account')
		self.init_account_holder()
		self.select_account_type()
		# ...
		new_account = self.new_account_creation()
		new_account.account_detail
		self.set_account(new_account)
		self.go_home()

class AccountDetail(State):
	def on_enter(self):
		self.account.account_detail()
		self.go_home()

class CheckBalance(State):
	def on_enter(self):
		self.account.check_balance()
		self.go_home()

class Deposit(State):
    def on_enter(self):
        self.account.get_deposit_input()
        self.go_home()


class Withdraw(State):
    def on_enter(self):
        self.account.withdraw()
        self.go_home()

class MakePurchase(State):
    def on_enter(self):
        self.account.make_purchase()
        self.go_home()

class WithdrawFromCredit(State):
    def on_enter(self):
        self.account.withdraw_from_credit()
        self.go_home()

class MakePayment(State):
    def on_enter(self):
        self.account.make_payment()
        self.go_home()

class Exit(State):
    def on_enter(self):
        print("Thank you for using our service. Have a nice day!")
        exit()

class App:
	states = {
		000: CreateAccount,
		1: AccountDetail,
		2: CheckBalance,
		3: Debit.deposit,
		4: Debit.withdraw,
		5: Credit.make_purchase,
		6: Credit.withdraw,
		7: Credit.pay_credit,
		8: exit,
		99: Home
	}

	state = None
	account = None
	prevState = None

	def go_home(self):
		self.set_state(9)

	def run_state(self, state):
		print(f"running state")
		state(self.set_state, self.set_account, self.account, self.go_home)

	def set_state(self, state: int):
		print(f"setting state {state}")

		self.state = self.states[state]
		self.run_state(self.state)

	def set_account(self, account: Account):
		self.account = account

	def __init__(self) -> None:
		self.set_state(9)

app = App()

# -----USER INPUT-----
# print("---Welcome to the Bank of FinTech---")
# print("------------------------------------")
# print("Please enter your information below to create an account.")
# print("------------------------------------")
# time.sleep(.25)

# inputted_account_holder = get_full_name(input("Please enter your full name: "))
# print(inputted_account_holder)

# inputted_account_type = get_account_type(input("Please enter your account type (Debit/Credit): "))
# print(inputted_account_type)

# inputted_credit_score = get_credit_score(input("Please enter your credit score: "))
# print(inputted_credit_score)

# inputted_annual_income = get_annual_income(input("Please enter your annual income: $"))
# print(inputted_annual_income)

# def new_account_creation():
# 	if inputted_account_type == "Account type: Debit":
# 		account_number = random.randint(444400000000, 444499999999)
# 		new_account = Debit(inputted_account_holder, inputted_account_type, inputted_credit_score, inputted_annual_income, 0, account_number)
# 		print("Congratulations! Account created successfully.....")
# 		return new_account.account_detail()
# 	elif inputted_account_type == "Account type: Credit":
# 		account_number = str(random.randint(555500000000, 555599999999))
# 		new_account = Credit(inputted_account_holder, inputted_account_type, inputted_credit_score, inputted_annual_income, account_number, 0, 500)
# 		print("Congratulations! Account created successfully.....")
# 		return new_account.account_detail()

# time.sleep(0.75)
# print("********************************")
# print(new_account_creation())

# time.sleep(0.5)

# inputted_transaction_choice = get_transaction_choice_input(input("Would you like to make a transaction? (Y/n): "))


# #inputted_deposit_amount = get_deposit_input(input("Please enter the amount you would like to deposit: "))
# #print(inputted_deposit_amount)

# #inputted_deposit = get_deposit_input(input("Please enter the amount you would like to deposit: "))
# #print(inputted_deposit)



# #print("*******************************")

# #new_user.account_detail()
