import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

#city = 'https://www.goodreturns.in/gold-rates/chandigarh.html'
gold = 'https://groww.in/gold-rates'
#response = requests.get(city)
#print(response.status_code)

response = requests.get(gold)
#print(response.status_code)
source_code = response.text
doc = BeautifulSoup(source_code, 'html.parser')
#print(type(doc))
#print(doc.prettify()) #data_file





tables = doc.find_all('table', {'class': 'tb10Table'})
#print(tables)

# Initialize gold_table to None
gold_table = None

# Iterate over the tables to find the one with '24K PURE GOLD' in the header
for table in tables:
    header = table.find('thead')
    if header:
        header_text = header.get_text()
        if '24K PURE GOLD' in header_text:
            gold_table = table
            break

# Check if the gold_table was found
if gold_table:
    # Extract the rows from the table
    rows = gold_table.find_all('tr')

    # Print the last week's prices of 24k gold
    print("24k Gold Prices in Delhi for the Last Week:")
    for row in rows[1:14]:  # Skip the header row and get the next 7 rows
        cols = row.find_all('td')
        if len(cols) >= 3:
            date_str = cols[0].text.strip()
            price_24k = cols[2].find('div').text.strip()
            print(f"Date: {date_str}, 24k Gold Price: {price_24k}")
else:
    print("Gold price table not found.")
