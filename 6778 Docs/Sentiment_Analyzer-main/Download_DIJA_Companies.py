import requests
from bs4 import BeautifulSoup

#url = 'https://markets.businessinsider.com/index/components/dow_jones'

url = 'https://www.cnbc.com/dow-30/'
response = requests.get(url)
#print(response.status_code)
companies = []

soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find('table', class_ = 'table')
#print(table)

for data in table.find_all('tbody', class_ = 'table__tbody'):
 rows = data.find_all('tr')
 #print(rows)

for row in rows:
   name = row.find_all('Name')[0].text.strip()
   companies.append(name)

print(companies)

