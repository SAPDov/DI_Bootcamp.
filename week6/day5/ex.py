import psycopg2
import psycopg2.extras
import sqlite3 as sl


HOSTNAME = "localhost"
USERNAME = "postgres"
PASSWORD = "postgres"
DATABASE = "supermarket"

class MenuItem:
	def __init__(self, item, price):
		self.item = item
		self.price = price
		 
	def save_item (self):
		quary =f"INSERT INTO items (name, price) VALUES ('{self.item}', {self.price})"
		self.run(quary)

	def delete_item(self):
		quary = f"DELETE FROM items WHERE name ='{self.item}'"
		self.run(quary)

	def update_item(self, old_item):
		quary = f"UPDATE items SET name = '{self.item}' WHERE name = '{old_item}'"
		quary = f"UPDATE items SET price = '{self.price}' WHERE name = '{self.item}'" 
		self.run(quary)
	
	def all (self):
		quary_all = f"SELECT * FROM items"
		connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
		cursor = connection.cursor()
		cursor.execute(quary_all)
		connection.commit()
		results = cursor.fetchall()
		connection.close()

		for item in results:
			print(item)


	def run (self, quary):
		connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
		cursor = connection.cursor()
		cursor.execute(quary)
		connection.commit()
		connection.close()
	
	def get_by_name (self, obtain_item):
		item_name =f"SELECT name, price FROM items WHERE name = '{obtain_item}'"
		connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
		cursor = connection.cursor()
		cursor.execute(item_name)
		connection.commit()
		results = cursor.fetchall()
		connection.close()

		if results:
			print(results)
		else: 
			 print(None)

		

# menu = MenuItem("hot dog", 20)
# # menu.update_item("BurgerBBB")
# # menu.save_item()
# # menu.all()
# menu.get_by_name("bread")
# menu.delete_item()
