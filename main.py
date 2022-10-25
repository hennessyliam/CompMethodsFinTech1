countdown = 10

while countdown >= 0:
	print(countdown)
	countdown += - 1
print('We have liftoff!')

##

ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

for age in ages:
	if age < 21:
		continue
	else:
		print(age)


##

# Write your over_budget function here:

def over_budget(budget, food_bill, electricity_bill, internet_bill, rent):
	if budget < (food_bill + electricity_bill + internet_bill + rent):
		return True
	else:
		return False


# Uncomment these function calls to test your over_budget function:
print(over_budget(100, 20, 30, 10, 40))
# should print False
print(over_budget(80, 20, 30, 10, 30))


# should print True

##

# Create your class here

class Turtle:
	def __init__(self, input_name, input_breed, input_age=0):
		self.name = input_name
		self.age = input_breed
		self.size = input_age
		self.slow = True


new_turtle = Turtle("Leo", 200, "Large")
print(new_turtle)
print(new_turtle.age)


##


class Cat:
	def __init__(self, input_name, input_breed, input_age=0):
		self.name = input_name
		self.breed = input_breed
		self.age = input_age
		self.is_cuddly = True

	def show(self):
		print("The Cats name is {name}, breed is {breed} and age is {age}".format(name=self.name, breed=self.breed, age=self.age))


new_cat = Cat("Leo", "Tabby", 3)
my_cat = Cat("James", "Tiger", 45)

new_cat.show()
my_cat.show()
print(new_cat.age)
