# recursion of pow(x, n)

def power(x, n):
	if n == 0:
		return 1
	else:
		return power(x, n-1) * x


print(power(3, 4))
