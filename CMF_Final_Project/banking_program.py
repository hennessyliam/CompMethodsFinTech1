import random
import time
import re
import string

# allowed charcters used throughout program
allowed_chars = string.ascii_letters 
allowed_digits = string.digits

# creating Account class
class Account:
	account_number: int

	def __init__(self, account_holder, account_type, credit_score, annual_income, credit_limit, balance = 0):
		self.account_holder = account_holder
		self.account_type = account_type
		self.credit_score = credit_score
		self.annual_income = annual_income
		self.balance = balance
		self.credit_limit = credit_limit

	# method to produce account details
	def account_detail(self):
		print("-----Account Details-----")
		print("Account Holder: ", self.account_holder)
		print("Account Type: ", self.account_type.title())
		print("Credit Score: ", self.credit_score)
		print("Annual Income: $", self.annual_income)


	# blank methods for reference by State Class
	def check_balance(self):
		print("Your balance is ${self.balance}")

	def deposit(self, amount):
		pass

	def debit_withdraw(self, amount):
		pass

	def make_purchase(self, amount):
		pass

	def credit_withdraw(self, amount):
		pass

	def pay_credit(self, amount):
		pass

# creating subclass of Account, Debit
class Debit(Account):
	def __init__(self, account_holder, account_type, credit_score, annual_income, balance, account_number):
		super ().__init__(account_holder, account_type, credit_score, annual_income, balance)
		self.account_number = account_number
	
	# methods to handle debit account transactions
	def deposit(self, amount):
		if amount < 0:
			print("You cannot deposit a negative amount")
		else:
			self.balance += amount

	def debit_withdraw(self, amount):
		self.balance -= amount

	# produces elements of account details and debit account specific details
	def account_detail(self):
		super().account_detail()
		print("Account Number: ", self.account_number)
		print(f"Account Balance: {self.balance}")


# creating subclass of Account, Credit
class Credit(Account):
	def __init__(self, account_holder, account_type, credit_score, annual_income, account_number, balance, credit_limit = 500):
		super().__init__(account_holder, account_type, credit_score, annual_income, balance)
		self.account_number = account_number
		self.credit_limit = credit_limit
	
	# 'calculates' credit limit based off of credit score and annual income
		if 580 <= self.credit_score <= 669 and self.annual_income >= 60000:
			self.credit_limit = 1000
		elif 670 <= self.credit_score <= 739 and self.annual_income >= 80000:
			self.credit_limit = 2000
		elif self.credit_score >= 740 and self.annual_income >= 100000:
			self.credit_limit = 4000
		else:
			self.credit_limit = 500

	# handles if user inputs tries to deposit into a credit account
	def deposit(self, amount):
		print("You cannot deposit money into a credit account!")

	# logic for credit purchase transaction
	def make_purchase(self, purchase_amount):
		if purchase_amount > self.credit_limit:
			print("You cannot purchase more than your credit limit!")
		elif (purchase_amount + self.balance) > self.credit_limit:
			print("You cannot purchase more than your credit limit!")
		else:
			self.balance += purchase_amount
			return self.balance, self.credit_limit
	
	# logic for credit withdraw transaction
	def credit_withdraw(self, amount):
		amount = 1.05 * amount
		if amount > self.credit_limit:
			print("Insufficient funds!")
		#elif (amount + self.balance) > self.credit_limit:
			#print("Credit limit exceeded!")
		else:
			self.balance += amount
			return self.balance
	
	# logic for credit account balance check
	def pay_credit(self, payment_amount):
		self.balance -= payment_amount

	# produces elements of account details and credit account specific details
	def account_detail(self):
		super().account_detail()
		print("Account Number: ", self.account_number)
		print("Your balance is: ", self.balance)
		print("Your credit limit is: ", self.credit_limit)
		

# the State class is responsible for getting user input, displaying the UI in the console and validations
class State:
	account: Account
	title: str
	
	# intializes methods that control the UI
	def __init__(self, go_to, set_account, account, go_home) -> None:
		self.go_to = go_to
		self.go_home = go_home
		self.set_account = set_account
		self.account = account
		self.on_enter()

	# blanks methods to be referenced by subclasses
	# may include functionality later if applicable
	def on_enter(self):
		pass

	def on_exit(self):
		pass

	def go_home(self):
		pass

	def go_to(self, state: int):
		pass

	def set_account(self, account: Account):
		pass

	def set_credit_limit(self, credit_limit: int):
		pass

# the Home class is responsible for displaying the transaction UI which is the main UI
class Home(State):
	# Exception handling for transaction input
	def should_show_menu(self):
		transaction_choice = input("Would you like to make a transaction? (Y/n): ")
		if not re.search("[yYnN]", transaction_choice):
			print("Invalid input. Please enter either y or n.")
			return self.should_show_menu()
		elif re.search("[nN]", transaction_choice):
			return False
		elif re.search("[yY]", transaction_choice):
			return True

	# transaction menu
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

		# handles transaction input
		menu_input = input("Please enter your choice from 1-8: ")
		if not all(menu_input.isdigit() and len(menu_input) == 1 for menu_input in menu_input):
			print("Invalid input. Please enter a number from 1-8.")
			return self.show_menu()
		else:
			if 1 < int(menu_input) > 8:
				print("Invalid input. Please enter a number from 1-8.")
				return self.show_menu()
			else:
				self.go_to(int(menu_input))
	
	# this is what the app runs when the state is initialized
	def on_enter(self):
		should_show_menu = self.should_show_menu()
		if should_show_menu:
			self.show_menu()
		else:
			self.go_to(8)

# the CreteAccount subclass of State, is responsible for creating a new account
class CreateAccount(State):
	title = "Create an Account"

	# sets what date type each input should be
	account_type: str
	account_holder: str
	credit_score: int
	annual_income: int
	credit_limit: int
	balance: int

	# Exception handling for account_holder input
	def get_full_name(self, account_holder):
		# only allow letters, spaces, and hyphens using string library
		if not re.search("^[a-zA-Z -]*$", account_holder):
			print("Invalid input. Please enter your full name without any special characters.")
			return self.get_full_name(input("Please enter your full name: "))
		else:
			if not len(account_holder) > 0:
				print("Invalid input. Please enter your full name.")
				return self.get_full_name(input("Please enter your full name: "))
			else:
				return account_holder.title()

		
	# Exception handling for account_type input
	def get_account_type(self, account_type):
		if account_type != "debit" and account_type != "credit":
			print("Invalid input. Please enter either debit or credit.")
			return self.get_account_type(input("Please enter your account type: "))
		else:
			return account_type


	# Exception handling for credit_score input
	def get_credit_score(self, credit_score):
		# only allow credit_score to be a number between 300 and 850

		if not re.search('[0-9]+$', credit_score):
			print("Invalid input. Please enter a number between 300 and 850.")
			return self.get_credit_score(input("Please enter your credit score: "))
		try:
			credit_score = int(credit_score)
			if credit_score < 300 or credit_score > 850:
				raise ValueError

		except ValueError:
			print("Invalid input. Please enter a number between 300 and 850.")
			return self.get_credit_score(input("Please enter your credit score: "))
		else:
			credit_score = int(credit_score)
			return credit_score

	# Exception handling for annual_income input
	def get_annual_income(self, annual_income):
		if not re.search(r"[0-9]+", annual_income):
			print("Invalid input. Please enter a greater than or equal to 0.")
			return self.get_annual_income(input("Please enter your annual income: $"))
		else:
			annual_income = int(annual_income)
			return annual_income

	# driver that created account initialy  
	def new_account_creation(self) -> Account:
		inputted_account_holder = self.get_full_name(input("Please enter your full name: "))

		inputted_account_type = self.get_account_type(input("Please enter your account type (Debit/Credit): "))
		self.account_type = inputted_account_type.title()

		inputted_credit_score = self.get_credit_score(input("Please enter your credit score: "))

		inputted_annual_income = self.get_annual_income(input("Please enter your annual income: $"))


	# creates account number according to account type and instantiates the object in its respective class
		if self.account_type == "Debit":
			account_number = random.randint(444400000000, 444499999999)
			new_account = Debit(inputted_account_holder, inputted_account_type, inputted_credit_score, inputted_annual_income, 0, account_number)
			print("Congratulations! Account created successfully.....")
			return new_account
		else:
			account_number = str(random.randint(555500000000, 555599999999))
			new_account = Credit(inputted_account_holder, inputted_account_type, inputted_credit_score, inputted_annual_income, account_number, 0, 500)
			print("Congratulations! Account created successfully.....")
			return new_account


			
	# this is what the app runs when the state is initialized i.e. when the user chooses to create an account
	def on_enter(self):
		if self.account != None:
			self.go_home()

		# self.init_account_holder()
		print("                                        ")
		print("******* WELCOME TO BANK OF FINTECH *******")
		print("___________________________________________________________")
		print("Please create an account:")
		new_account = self.new_account_creation()
		new_account.account_detail
		self.set_account(new_account)
		self.go_home()


# this class calls the account_details method from the Account class when selected in the transaction menu
class AccountDetail(State):
	def on_enter(self):
		self.account.account_detail()
		time.sleep(0.5)
		self.go_home()


# this class calls the check_balance method from the Account class when selected in the transaction menu
class CheckBalance(State):
	def on_enter(self):
		print(f"Your current account balance is ${self.account.balance}")
		time.sleep(0.5)
		self.go_home()


# this class calls the account detail method from the Account class when selected in the transaction menu
class Deposit(State):
	title = "Deposit"

	# Exception handling for deposit input
	def get_deposit_input(self) -> int:  # type: ignore

		# only allow deposit if account is a debit account
		if self.account.account_type.title() != "Debit":
			print("You cannot deposit into a credit account.")
			self.go_home()
	
		deposit_amount = input("Please enter the amount you would like to deposit into your debit account: $")

		# handles all bad inputs for deposit
		if not (x.isdigit() for x in deposit_amount):
			print("Invalid input. Please enter a number greater than 0.")
			return self.get_deposit_input()
		elif int(deposit_amount) < 0:
			print("Invalid input. Please enter a number greater than 0.")
			return self.get_deposit_input()
		elif int(deposit_amount) == 0:
			print("Transaction cancelled.")
			time.sleep(0.5)
			self.go_home()
		else:
			debit_deposit = int(deposit_amount)
			return debit_deposit

	# this is what the app runs when the state is initialized i.e. when the user chooses to deposit
	def on_enter(self):
		deposit_amount = self.get_deposit_input()
		self.account.deposit(deposit_amount)

		print("Deposit successful!")
		print(f"Your current account balance is ${self.account.balance}")
		time.sleep(0.5)

		self.go_home()


class DebitWithdraw(State):
	
	# exception handling for debit withdraw input
	def get_deb_withdraw_input(self) -> int:  # type: ignore

		# only allows withdraw if account type is debit
		if self.account.account_type.title() != "Debit":
			print("You cannot withdraw from a credit account.")
			self.go_home()

		debit_withdrawal_amount = input("Please enter the amount you would like to withdraw: $")

		# handles all bad inputs for debit withdraw
		if not re.search(r"[0-9]+", debit_withdrawal_amount):
			print("Invalid input. Please enter a number greater than 0.")
			return self.get_deb_withdraw_input()
		elif int(debit_withdrawal_amount) > self.account.balance:
			print("Insufficient funds!")
			print(f"Please enter a number less than your account balance of ${self.account.balance}.")
			return self.get_deb_withdraw_input()
		elif int(debit_withdrawal_amount) < 0:
			print("Invalid input. Please enter a number greater than 0.")
			return self.get_deb_withdraw_input()
		elif int(debit_withdrawal_amount) == 0:
			print("Transaction cancelled.")
			time.sleep(0.5)
			self.go_home()
		else:
			withdraw = int(debit_withdrawal_amount)
			return withdraw

	# this is what the app runs when the state is initialized i.e. when the user chooses to withdraw from debit account
	def on_enter(self):

		debit_withdraw_amount = self.get_deb_withdraw_input()
		self.account.debit_withdraw(debit_withdraw_amount)

		print("Withdrawal successful!")
		print(f"Your account balance is ${self.account.balance}")
		time.sleep(0.5)

		self.go_home()


class MakePurchase(State):

	# exception handling for purchase input
	def get_purchase_input(self) -> int: # type: ignore

		# only allows purchase if current account state is a credit account
		if self.account.account_type.title() != "Credit":
			print("You cannot make a purchase from a debit account.")
			self.go_home() 

		purchase_amount = input("Please enter the amount you would like to purchase: $")

		# handles all bad inputs for purchase amount
		if not re.search(r"[0-9]+", purchase_amount):
			print("Invalid input. Please enter a number greater than 0.")
			return self.get_purchase_input()
		elif int(purchase_amount) < 0:
			print("Invalid input. Please enter a number greater than 0.")
			return self.get_purchase_input()
		elif int(purchase_amount) > self.account.credit_limit:
			print(f"Insufficient credit. Please enter a number less than your credit limit of ${self.account.credit_limit}.")
			return self.get_purchase_input()
		elif int(purchase_amount) + self.account.balance > self.account.credit_limit:
			print(f"Insufficient credit.")
			print(f"Please enter a number less than or equal to your current remaining credit limit of ${self.account.credit_limit - self.account.balance}.")
			return self.get_purchase_input()
		elif int(purchase_amount) == 0:
			print("Transaction cancelled.")
			time.sleep(0.5)
			self.go_home()
		else:
			purchase = int(purchase_amount)
			return purchase

	# this is what the app runs when the state is initialized i.e. when the user chooses to make a purchase from their credit account
	def on_enter(self):

		purchase_amount = self.get_purchase_input()
		self.account.make_purchase(purchase_amount)

		print("Purchase successful!")
		print(f"Your credit balance is ${self.account.balance}")
		time.sleep(0.5)

		self.go_home()

class CreditWithdraw(State):

	# exception handling for credit withdraw input
	def get_cred_withdraw_input(self) -> int: # type: ignore

		# only allows withdraw if account type is credit
		if self.account.account_type.title() != "Credit":
			print("You cannot withdraw from a debit account.")
			self.go_home()
		
		credit_withdrawal_amount = input("Please enter the amount you would like to withdraw: $")

		# handles all bad inputs for credit withdraw
		if not re.search(r"[0-9]+", credit_withdrawal_amount):
			print("Invalid input. Please enter a number.")
			return self.get_cred_withdraw_input()

		elif (int(credit_withdrawal_amount) * 1.05) > (self.account.credit_limit - self.account.balance):
			print(f"Insufficient credit.")
			print(f"Please enter a number less than or equal to your current remaining credit limit of ${self.account.credit_limit - self.account.balance}.")
			print(f"Please also consider the 5% fee charged on withdrawing from your credit account.") # type: ignore
			return self.get_cred_withdraw_input()
		elif int(credit_withdrawal_amount) < 0:
			print("Invalid input. Please enter a number greater than 0.")
			return self.get_cred_withdraw_input()
		elif int(credit_withdrawal_amount) == 0:
			print("Transaction cancelled.")
			time.sleep(0.5)
			self.go_home()
		else:
			withdraw = int(credit_withdrawal_amount)
			return withdraw

	# this is what the app runs when the state is initialized i.e. when the user chooses to withdraw from credit account
	def on_enter(self):
		
		credit_withdraw_amount = self.get_cred_withdraw_input()
		self.account.credit_withdraw(credit_withdraw_amount)

		print("Withdrawal successful!")
		print(f"Your credit balance is ${self.account.balance}")
		time.sleep(0.5)

		self.go_home()


class PayCredit(State):

	# exception handling for credit pay input
	def get_payment_input(self) -> int: # type: ignore

		# only allows payment if account type is credit
		if self.account.account_type.title() != "Credit":
			print("You cannot make a payment to a debit account.")
			self.go_home() 

		payment_amount = input("Please enter the amount you would like to pay: $")

		# handles all bad inputs for payment amount
		if not re.search(r"[0-9]+", payment_amount):
			print("Invalid input. Please enter a number.")
			return self.get_payment_input()
		elif int(payment_amount) < 0:
			print("Invalid input. Please enter a number greater than 0.")
			return self.get_payment_input()
		elif int(payment_amount) == 0:
			print("Transaction cancelled.")
			time.sleep(0.5)
			self.go_home()
		else:
			payment = int(payment_amount)
			return payment

	# this is what the app runs when the state is initialized i.e. when the user chooses to make a payment to their credit account
	def on_enter(self):

		payment_amount = self.get_payment_input()
		self.account.pay_credit(payment_amount)

		print("Payment successful!")
		print(f"Your credit balance is ${self.account.balance}")

		time.sleep(0.5)
		self.go_home()

# this is what the app runs when the user chooosed to exit the app
# i.e. when '8' is selected from the transaction menu or when 'Nn' is inputted when the user is asked if they want to make a transaction
class Exit(State):

	# this is what the app runs when the exit state is initialized i.e. when the user chooses to exit the app
	# prints a receipt :)
	def on_enter(self):
		print("----------------------------------------")
		print("Thank you for banking with us!")
		print("Printing receipt...")
		time.sleep(1)
		print("********************************")
		print("Transaction is now complete.")
		print("Transaction number: " + str(random.randint(100000, 1000000)))
		print(f"Account holder: {self.account.account_holder}")
		print(f"Account number: {self.account.account_number}")
		print(f"Account balance: ${self.account.balance}")
		print("Thank you for choosing FinTech as your bank!")
		print("********************************")
		time.sleep(2)
		exit(0)

# this is what the State class feeds in and out of 
# each state is an instance of the State class
class App:
	states = {
		000: CreateAccount,
		1: AccountDetail,
		2: CheckBalance,
		3: Deposit,
		4: DebitWithdraw,
		5: MakePurchase,
		6: CreditWithdraw,
		7: PayCredit,
		8: Exit,
		99: Home
	}

	# all methods below are used to initialize each next state in the
	# in other words, allows the user to 'naviate' through the app

	state: State = None # type: ignore
	account = None

	def go_home(self):
		self.set_state(99)

	def run_state(self, state):
		state(self.set_state, self.set_account, self.account, self.go_home)

	def set_state(self, state: int):
		if self.state:
			self.state.on_exit(self) # type: ignore

		self.state = self.states[state]
		self.run_state(self.state)

	def set_account(self, account: Account):
		self.account = account

	def __init__(self) -> None:
		self.set_state(000)

# this calls the program to run
app = App()
