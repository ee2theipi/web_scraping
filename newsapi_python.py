# api_key = eccf434a292f43bdb3d37f7d0d131a96

import requests

# NewsAPI used as endpoint  
url = ('https://newsapi.org/v2/everything?'
       'q=Apple AND india&'
       'from=2024-11-01&'
       'sortBy=popularity&'
       'apiKey=eccf434a292f43bdb3d37f7d0d131a96')

# GET request to the newsAPI
response = requests.get(url)

# Print the response
#print(response.json())

data = response.json()

for article in data['articles']:
    print(article['title'])
