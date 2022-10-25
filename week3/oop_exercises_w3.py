# OOP exercises
# Creating a class and object

# Have an Employee class that takes name and salary
# Class, object,
import math


class Employee:
	# constructor to initialize the objecct
	def __init__(self, name, salary):
		# instance variables:
		self.name = name
		self.salary = salary

	# instance method
	def show(self):
		print("Employee name: {name}. Employee Salary: {salary}".format(name=self.name, salary=self.salary))


# can also use concatenation for sentence but this method reads easier


# Driver Code:
# Create and object of employee class
emp1 = Employee("Liam", 12000)
print(emp1.name, emp1.salary)
emp1.show()


# Exercise.2
# POLYMORPHISM:

class Circle:
	# class variable
	pi = math.pi

	def __init__(self, radius):
		self.radius = radius

	def calculate_area(self):
		return self.pi * pow(self.radius, 2)


class Rectangle:
	def __init__(self, length, width):
		self.length = length
		self.width = width

	def calculate_area(self):
		print("Area of rectangle is:", self.length * self.width)


# Driver Code:
rad = 5
circle1 = Circle(rad)
print("The area of the circle with radius", rad, "is", circle1.calculate_area())

rect = Rectangle(10, 5)
rect.calculate_area()


# INHERITANCE:

# base class:
class Vehicle:
	def __init__(self, name, color, price):
		self.name = name
		self.color = color
		self.price = price

	def info(self):
		print("The vehicle info:", self.name, self.color, self.price)


# Derived (child) class
class Car(Vehicle):
	def change_gear(self, num):
		print(self.name, "changes the gear to", num)

	# overrides the method in the class above
	def info(self):
		print("The car info is:", self.name, self.color, self.price)


# Child of Car class
class BodyType(Car):
	def __init__(self, name, color, price, body_type):
		super().__init__(name, color, price)
		self.body_type = body_type

	def info(self):
		print("The car info:", self.name, self.color, self.price, self.body_type)


# Driver Code:
car = Car("BMW M8", "Black", 100000)
car.info()

vehicle1 = Vehicle("MB C300", "Red", 50000)
vehicle1.info()

body_t = BodyType("BMW X5", "Blue", 60000, "SUV")
body_t.info()
