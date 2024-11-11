# in Date column remove the time and keep only the date

import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect('news.db')

# Load the data from the database
query = "SELECT * FROM News"
df = pd.read_sql(query, conn)

# Convert 'Date' to datetime format
df['Published_on'] = pd.to_datetime(df['Published_on'])

# Remove the time component from the 'Date' column
df['Published_on'] = df['Published_on'].dt.date

# Save the updated data back to the database
df.to_sql('News', conn, if_exists='replace', index=False)

# Close the database connection
conn.close()