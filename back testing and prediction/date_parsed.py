import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect('stock_prices.db')

# Load the data from the database
query = "SELECT * FROM STOCK_PRICE_OF_LAST_5_YEARS"
df = pd.read_sql(query, conn)

# Convert 'Date' to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Remove the time component from the 'Date' column
df['Date'] = df['Date'].dt.date

# Save the updated data back to the database
df.to_sql('STOCK_PRICE_OF_LAST_5_YEARS', conn, if_exists='replace', index=False)

# Close the database connection
conn.close()
