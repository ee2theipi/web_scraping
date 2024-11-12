import pandas as pd
import sqlite3
import backtrader as bt
import matplotlib.pyplot as plt

conn_stock = sqlite3.connect('last_1_month.db')
stock_df = pd.read_sql("SELECT * FROM STOCK_PRICE_OF_LAST_MONTH", conn_stock)

stock_df['Date'] = pd.to_datetime(stock_df['Date'])

numeric_cols = ['Opening_Price', 'High', 'Low', 'Closing_Price', 'Volume']
for col in numeric_cols:
    stock_df[col] = pd.to_numeric(stock_df[col], errors='coerce')

conn_news = sqlite3.connect('news.db')
news_df = pd.read_sql("SELECT * FROM News", conn_news)

news_df['Published_on'] = pd.to_datetime(news_df['Published_on'])

# taking maximum sentiment
daily_sentiment = news_df.groupby('Published_on')['sentiment'].max().reset_index()

merged_df = pd.merge(stock_df, daily_sentiment, left_on='Date', right_on='Published_on', how='left')

merged_df.drop(columns=['Published_on'], inplace=True)

merged_df['sentiment'] = merged_df['sentiment'].fillna(0)
#print(merged_df)
merged_df = merged_df.sort_values('Date')
merged_df.reset_index(drop=True, inplace=True)

print(merged_df)

class SentimentData(bt.feeds.PandasData):
    lines = ('sentiment',)
    params = (('sentiment', -1),)


class SentimentStrategy(bt.Strategy):
    params = dict(
        sentiment_threshold=0.1, 
    )

    def log(self, txt, dt=None):
        dt = dt or self.datas[0].datetime.date(0)
        #print(f'{dt.isoformat()} - {txt}')

    def next(self):
        sentiment = self.datas[0].sentiment[0]
        close_price = self.datas[0].close[0]

        # Log the sentiment and close price
        self.log(f'Sentiment: {sentiment}, Close Price: {close_price}')

        if not self.position:
            if sentiment > self.params.sentiment_threshold:
                self.log(f'BUY CREATE at {close_price}')
                self.buy()
        else:
            if sentiment <= self.params.sentiment_threshold:
                self.log(f'SELL CREATE at {close_price}')
                self.sell()

print("Sentiment Values:")
print(merged_df[['Date', 'sentiment']])

data = SentimentData(
    dataname=merged_df,
    datetime=0,
    open=2,
    high=5,
    low=6,
    close=1,
    volume=4,
    openinterest=-1,
    sentiment=7  
)

cerebro = bt.Cerebro()
cerebro.adddata(data)
cerebro.addstrategy(SentimentStrategy)
cerebro.broker.setcash(10000.0)
cerebro.broker.setcommission(commission=0.001)

print("Starting Portfolio Value:", cerebro.broker.getvalue())
cerebro.run()
print("Ending Portfolio Value:", cerebro.broker.getvalue())
cerebro.plot()
merged_df.plot(x='Date', y='sentiment', kind='line', figsize=(12,6))
plt.show()