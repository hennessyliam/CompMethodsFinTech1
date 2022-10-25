# 1
def function1(k):
	return k & 1 == 0


k = 2
print(function1(k))

# 2
j = 4
# total = sum(j*j for j in range(1, n + 1, 2))

# print(total)

# 3

data = ["GOOGLE", 123.2, "AMAZON", 457.6, "TESLA", 867.3]
print(data)
data.pop()
print(data)
data.remove(123.2)
print(data)
del data[1]
print(data)
data.append("META")
print(data)

# 4
data2 = {x: x ** 2 for x in range(1, 6)}
print(data2)


# 5
class Stock:
	def __init__(self, name, price):
		self.name = name
		self.price = price


Goog = Stock("Google", 312)

print(Goog.price)

# 6
class Dog:
    def walk(self):
        return "*walking*"

    def speak(self):
        return "Woof!"


class JackRussellTerrier(Dog):
    def speak(self):
        return "Arff!"

    def talk(self):
        return super().speak()


bobo = JackRussellTerrier()
print(bobo.speak())
print(bobo.walk())
print(bobo.talk())


# 11
def matrix(n):

    if n == 1:
        print('1')
    else:
        for i in range(1, n):
            print(i, end=' ')
        print()
        matrix(n-1)


print("---Q11---")
print(matrix(5))
