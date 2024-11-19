import sqlite3

conn = sqlite3.connect('news.db')
cursor = conn.cursor()

cursor.execute("SELECT COUNT(DISTINCT Published_on) FROM News")
unique_dates_count = cursor.fetchone()[0]

print("Number of unique dates in news.db:", unique_dates_count)
conn.close()
