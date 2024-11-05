import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

prices = 'https://www.equitypandit.com/historical-data/ADANIENT'


response = requests.get(prices)
#print(response.status_code)
#print(response.status_code)
source_code = response.text
doc = BeautifulSoup(source_code, 'html.parser')
#print(doc.prettify()) #data_file

tables = doc.find_all('tbody')
#print(tables)

#print(tables[1])
rows = doc.find_all('tr')
print(rows[2])
for row in rows[1:]:
    cols = row.find_all('td')
    if len(cols) >= 3:
        date = cols[0].text.strip()
        Closing_price = cols[1].text.strip()
        Opening_price = cols[2].text.strip()
        change = cols[6].text.strip()
        print(f"Date: {date}, Closing Price: {Closing_price}, Opening Price: {Opening_price}, Percentage Change: {change}")
    else:
        print("Price table not found.")
