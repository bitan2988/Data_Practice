import requests
import pandas as pd

headers = {
	"X-RapidAPI-Key": "SIGN-UP-FOR-KEY",
	"X-RapidAPI-Host": "alpha-vantage.p.rapidapi.com"
}

# url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=AD5AW3LKSXM1EDB3'

url = 'https://www.alphavantage.co/query'

apiKey = 'AD5AW3LKSXM1EDB3'
querystring = {
    'apikey' : apiKey,
    'function' : 'TIME_SERIES_INTRADAY',
    'symbol' : 'IBM',
    'interval' : '5min'
}

response = requests.request("GET", url, headers=headers, params=querystring)

data = response.json()
df = pd.json_normalize(data)

print(data)
