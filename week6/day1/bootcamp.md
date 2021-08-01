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