# Liam Hennessy
# li621332
# 09/04/2022
# A script that determines if a specific set of numbers in a sequence has an odd product

# This works on the premise that you need two multiply two odd numbers to get an odd product

def has_odd_pair(data): 		# function takes an int list[data] & checks each int to see if there are two odd values
	for first_item in data: 		# for loop loops through each value in a sequence
		is_even = first_item % 2 == 0		# determining an if value is even
		if is_even:						# if statement says what to do if value is even
			continue			# pushes on to the next value in the data set and back to the beginning of the loop

		for second_item in data:		# if a first odd value is found, this checks if there is another odd value
			if first_item != second_item:	 # this makes sure the two values are not the same
				return True					# returns True if there are two values that are odd
	return False					# returns false if there are not two odd values


# driver code
data = [4, 8 ,7, 9]

print(has_odd_pair(data))
if has_odd_pair(data) == False:  # cute if statement informing the user about the outcome
	print('There is no set of numbers in this data set whose product is odd.')
else:
	print('There is a set of numbers in this data set whose product is odd.')





