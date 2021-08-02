| Database: dvdrental|
|:----|
| DROP DATABASE dvdrental;|
|CREATE DATABASE dvdrental|
|    WITH    OWNER = postgres|
|     ENCODING = 'UTF8'|
|   LC_COLLATE = 'Hebrew_Israel.1255'|
|    LC_CTYPE = 'Hebrew_Israel.1255'|
|    TABLESPACE = pg_default|
|    CONNECTION LIMIT = -1;|
|SELECT * FROM customer;|
| SELECT first_name || ' ' || last_name AS full_name FROM customer;|
| SELECT DISTINCT create_date FROM customer;|
| SELECT * FROM customer ORDER BY first_name ASC SELECT * FROM film;|
| SELECT film_id| title| description| release_year| rental_rate FROM film ORDER BY rental_rate ASC;|
| SELECT address| district| phone FROM customer INNER JOIN address ON customer.address_id = address.address_id WHERE district = 'Texas';|
| SELECT * FROM film WHERE film_id = '15' OR film_id = '150'|
| SELECT film_id| title| description| length| rental_rate FROM film WHERE title = 'Million Dollar Baby';|
| SELECT film_id| title| description| length| rental_rate FROM film WHERE title LIKE 'M%';|
| SELECT * FROM film ORDER BY rental_rate ASC LIMIT 10;|
| SELECT * FROM film ORDER BY rental_rate ASC OFFSET 10 ROWS FETCH FIRST 10 ROW ONLY;|
| SELECT DISTINCT customer.*| amount| payment_date FROM customer INNER JOIN payment ON customer.customer_id = payment.customer_id ORDER BY customer.customer_id ASC; SELECT film.film_id| title FROM film INNER JOIN inventory ON inventory.film_id = film.film_id WHERE inventory.film_id != film.film_id;|
| SELECT country| city FROM country INNER JOIN city ON country.country_id = city.country_id;|
