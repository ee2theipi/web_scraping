This project is done in partial fulfillment of the course credits IDC409 taken by Dr. Vishal Bharadwaj.  
It involves:
  1) **Gold: Ref. files:**
     - Gold_data_unfiltered.html - Contains the source code www.groww.in/gold-rates as on 5-11-24. Although we fetch it everytime.
     - gold_prices.py - Scrapes the gold price as stores it in sqlite3
     - gold_prices.db - database for gold prices
     - gold_prices_plot.py
     - gold_prices_plot.png
      
  2) **Stock Ref. files:** (website: https://www.equitypandit.com/historical-data/ADANIENT)
     - stock_prices.py - scrapes ADANI ENTERPRISES price data for the last 5 years
     - stock_prices.db - database
     - regression files (Interperting the data and trading strategy)

  3) **News (War, election, ... any news):**
     - newsapi_python.py
     - news.db

Testing the Relation/impact of news on stock prices - (presentation) 
Testing how news affect the stock price:
 - Check for dates on which there is sudden rise/fall in stock price.
 - scrape for news on adani or related industry (or any major global event) around that date.
 - Observation:
    - Positive news suggests a increase in price and negative news fall in price. 

Note: All the files should be executed in the order they are mentioned.
database file will be saved in default user directory (C:/users/admin/'database.db') maybe

**Conclusions for stock (ADANI Enterprise)**
- Looking at the gaussian of the past 5 years it can be concluded that the stock is pretty volatile. Except for the year 2023-24 what it shows comparatively higher stability.
- Linear regression (along with the news) helps us predict the stock price and pick a trading strategy based on the fact that the price movement will be about the best fit line.

Part of interpretation and prediction involed in presentation.

How does linear regerssion help?
- One can expect
