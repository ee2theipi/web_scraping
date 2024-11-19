import pandas as pd
import sqlite3
import backtrader as bt
from textblob import TextBlob

conn = sqlite3.connect('stock_prices.db')
conn2 = sqlite3.connect('news.db')
query = "SELECT Date, Closing_Price, Opening_Price, Percentage_Change, Volume, High, Low FROM STOCK_PRICE_OF_LAST_5_YEARS"
price_df = pd.read_sql(query, conn)

price_df['Date'] = pd.to_datetime(price_df['Date'])

# bringing data in right format and type
price_df['Closing_Price'] = price_df['Closing_Price'].replace('[\$,]', '', regex=True).astype(float)
price_df['Opening_Price'] = price_df['Opening_Price'].replace('[\$,]', '', regex=True).astype(float)
price_df['Percentage_Change'] = price_df['Percentage_Change'].replace('[\%,]', '', regex=True).astype(float)
price_df['Volume'] = price_df['Volume'].replace('[\$,]', '', regex=True).astype(float)
price_df['High'] = price_df['High'].replace('[\$,]', '', regex=True).astype(float)
price_df['Low'] = price_df['Low'].replace('[\$,]', '', regex=True).astype(float)

price_df = price_df.sort_values(by='Date')
#print(price_df.dtypes)
#print(price_df.head())

# Plots only the last month's data
last_month = price_df['Date'].max() - pd.DateOffset(months=1)
price_df = price_df[price_df['Date'] >= last_month]

news_query = "SELECT Published_on, Title, About FROM News"
news_df = pd.read_sql(news_query, conn2)

# Converting 'Published_on' to datetime format
news_df['Published_on'] = pd.to_datetime(news_df['Published_on'])

# Sentiment Score calculation for  news
news_df['sentiment'] = news_df['Title'].apply(lambda x: TextBlob(x).sentiment.polarity)

# handles issue of there being more then 1 news on a particular day
daily_sentiment = news_df.groupby('Published_on')['sentiment'].mean().reset_index()


price_df = price_df.merge(daily_sentiment, left_on='Date', right_on='Published_on', how='left')
price_df['sentiment'] = price_df['sentiment'].fillna(0)  # Fill NaNs with neutral sentiment (0)

price_df = price_df.drop(columns=['Published_on'])
print(price_df['sentiment'][1200:])
#print(price_df[['Date', 'Closing_Price', 'sentiment']].head())
print(price_df['sentiment'].describe())

# Define Custom Data Feed to include Sentiment
class CustomPandasData(bt.feeds.PandasData):
    lines = ('sentiment',)
    params = (('sentiment', -1),)

# Strategy
class SentimentStrategy(bt.Strategy):
    params = (('sentiment_threshold', 0.03),)
    def next(self):
        sentiment = self.data.sentiment[0]
        if sentiment > self.params.sentiment_threshold and not self.position:
            self.buy()
        elif sentiment < -self.params.sentiment_threshold and self.position:
            self.sell()

data = CustomPandasData(
    dataname=price_df,
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
cerebro.addstrategy(SentimentStrategy)
cerebro.adddata(data)
cerebro.broker.setcash(10000.0)
cerebro.broker.setcommission(commission=0.001) 
print("Starting Portfolio Value:", cerebro.broker.getvalue())
cerebro.run()
print("Ending Portfolio Value:", cerebro.broker.getvalue())
cerebro.plot()
