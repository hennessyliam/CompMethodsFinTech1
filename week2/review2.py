from week1.hennessy_liam_1 import has_odd_pair
import math

my_data = [1, 4, 6, 8]

if not has_odd_pair(my_data):
	print("My data has a pair of odd numbers")
else:
	print("No pair!")


##
# above we imported the math library, and below we are calling it and some functions

print(math.pi)				# calls the value of pi
print(math.sqrt(9))			# sqrt 9 as a float
print(math.sqrt(8))
print(math.log(16, 2))		# log 16 base 2
print(int(math.log(16, 2)))	# log 16 base 2 as an int
print(math.log10(100))
print(math.factorial(5))


# write a function that calculates factorial with a given number n
# without using the built-in function:

# profs solution:

def my_factorial(n):

	fact_result = 1
	for items in range(1, n+1):
		fact_result = fact_result * items
	return fact_result

#driver code:
# my_factorial(5)
n = 5
print('Factorial of', n, 'is', my_factorial(5))


# my solution using a while loop:
def my_factorial2(n):
	fact_result = 1
	while n > 1:
		fact_result = fact_result * n
		n = n - 1
	return fact_result

print('Factorial using while-loop: ', my_factorial2(5))

# driver code:
# my_factorial2(5)
n = 5
print('Factorial of', n, 'is', my_factorial2(n))


# create a list of even numbers using range(), from 0 to 10
even_numbers = []
for i in range(0, 10, 2):		# range(end, start, stepSize)
	even_numbers.append(i)		# adds numbers to the list
print(even_numbers)

# LISTS:
my_list = [3, 4, 6, 76, 23, 45, 65]
print(my_list[:3])
print(my_list[3:])
print(my_list[3:5])
my_list[0] = 4
print(my_list)


# STRINGS;
word = 'FinTech'
# indexing/slicing
print(word[:3])
print(word[3:])
print(word[3:5])
print(word[0])

# word[0] = "T" 	# 'str' object does not support assignment (i)


# SETS
my_set = {2, 3, 3, 4, 5}
print(my_set)
print(type(my_set))

# note that this creates an empty dict:
temp = {}
print(type(temp))

# test this? ==> prints <class 'dict'>
temp2 = ()
print(type(temp))

# converting an empty dictionary to an empty set:
temp3 = set(temp)
print(temp3)
print(type(temp3))

# the elements in the set cannot be duplicates
# the elements in the set are immutable (cannot be modified) but the set as a whole is mutable
# there is no index attached to any element in the python set. So they do not support nay indexing/slicing operation
# accessing values in a set:
days = set(['Mon', 'Tues', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
for d in days:
	print(d)		# returns elements in a different order on each execution. why?


# Exercise:
# 1 to n, for n = 5
# {1: 1, 2:4, 3:9, 4:16, 5:25}
# write a function that creates this dictionary above

def squares_matching(n):
	my_dict = {}
	for numbers in range(1, n+1):
		my_dict[numbers] = pow(numbers, 2)
	return my_dict

# Driver Code:
print(squares_matching(5))

# comprehension dictionary syntax:
def squares_match2(n):
	return {x: x**2 for x in range(1, n+1)}

# Driver Code:
print(squares_match2(5))
