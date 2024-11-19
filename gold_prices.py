import os
import sqlite3 
import requests
from bs4 import BeautifulSoup

#city = 'https://www.goodreturns.in/gold-rates/chandigarh.html'
gold = 'https://groww.in/gold-rates'
#response = requests.get(city)

response = requests.get(gold)
#print(response.status_code)
source_code = response.text
doc = BeautifulSoup(source_code, 'html.parser')
rows_tbi = []
#print(type(doc))
#print(doc.prettify()) #data_file

tables = doc.find_all('table', {'class': 'tb10Table'})

gold_table = None

# find table '24K PURE GOLD' in the header
for table in tables:
    header = table.find('thead')
    if header:
        header_text = header.get_text()
        if '24K PURE GOLD' in header_text:
            gold_table = table
            break

if gold_table:
    rows = gold_table.find_all('tr')

    # last week's prices of 22k gold
    print("24k Gold Prices in Delhi for the Last Week:")
    for row in rows[1:14]:  
        cols = row.find_all('td')
        if len(cols) >= 3:
            date_str = cols[0].text.strip()
            price_24k = cols[2].find('div').text.strip()
            price_22k = cols[1].find('div').text.strip()
            print(f"Date: {date_str}, 24k Gold Price: {price_24k}")
            print(f"Date: {date_str}, 22k Gold Price: {price_22k}")
            rows_tbi.append((date_str, '24k', price_24k))
            rows_tbi.append((date_str, '22k', price_22k))
else:
    print("Gold price table not found.")
    
# Inserting data into database
if os.path.exists('gold_prices.db'):
    os.remove('gold_prices.db')

conn = sqlite3.connect('gold_prices.db') 

#Creating a cursor object in sqlite (badically an instance of the database)
cursor = conn.cursor()   

table = '''CREATE TABLE IF NOT EXISTS Gold_prices_for_last_week (
    "Date" VARCHAR(255),
    "karat" VARCHAR(255),
    "Price" VARCHAR(255)
);'''

conn.execute(table)
conn.commit()

for date, karat, price in rows_tbi:
    cursor.execute(
            '''INSERT INTO Gold_prices_for_last_week VALUES (?, ?, ?)''', (date, karat, price))
    conn.commit()
conn.close()
