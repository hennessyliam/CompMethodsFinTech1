import csv
positive_words = []
negative_words = []


with open(r'filepath','r')as file:
   filecontent=csv.reader(file,delimiter=':')
   for row in filecontent:
      positive_words.append(row)

with open(r'filepath','r')as file:
   filecontent=csv.reader(file,delimiter=':')
   for row in filecontent:
      negative_words.append(row)

print(positive_words)
print(negative_words)


