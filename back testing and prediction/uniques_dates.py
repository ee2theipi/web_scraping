import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('news.db')
cursor = conn.cursor()

# Count the number of unique dates in the 'Published_on' column
cursor.execute("SELECT COUNT(DISTINCT Published_on) FROM News")
unique_dates_count = cursor.fetchone()[0]

print("Number of unique dates in news.db:", unique_dates_count)

# Close the database connection
conn.close()