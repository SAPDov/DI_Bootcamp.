import requests
import json
import sqlite3
import psycopg2
import psycopg2.extras



import requests

url = "https://love-calculator.p.rapidapi.com/getPercentage"

querystring = {"fname":"Guy","sname":"Hadad"}

headers = {
    'x-rapidapi-key': "f701eef6dcmshcd924a190cf185ep1d7335jsn1bd4a450409a",
    'x-rapidapi-host': "love-calculator.p.rapidapi.com"
    }

response = requests.get(url, headers=headers, params=querystring)

print(response.text)
	
   

