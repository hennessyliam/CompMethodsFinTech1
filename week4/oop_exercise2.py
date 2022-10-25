# OOP Example - week4

class Vehicle:
	def __init__(self, name, mileage, capacity):  # constructor
		self.name = name
		self.mileage = mileage
		self.capacity = capacity

	def fare(self):
		return self.capacity * 100


class Bus(Vehicle):
	def fare(self):
		amount = super().fare()
		amount += amount * 10 / 100
		return amount


print("--EXERCISE 1--")

# Driver Code:
school_bus = Bus("School Volvo", 150, 40)
print(school_bus.fare())


# Exercise-2
class Staff:
	def __init__(self, role, dept, salary):
		self.role = role
		self.dept = dept
		self.salary = salary

	def show_info(self):
		print("Name:", self.name)
		print("Age:", self.age)
		print("Role:", self.role)
		print("Department:", self.dept)
		print("Salary:", self.salary)


class Analyst(Staff):
	def __init__(self, name, age):
		self.name = name
		self.age = age
		super().__init__("Analyst", "Finance", 100000)


print("--EXERCISE 2--")
# Driver Code:
analyst1 = Analyst("Lisa", 29)
print(analyst1.show_info())
