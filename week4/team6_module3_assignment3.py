# Team 6 - Liam Hennessy, Anna Zheng
# PID: Liam - 5499630, Anna - 4397893
# Submission Date: Sep 25, 2022
# A script to determine if there is a missing integer in a sequence of numbers

# Solution Method 1:

def find_missing(sequence):		# defining a function
	missing = []				# creating an empty list
	for item in range(sequence[0], sequence[-1] + 1):		# loop through the items in range
		if item not in sequence:			# determines if number is not in the sequence
			missing.append(item)			# if value is missing, this appends it to this list
		else:
			continue						# if no missing value, continue through the sequence
	return missing							# return the list of missing numbers


# Solution Method 2:
# this function emulates what happens in method 1 in one line of code 
def find_missing2(sequence):
	return [item for item in range(sequence[0], sequence[-1] + 1) if item not in sequence]


def find_missing3(seq):
	sum = len(seq) * (len(seq) + 1) / 2
	total = 0
	for i in seq:
		total += i
	return sum - total


# Driver Code:

S = [0, 1, 2, 3, 5, 6, 7, 9, 12]

print(find_missing(S))
print(find_missing2(S))
print(find_missing3(S))
print(f'The values missing from the sequence are {find_missing(S)}')



