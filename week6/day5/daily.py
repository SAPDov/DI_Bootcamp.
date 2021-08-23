
import requests
import random
import pprint
import json
import psycopg2
import psycopg2.extras
import sqlite3


HOSTNAME = "localhost"
USERNAME = "postgres"
PASSWORD = "postgres"
DATABASE = "countries"




def add_county(random_list):
    for c in random_list:
        quary = f"""INSERT INTO country (country_name, capital, flag, subregion, population) 
            VALUES ('{c['name']}', '{c['capital']}', '{c['flag']}', '{c['subregion']}', {c['population']})"""
        run(quary)

def random_country(n):
    random_list = random.sample(get_countries(), n)
    return random_list

def run(quary):
    connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
    cursor = connection.cursor()
    cursor.execute(quary)
    connection.commit()
    connection.close()

add_county(random_country(10))
