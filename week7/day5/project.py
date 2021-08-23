import requests
import json



url = "https://alpha-vantage.p.rapidapi.com/query"

querystring = {"market":"CNY","symbol":"BTC","function":"DIGITAL_CURRENCY_DAILY"}

headers = {
    'x-rapidapi-key': "f701eef6dcmshcd924a190cf185ep1d7335jsn1bd4a450409a",
    'x-rapidapi-host': "alpha-vantage.p.rapidapi.com"
    }

data = requests.request("GET", url, headers=headers, params=querystring)

print(data.text)


