

# range() -> range(start,end,stepSize) 	==> loop through from start to (end-1) incremented by stepSize
# range(start,end=n-1) 					==> loop through data from start to (end-1) incremented by 1
# range(end) 							==> loop through data from 0 to (end-1) incremented by 1

def has_odd_pair(data):
	# counter for odd numbers
	count = 0

	for j in range(len(data)):		# j = 0, 1, 2, n-1
		# condition to be odd for a number
		if data[j] % 2 == 1:
			count += 1
			# condition to be odd for a multiplication
			if count == 2:
				return True
	return False

# driver code
# example_data1 = [2, 4, 5, 6]
# print(has_odd_pair(example_data1))

example_data2 = [2, 4, 5, 7]
print(has_odd_pair(example_data2))
