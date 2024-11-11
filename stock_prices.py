import requests
from bs4 import BeautifulSoup
import sqlite3 
import os

prices = 'https://www.equitypandit.com/historical-data/ADANIENT'


response = requests.get(prices)
#print(response.status_code)
source_code = response.text
doc = BeautifulSoup(source_code, 'html.parser')
#print(doc.prettify()) #data_file

rows_tbi = []
tables = doc.find_all('tbody')
#print(tables[1])
rows = doc.find_all('tr')
#print(rows[2])
for row in rows[1:]:
    cols = row.find_all('td')
    if len(cols) >= 3:
        date = cols[0].text.strip()
        Closing_price = cols[1].text.strip()
        Opening_price = cols[2].text.strip()
        change = cols[6].text.strip()
        vol = cols[5].text.strip()
        high = cols[3].text.strip()
        low = cols[4].text.strip()
        print(f"Date: {date}, Closing Price: {Closing_price}, Opening Price: {Opening_price}, Percentage Change: {change}, volume: {vol}, High: {high}, Low: {low}")
        rows_tbi.append((date, Closing_price, Opening_price, change, vol, high, low))
    else:
        print("Price table not found.")
#print(rows_tbi)

if os.path.exists('stock_prices.db'):
    os.remove('stock_prices.db')

conn = sqlite3.connect('stock_prices.db') 

#Creating a cursor object in sqlite (badically an instance of the database)
cursor = conn.cursor()   

table = '''CREATE TABLE IF NOT EXISTS STOCK_PRICE_OF_LAST_5_YEARS (
    "Date" VARCHAR(255),
    "Closing_Price" VARCHAR(255),
    "Opening_Price" VARCHAR(255),
    "Percentage_Change" VARCHAR(255),
    "Volume" VARCHAR(255),
    "High" VARCHAR(255),
    "Low" VARCHAR(255)
);'''
conn.execute(table)
conn.commit()

for date, Closing_price, Opening_price, change, vol, high, low in rows_tbi:
    cursor.execute(
            '''INSERT INTO STOCK_PRICE_OF_LAST_5_YEARS VALUES (?, ?, ?, ?, ?, ?, ?)''', (date, Closing_price, Opening_price, change, vol, high, low))
    conn.commit()
   
conn.close()
