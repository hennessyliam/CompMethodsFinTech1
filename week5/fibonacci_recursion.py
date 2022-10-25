

def fib(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	else:
		return fib(n-1) + fib(n-2)


# Driver Code:
n = 90
print("The fibonacci numbers for", n, "elements: ")
for i in range(0, n):
	print(fib(i))

