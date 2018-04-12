use sakila;
drop table filmtabletest;

CREATE TABLE IF NOT EXISTS filmTableTest as select title, film_id, 
(select count(*) from inventory where film.film_id = inventory.film_id) 'number of copies'
from film;

SELECT * FROM filmtabletest;