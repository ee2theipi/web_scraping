import sqlite3
import pandas as pd

conn = sqlite3.connect('stock_prices.db')
query = "SELECT * FROM STOCK_PRICE_OF_LAST_5_YEARS"
df = pd.read_sql(query, conn)

df['Date'] = pd.to_datetime(df['Date'])

last_month = df['Date'].max() - pd.DateOffset(months=1)
recent_df = df[df['Date'] >= last_month]

new_conn = sqlite3.connect('last_1_month.db')

recent_df.to_sql('STOCK_PRICE_OF_LAST_MONTH', new_conn, if_exists='replace', index=False)

conn.close()
new_conn.close()