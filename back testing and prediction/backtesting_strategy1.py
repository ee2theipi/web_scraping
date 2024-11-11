import pandas as pd
import sqlite3
import backtrader as bt

# Converting the data from the database to a pandas dataframe
conn = sqlite3.connect('stock_prices.db')
query = "SELECT Date, Closing_price, Opening_price, Percentage_Change, Volume, High, Low FROM STOCK_PRICE_OF_LAST_5_YEARS"
price_df = pd.read_sql(query, conn)

# 'Date' --> datetime format
price_df['Date'] = pd.to_datetime(price_df['Date'])

# Removing any non-numeric characters and convertnig columns to numeric types
price_df['Closing_Price'] = price_df['Closing_Price'].replace('[\$,]', '', regex=True).astype(float)
price_df['Opening_Price'] = price_df['Opening_Price'].replace('[\$,]', '', regex=True).astype(float)
price_df['Percentage_Change'] = price_df['Percentage_Change'].replace('[\%,]', '', regex=True).astype(float)
price_df['Volume'] = price_df['Volume'].replace('[\$,]', '', regex=True).astype(float)
price_df['High'] = price_df['High'].replace('[\$,]', '', regex=True).astype(float)
price_df['Low'] = price_df['Low'].replace('[\$,]', '', regex=True).astype(float)

price_df = price_df.sort_values(by='Date')

# Check the DataFrame to ensure the conversion was successful
#print(price_df.dtypes)
#print(price_df.head())


class MovingAverageStrategy(bt.Strategy):
    params = (('short_period', 10),('long_period', 50),)

    def __init__(self):
        self.short_ma = bt.indicators.SimpleMovingAverage(self.data.close, period=self.params.short_period)
        self.long_ma = bt.indicators.SimpleMovingAverage(self.data.close, period=self.params.long_period)
        self.crossover = bt.indicators.CrossOver(self.short_ma, self.long_ma)

    def next(self):
        # Buy if short MA crosses above long MA
        if self.crossover > 0 and not self.position:
            self.buy()
        # Sell if short MA crosses below long MA
        elif self.crossover < 0 and self.position:
            self.sell()


# Parsing the data to backtrader
price_df_parsed = bt.feeds.PandasData(dataname=price_df, datetime=0, open=2, high=5, low=6, close=1, volume=4, openinterest=None)

cerebro = bt.Cerebro()
cerebro.addstrategy(MovingAverageStrategy)
cerebro.adddata(price_df_parsed)

cerebro.broker.setcash(10000.0)
cerebro.broker.setcommission(commission=0.001)

print("Starting Portfolio Value:", cerebro.broker.getvalue())
cerebro.run()
print("Ending Portfolio Value:", cerebro.broker.getvalue())
cerebro.plot()
