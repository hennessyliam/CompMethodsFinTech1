from time import time, sleep
# in order to calculate execution time, measuring the time taken between lines of code
import matplotlib.pyplot as plt

start_time = time()


def fact(number):
	product = 1
	for i in range(number):		# range(number) from 0 to (n-1)
		product = product * (i+1)
	return product

# sleep(1)
# Driver Code:
print(fact(6))
end_time = time()

elapsed_time = end_time - start_time
print(elapsed_time)


# Constant Complexity:
def constant_alg(items):
	result = items[0] * items[0]
	print(result)


# Driver Code:
items1 = [2, 4, 5, 6]
constant_alg(items1)
# constant_alg() method runs in O(1) time



def constant(n):
	return 1

steps = []
for i in range(1, 100):
	steps.append(constant(i))

plt.plot(steps)
# plt.show()


# Logarithmic Complexity
def binary_search_iterative(array, element):

	mid = 0
	start = 0
	end = len(array)
	step = 0

	while start <= end:
		print("Subarray in step {}: {}".format(step, str(array[start:end+1])))
		step += 1
		mid = (start+end) // 2
		if element == array[mid]:
			return element
		if element < array[mid]:
			end = mid - 1
		else:
			start = mid + 1


# Driver Code:
sequence1 = [1, 2, 5, 7, 13, 15, 16, 18, 24, 28, 29]
print(binary_search_iterative(sequence1, 18))


# Linear Complexity O(n):

def sum1(array):
	total = 0
	for i in range(len(array)):
		total = total + array[i]
	return total


# Driver Code:
sequence2 = [1, 2, 5, 7, 13]
print(sum1(sequence2))

def linear_alg(n):
	return n

steps = []
for i in range(1, 100):
	steps.append(linear_alg(i))

plt.plot(steps)
# plt.show()


# Quadratic
