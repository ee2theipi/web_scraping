# api_key = eccf434a292f43bdb3d37f7d0d131a96

import requests
import sqlite3
import os

# NewsAPI used as endpoint  
url = ('https://newsapi.org/v2/everything?'
       'q=adani&'
       'from=2024-11-01&'
       'sortBy=popularity&'
       'apiKey=eccf434a292f43bdb3d37f7d0d131a96')

# A GET request to the API
response = requests.get(url)
rows_tbi = []
#print(response.json())
data = response.json()
print(f"Total news articles with the desired keyword: {data['totalResults']}")
for article in data['articles']:
    #print(article['title'], article['publishedAt'])
    rows_tbi.append((article['publishedAt'], article['title'], article['description'], article['url']))
  
  
# Creating a database to store the news articles
  
if os.path.exists('news.db'):
    os.remove('news.db')

conn = sqlite3.connect('news.db') 

#Creating a cursor object in sqlite (badically an instance of the database)
cursor = conn.cursor()   

table = '''CREATE TABLE IF NOT EXISTS News (
    "Published on" VARCHAR(255),
    "Title" VARCHAR(255),
    "About" VARCHAR(255),
    "url" VARCHAR(255)
);'''
conn.execute(table)
conn.commit()

for _, _, _, _ in rows_tbi:
    cursor.execute(
            '''INSERT INTO News VALUES (?, ?, ?, ?)''', (_, _, _, _))
    conn.commit()
conn.close()
