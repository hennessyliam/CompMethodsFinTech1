import csv

djia = csv.reader(open('/Users/hennessyliam/CompMethodsFinTech1/6778 Docs/DJIA.csv', 'r'))

companies = []

for row in djia:
    for company in row:
        companies.append(company)

print(companies)

