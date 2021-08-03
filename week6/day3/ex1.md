|SELECT film.title, language.name FROM film INNER JOIN language ON film.language_id = language.language_id;|
|:----|
|SELECT film.title, film.description, language.name FROM film LEFT OUTER JOIN language ON film.language_id = language.language_id;|
|SELECT film.title, film.description, language.name FROM film RIGHT OUTER JOIN language ON film.language_id = language.language_id;|
| CREATE TABLE new_film (|
| 	id SERIAL PRIMARY KEY,|
| 	name VARCHAR NOT NULL|
|);|
| INSERT INTO new_film (name) VALUES ('Million Dollar Baby'),|
| ('Free Willy'),|
| ('The Blind Side'),|
| ('American Pie');|
| CREATE TABLE customer_review (|
| review_id SERIAL PRIMARY KEY NOT NULL,|
| film_id int REFERENCES film (film_id) ON DELETE RESTRICT,|
| language_id int REFERENCES language (language_id) ON DELETE RESTRICT,|
| title varchar (100),|
| score int, check (score between 0 AND 10),|
| review_text TEXT,|
Exercise 1: DVD Rental

| last_update date|
| );|
| SELECT * FROM customer_review;|
|INSERT INTO customer_review (film_id, language_id, title, score, review_text, last_update)|
| VALUES ((SELECT film_id FROM film WHERE film_id is NULL), (SELECT language_id FROM language WHERE language_id='1') ,'Million Dollar Baby', '10', 'Fakes you out, then knocks you flat with a right hook to the heart.', '03/08/2021');|
| INSERT INTO customer_review (film_id, language_id, title, score, review_text, last_update)|
| VALUES ((SELECT film_id FROM film WHERE film_id is null), (SELECT language_id FROM language WHERE language_id ='1'),'Free Willy', '3', 		('I watched this film when my kids were 6 and 7. I didn not know the full story. It was much darker than I expected and ended up being a big trigger for my 6-year old fost-adopted daughter still grieving the move from her foster family to our forever family'), '18/08/2001');|
| INSERT INTO customer_review (film_id, language_id, title, score, review_text, last_update)|
| VALUES ((SELECT film_id FROM film WHERE film_id is null), (SELECT language_id FROM language WHERE language_id ='1'),'The Blind Side', '8', 'As a fable about the power of giving, it hits pretty hard.', '10/04/2014');|
| INSERT INTO customer_review (film_id, language_id, title, score, review_text, last_update)|
| VALUES ((SELECT film_id FROM film WHERE film_id is null), (SELECT language_id FROM language WHERE language_id ='1'),'American Pie', '5', 'Another giggly gross-out comedy for teenagers, this one somewhat better than most by virtue of a more satisfying ending.', '05/07/2011');|
| INSERT INTO customer_review (film_id, language_id, title, score, review_text, last_update)|
| VALUES ((SELECT film_id FROM film WHERE title = 'Baby Hall'), (SELECT language_id FROM language WHERE language_id ='1'),'Baby Hall', '8',|
| 		('A very good movie. it''s one of my favorite.'), '05/07/2015');|
| INSERT INTO customer_review (film_id, language_id, title, score, review_text, last_update)|
| VALUES ((SELECT film_id FROM film WHERE title = 'Autman Crow'), (SELECT language_id FROM language WHERE language_id ='1'),'Autman Crow', '9',|
| 		('Autumcrow provided a pleasurable reading experience for the Halloween Season. The slim volume seven tales capture the spirit of the authors popular Library Macabre youtube channel, where every day is Halloween'), '05/07/2016');|
| UPDATE customer_review SET film_id = "46" WHERE review_id = '5';|
| UPDATE customer_review SET title = "Autumn Crow" WHERE review_id = '5';|
| DELETE FROM film WHERE film_id = '47';|

| Exercise 2 : DVD Rental|

| UPDATE customer_review SET language_id = '5' WHERE title = 'Free Willy';|
| UPDATE customer_review SET language_id = '2' WHERE title = 'Million Dollar Baby';|
| UPDATE customer_review SET language_id = '2' WHERE title = 'Autumn Crow';|
| SELECT language_id FROM film WHERE title = 'Autumn Crow';|
| DROP TABLE customer_review;|
| SELECT title, rental_rate, rental.return_date FROM film LEFT JOIN rental ON rental.last_update = film.last_update WHERE return_date is null ORDER BY rental_rate DESC LIMIT 30;|
| SELECT film.title, film.description, actor.first_name FROM film INNER JOIN actor ON actor.actor_id = film.film_id WHERE film.description LIKE '%sumo wrestler%' OR last_name ='Monroe' AND first_name ='Penelope';|
| SELECT * FROM film WHERE rating = 'R' AND description LIKE '%Documentary%' AND length < 61|
|SELECT film.title, c.first_name, c.last_name, r.rental_date FROM filmINNER JOIN inventory AS i|
|ON i.film_id = film.film_id|
|INNER JOIN rental AS r|
|ON r.inventory_id = i.inventory_id|
|INNER JOIN customer AS c|
|ON c.customer_id = r.customer_idWHERE c.first_name = 'Matthew' AND c.last_name = 'Mahan' AND film.rental_rate > '4' AND r.rental_date BETWEEN '2005-07-28' AND '2005-08-01';SELECT film.title, c.first_name, c.last_name, film.rental_rate FROM filmINNER JOIN inventory AS i|
|ON i.film_id = film.film_id|
|INNER JOIN rental AS r|
|ON r.inventory_id = i.inventory_id|
|INNER JOIN customer AS c|
|ON c.customer_id = r.customer_idWHERE c.first_name = 'Matthew' AND c.last_name = 'Mahan' AND (description LIKE '%Boat%' OR title LIKE '%boat%') ORDER BY film.rental_rate DESC;|
