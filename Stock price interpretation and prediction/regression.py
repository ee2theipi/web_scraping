import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression


data = pd.read_csv('stock_prices.csv')
print(data.head())
data['Date'] = pd.to_datetime(data['Date'])

data = data.sort_values('Date')

# Prepare feature matrix X and target vector y
X = (data['Date'] - data['Date'].min()).dt.days.values.reshape(-1, 1)
y = data['Closing_Price'].values

# Fit the linear regression model
model = LinearRegression()
model.fit(X, y)

y_p = model.predict(X)

# Calculate the residuals
residuals = y - y_p
std_dev = np.std(residuals)

#standard deviation bounds
y_p_upper_1 = y_p + std_dev
y_p_lower_1 = y_p - std_dev
y_p_upper_1_5 = y_p + 1.5 * std_dev
y_p_lower_1_5 = y_p - 1.5 * std_dev

plt.figure(figsize=(10, 6))
plt.plot(data['Date'], y, label='Closing Price', color='blue')
plt.plot(data['Date'], y_p, label='Regression Line', color='red', linestyle='--')
plt.plot(data['Date'], y_p_upper_1, label='+1 Std Dev', color='green', linestyle=':')
plt.plot(data['Date'], y_p_lower_1, color='green', linestyle=':')
plt.plot(data['Date'], y_p_upper_1_5, label='+1.5 Std Dev', color='orange', linestyle='-.')
plt.plot(data['Date'], y_p_lower_1_5, color='orange', linestyle='-.')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.title('Closing Price with Regression Line and ±1 and ±1.5 Std Dev')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
