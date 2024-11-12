import sqlite3
from textblob import TextBlob


conn = sqlite3.connect('news.db')
cursor = conn.cursor()

cursor.execute("PRAGMA table_info(News)")
columns = [column[1] for column in cursor.fetchall()]
if 'sentiment' not in columns:
    cursor.execute("ALTER TABLE News ADD COLUMN sentiment REAL")
    conn.commit()

def add_sentiment_score(title):
    sentiment_score = TextBlob(title).sentiment.polarity
    cursor.execute("UPDATE News SET sentiment = ? WHERE Title = ?", (sentiment_score, title))
    conn.commit()

cursor.execute("SELECT * FROM News")
rows = cursor.fetchall()
for row in rows:
    add_sentiment_score(row[1])

conn.close()