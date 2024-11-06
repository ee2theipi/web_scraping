import sqlite3
import matplotlib.pyplot

conn = sqlite3.connect('gold_prices.db') 
cursor = conn.cursor() 

order_24k = [8,6,4,2,0,18,16,14,12,10]
order_22k = [9,7,5,3,1,19,17,15,13,11]
dates = []
x_values = []
x_values_24k = []
x_values_22k = []

cursor.execute('SELECT * FROM Gold_prices_for_last_week')
rows = cursor.fetchall()

for i in order_24k:
    price_str1 = rows[i][2].replace('₹', '').replace(',', '')
    x_values_24k.append(float(price_str1))
for i in order_22k:
    price_str2 = rows[i][2].replace('₹', '').replace(',', '')
    x_values_22k.append(float(price_str2))

for i in order_24k:
    dates.append(rows[i][0][0:2])
print(x_values_22k)
print(x_values_24k)
print(dates)

matplotlib.pyplot.plot(dates, x_values_22k, label='22k Gold Price')
matplotlib.pyplot.plot(dates, x_values_24k, label='24k Gold Price')
matplotlib.pyplot.legend()
matplotlib.pyplot.show()
conn.close()
