|Database: public|
|:----|
|DROP DATABASE public;|
|CREATE TABLE items (|
|name VARCHAR(50),|
|price SMALLINT|
|	|
| );|
| CREATE TABLE customers (|
|first_name VARCHAR(50),|
| last_name VARCHAR(100)|
| );|
| ALTER TABLE items ADD id SERIAL PRIMARY KEY;|
|INSERT INTO items (name, price)|
| VALUES('Small Desk', '100');|
| INSERT INTO items (name, price)|
| VALUES('Large desk','300');|
| INSERT INTO items (name, price)|
| VALUES('fan','60');|
| INSERT INTO customers (first_name, last_name)|
| VALUES('Greg', 'Jones');|
| INSERT INTO customers (first_name, last_name)|
| VALUES('Sandra', 'Jones');|
| INSERT INTO customers (first_name, last_name)|
|VALUES('Scott', 'Scott');|
| INSERT INTO customers (first_name, last_name)|
|VALUES('Trevor', 'Green');|
| INSERT INTO customers (first_name, last_name)|
| VALUES('Melanie', 'Johnson');|
| SELECT * FROM items;|
|SELECT * FROM customers;|
| DELETE FROM items WHERE price > 10|
|SELECT * FROM customers;|
| SELECT * FROM items WHERE price > 80;|
| SELECT * FROM items WHERE price <= 300;|
|SELECT * FROM customers WHERE last_name = 'Smith';|
|SELECT * FROM customers WHERE last_name = 'Jones';|
| SELECT * FROM customers WHERE last_name != 'Scott'
|DROP TABLE IF EXISTS customers|
|:----|
| SELECT * FROM customers|
|CREATE TABLE customers (costumer_id SERIAL PRIMARY KEY, f_name VARCHAR (50), l_name VARCHAR (100))|
|INSERT INTO customers (f_name, l_name)|
|VALUES ('Greg', 'Jones'), ('Sandra', 'Jones'), ('Scott', 'Scott'), ('Trevor', 'Green'), ('Melanie', 'Johnson');|
|SELECT * FROM customers|
| SELECT * FROM items|
| CREATE TABLE purchases (|
|customer_id INTEGER,|
| item_id INTEGER,|
| FOREIGN KEY (item_id) REFERENCES items (id),|
| FOREIGN KEY (customer_id) REFERENCES customers (costumer_id));|
|SELECT * FROM purchases|
| SELECT * FROM items|
| UPDATE items SET id ='1' WHERE price='100';|
|UPDATE items SET id ='2' WHERE price='300';|
| UPDATE items SET id ='3' WHERE price ='60';|
| SELECT * FROM items|
|INSERT INTO purchases(customer_id, item_id) VALUES (1,2),(2,3),(3,1),(4,1),(5,2);|
| SELECT * FROM purchases|
| SELECT customers.costumer_id, f_name, l_name FROM customers|
| INNER JOIN purchases|
| ON customers.costumer_id = purchases.customer_id;|
| SELECT items.id, name, price FROM items|
|INNER JOIN purchases|
|ON items.id = purchases.item_id;|
| SELECT * FROM customers|
|SELECT * FROM customers JOIN purchases ON customers.costumer_id = purchases.customer_id;|
| SELECT * FROM customers JOIN purchases ON customers.costumer_id = purchases.customer_id WHERE customers.costumer_id = '4' ;|
| SELECT * FROM items JOIN purchases ON items.id = purchases.item_id;|
| SELECT * FROM items JOIN purchases ON items.id = purchases.item_id WHERE items.id = '1' OR items.id = '2' ;|
|INSERT INTO purchases(customer_id, item_id) VALUES (1,2),(2,3),(3,1),(4,1),(5,2);|
| SELECT * FROM purchases|
| INSERT INTO items (name ,price) VALUES ('Hard Drive', 9.99);|
| UPDATE items SET id ='4' WHERE price ='10'|
| SELECT * FROM items|
| SELECT id FROM items WHERE items.name = 'Hard Drive' INSERT INTO purchases (customer_id ,item_id) VALUES (3,4);|
| SELECT * FROM purchases;|
|SELECT f_name, l_name, name FROM customers JOIN items ON customers.costumer_id = items.id JOIN purchases ON customers.costumer_id = purchases.customer_id;|

