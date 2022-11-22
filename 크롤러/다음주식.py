from urllib import response
import requests
import json

url = "https://finance.daum.net/api/market_index/days"

custom_header = {
    "referer":"https://finance.daum.net/api",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}


params = {"page":1, "perPage":10, "market":"KOSPI", "pagination":"true"}
response = requests.get(url, headers=custom_header, params=params)
print(response.status_code )

data = json.loads(response.content)
print( data)
