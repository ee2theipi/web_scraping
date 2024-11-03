# https://www.goodreturns.in/gold-rates/

import requests
from bs4 import BeautifulSoup

city = 'https://groww.in/gold-rates'
response = requests.get(city)

#print(response)
