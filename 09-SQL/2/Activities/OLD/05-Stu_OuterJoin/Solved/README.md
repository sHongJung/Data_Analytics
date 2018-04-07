# Nested Joins

* Up to this point, you have learned to perform joins using two tables. It is not much of a stretch to extend the query across three or more tables! 

## Instructions

1. Write a query to display all horror and sports films, and display the genre of each film.

   ```sql
   SELECT f.title, c.name
   FROM film f
   INNER JOIN film_category fc
   ON (f.film_id = fc.film_id)
   INNER JOIN category c
   ON (fc.category_id = c.category_id)
   WHERE c.name = 'horror'
   OR c.name = 'sports';
   ```

2. Write a query to display the date of rental, the customer's ID number, and the title of the film that was rented. You will need to use `rental`, `film`, and `inventory` tables. Sort the results by date, starting with the earliest date.

   ```sql
   SELECT r.rental_date, r.customer_id, f.title
   FROM rental r
   INNER JOIN inventory i
   ON (r.inventory_id = i.inventory_id)
   INNER JOIN film f
   ON (i.film_id = f.film_id)
   ORDER BY rental_date ASC;
   ```

## Bonuses

* If you finish early, begin looking into subqueries in MySQL. Subqueries and joins often accomplish the same task. Try to see if you can perform one of the above problems with subqueries instead!
