#Chapter 1 Exercises

list1 = [1,2,3,4]
print(list1[0])
list1.append(5)
print(list1)
print("The number of elements is: " + str(len(list1)))
number1 = '123'
number2 = 5
print(int(number1)+number2)
list1.reverse()
print(list1)
list1.sort()
print(list1)
deleted_no = list1.pop()
print(deleted_no)
list1.insert(1,1.5)
print(list1)
list1.remove(1.5)
print(list1)

for items in list1:
    print(items)

#
# list1 = [1, 2, 3, 4]
even_list = []
odd_list = []
for item in list1:
    if item % 2 ==0:
        even_list.append(item)
    else:
        odd_list.append(item)
print(even_list)
print(odd_list)
