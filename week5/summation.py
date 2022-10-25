# A recursive function that returns the sum of first n numbers

def summation(seq, n):
	if n == 0:
		return 0
	else:
		return summation(seq, n-1) + seq[n-1]


# Driver Code:
seq = [2, 4, 5, 8, 10, 12]
print(summation(seq, 4))
