# C 1.15
# “Write a Python function that takes a sequence of numbers and determines if all the numbers are different
# from each other (that is, they are distinct).”

# A function that determines if all numbers in a sequence are distinct from each other

def distinct(data):
	for first_value in range(len(data)):
		for second_value in range(len(data)):
			if first_value == second_value:
				continue
			if data[first_value] == data[second_value]:
				return False
	return True

# Driver Code:
list1 = [1, 3, 4, 5]
list2 = [2, 6, 6, 7]

print(distinct(list1))
print(distinct(list2))


# C 1.22
# Write a short Python program that takes two arrays a and b of length n
# (assuming we are giving 2 arrays that both have length n) storing int values, and returns the dot product of a and b.
# That is, it returns an array c of length n such that c[i] = a[i] . b[i], for i = 0,...,n-1.

# A function that multiplies the elements of two arrays and produces a list with the products, in sequential order

def dot_product(a, b):
	prod_list = []
	for item in range(len(a)):
		prod = a[item] * b[item]
		prod_list.append(prod)
	return prod_list

# Driver Code:
print(dot_product(list1, list2))


# C 1.28
# Give an implementation of a function named norm such that norm(v, p) returns the p-norm value of v and norm(v)
# returns the Euclidean norm of v. You may assume that v is a list of numbers

# A function that returns the Euclidean norm of a vector

def norm(v, p=2):
	sum = 0
	for item in v:
		sum += item ** p
	return sum ** (1/p)

# Driver Code:

vector1 = (3, 4)
print(norm(vector1))
vector2 = (5, 12)
print(norm(vector2))
