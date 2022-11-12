import pandas as pd
import time

# PART 1:
# pull in the data
pulling_data = pd.read_html("https://www.ssa.gov/oact/STATS/table4c6.html")
df = pulling_data[0]
df.drop([120], inplace=True)

# convert columns from objects to numbers
df['Exact age'] = df['Exact age'].astype(int)
df['Male'] = df['Male'].astype(float)
df['Female'] = df['Female'].astype(float)

df_male = df["Male", "Life expectancy"]
df_female = df["Female", "Life  expectancy"]

male_life_expectancy = df_male.to_dict()
female_life_expectancy = df_female.to_dict()

# print(male_life_expectancy)
# print(female_life_expectancy)

# PART 2:
# start of program
print("Hello and thank you for using our Robo-advisor!")
time.sleep(.5)
print("To get started, we're going to need some personal information.")


# PART 3
# exception handling

# Exception check first name
def get_first_name(name):
	# makes sure the name is an allowable character limit
	if not name.isspace():
		while len(name) > 20:
			name = input("You have reached the character limit. \nPlease enter your first name: ")

		# makes sure the name is an allowable character limit
		while len(name) == 0:
			name = input("Please enter your first name: ")

		# outlines all forbidden characters
		forbidden_characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '`', '~', '!', '@', '#', '$', '%',
								'^', '&', '*', '(', ')', '_', '=', '+', '[', '{', ']', '}', '\\', '|', ';', ':',
								'"', ',', '<', '.', '>', '/', '?']
		# checks each element of the name against the forbidden characters
		for character in name:
			if character in forbidden_characters:
				name = input(
					"Please refrain from entering numbers or special characters.\nPlease enter your first name: ")
				return get_first_name(name)
	# makes the input uniform and removes any spaces
	return name.upper().replace(" ", "")


# Exception check last name
def get_last_name(name):
	# makes sure the name is an allowable character limit
	if not name.isspace():
		while len(name) > 20:
			name = input("You have reached the character limit. \nPlease enter your last name: ")

		# makes sure the name is an allowable character limit
		while len(name) == 0:
			name = input("Please enter your last name: ")

		# outlines all forbidden characters
		forbidden_characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '`', '~', '!', '@', '#', '$', '%',
								'^', '&', '*', '(', ')', '_', '=', '+', '[', '{', ']', '}', '\\', '|', ';', ':',
								'"', ',', '<', '.', '>', '/', '?']
		# checks each element of the name against the forbidden characters
		for character in name:
			if character in forbidden_characters:
				name = input(
					"Please refrain from entering numbers or special characters.\nPlease enter your last name: ")
				return get_last_name(name)
	# makes the input uniform and removes any spaces
	return name.upper().replace(" ", "")


# Exception check age
def get_age(age):
	if not age.isspace():
		while len(age) == 0:  # type: ignore
			age = int(input("Please enter your age: "))

		forbidden_characters = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h',
								'I', 'i', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p',
								'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x',
								'Y', 'y', 'Z', 'z', '`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
								'_', '=', '+', '[', '{', ']', '}', '\\', '|', ';', ':', '"', ',', '<', '.', '>', '/',
								'?']

		for number in age:  # type: ignore
			if number in forbidden_characters:
				age = int(input("Please refrain from entering letters or special characters.\nPlease enter your age: "))
				return get_age(age)

		if age > 119:
			age = int(input(
				"You're blessed to live a long life! There's no need to continue. \nIf you would like to continue, "
				"please enter an age less than or equal to 119: "))
			return get_age(age)
	return age.replace(" ", "")  # type: ignore


# Exception check gender
def get_gender(gender):
	if not gender.isspace():
		while len(gender) != 1:
			gender = input("""Please enter your gender with "m" for male or "f" for female: """)

		# outlines all forbidden characters
		forbidden_characters = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'G', 'g', 'H', 'h',
								'I', 'i', 'J', 'j', 'K', 'k', 'L', 'l', 'N', 'n', 'O', 'o', 'P', 'p',
								'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x',
								'Y', 'y', 'Z', 'z', '`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_',
								'=', '+', '[', '{', ']', '}', '\\', '|', ';', ':', '"', ',', '<', '.', '>', '/', '?',
								'0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
		# checks each element of the name against the forbidden characters
		for character in gender:
			if character in forbidden_characters:
				name = input("""Please enter your gender with "m" for male or "f" for female: """)
				return get_gender(gender)
	# makes the input uniform and removes any spaces
	return gender.replace(" ", "")


# Exception check retirement age
def get_retirement_age(retirement_age):
	if not retirement_age.isspace():
		while len(retirement_age) == 0:  # type: ignore
			retirement_age = int(input("Please enter your desired retirement age: "))

		forbidden_characters = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h',
								'I', 'i', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p',
								'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x',
								'Y', 'y', 'Z', 'z', '`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
								'_', '=', '+', '[', '{', ']', '}', '\\', '|', ';', ':', '"', ',', '<', '.', '>', '/',
								'?']

		for number in retirement_age:  # type: ignore
			if number in forbidden_characters:
				retirement_age = int(input("Please refrain from entering letters or special characters.\nPlease enter your desired retirement age: "))
				return get_retirement_age(retirement_age)


# potentially need something here in case retirement age is too high


# Part 4:
# Investor Inputs
first_name = input("Please enter your first name: ")
# Updates first name to corrected name
correct_first_name = first_name.replace(first_name, f"{get_first_name(first_name)}")
print(correct_first_name)

last_name = input("Please enter your last name: ")
# Updates first name to corrected name
correct_last_name = last_name.replace(last_name, f"{get_last_name(last_name)}")
print(correct_last_name)
print(correct_first_name, correct_last_name)

self_age = int(input("How old are you (rounded to the nearest whole year): "))
# correct_self_age = self_age.replace[self_age, f"{get_age(self_age)}"]              #need to check
# print(correct_self_age)

self_gender = input("""What is your gender (enter "m" for male or "f" for female): """)
correct_self_gender = self_gender.replace(self_gender, f"{get_gender(self_gender)}")
print(correct_self_gender)

self_retirement_age = input("Please enter your desired retirement age: ")
correct_self_retirement_age = self_retirement_age.replace(self_retirement_age, f"{get_retirement_age(self_retirement_age)}")
print(correct_self_retirement_age)


# self_gender = input("""What is your gender (enter "m" for male or "f" for female): """)
# self_age = int(input("How old are you (rounded to the nearest whole year): "))

# Part 5:
# Calculations
def life_expectancy(gender, age):
	if gender == "m":
		return male_life_expectancy[age] + age
	if gender == "f":
		return female_life_expectancy[age] + age


# Using Schwab Estimates:
# https://www.schwab.wallst.com/Prospect/Research/mutualfunds/overview/solutions.asp?type=targetFunds

years_to_retirement = self_retirement_age - self_age  # type: ignore

def stock_allocation(years_to_retirement):
	if years_to_retirement >= 34:
		return 100
	if 34 > years_to_retirement >= 30:
		return 91
	if 30 > years_to_retirement >= 25:
		return 84
	if 25 > years_to_retirement >= 20:
		return 78
	if 20 > years_to_retirement >= 15:
		return 71
	if 15 > years_to_retirement >= 10:
		return 64
	if 10 > years_to_retirement >= 5:
		return 51
	if 5 > years_to_retirement >= 0:
		return 43
	if 0 > years_to_retirement >= -5:
		return 38
	if -5 > years_to_retirement >= -10:
		return 35
	if -10 > years_to_retirement >= -15:
		return 30
	if -15 > years_to_retirement >= -20:
		return 26
	if years_to_retirement < -25:
		return 25


def bond_allocation(years_to_retirement):
	if years_to_retirement >= 34:
		return 0
	if 34 > years_to_retirement >= 30:
		return 8
	if 30 > years_to_retirement >= 25:
		return 15
	if 25 > years_to_retirement >= 20:
		return 21
	if 20 > years_to_retirement >= 15:
		return 27
	if 15 > years_to_retirement >= 10:
		return 32
	if 10 > years_to_retirement >= 5:
		return 44
	if 5 > years_to_retirement >= 0:
		return 52
	if 0 > years_to_retirement >= -5:
		return 57
	if -5 > years_to_retirement >= -10:
		return 60
	if -10 > years_to_retirement >= -15:
		return 65
	if -15 > years_to_retirement >= -20:
		return 69
	if years_to_retirement < -20:
		return 70

def cash_allocation(years_to_retirement):
	if years_to_retirement >= 34:
		return 0
	if 34 > years_to_retirement >= 30:
		return 1
	if 30 > years_to_retirement >= 25:
		return 1
	if 25 > years_to_retirement >= 20:
		return 1
	if 20 > years_to_retirement >= 15:
		return 2
	if 15 > years_to_retirement >= 10:
		return 4
	if 10 > years_to_retirement >= 5:
		return 5
	if 5 > years_to_retirement >= 0:
		return 5
	if years_to_retirement < 0:
		return 5


# Results
print('Hi,', first_name, last_name)
print('Based on your life expectancy of', life_expectancy(self_gender, self_age))
print('We suggest you invest ', stock_allocation(self_age), '% in stocks and', bond_allocation(self_age), '% in bonds.')
