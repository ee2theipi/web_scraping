# https://www.goodreturns.in/gold-rates/

import requests
from bs4 import BeautifulSoup

city = 'https://www.goodreturns.in/gold-rates/chandigarh.html'
response = requests.get(gold_rate_city)

#print(response)