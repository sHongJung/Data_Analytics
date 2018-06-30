-- These are not the only right answers to these questions!

-- Question 1
SELECT COUNT(DISTINCT(customer_id)) FROM rental;

-- Question 2
SELECT COUNT(*)
FROM film f
JOIN film_actor fa
ON f.film_id = fa.film_id
JOIN actor a
ON fa.actor_id = a.actor_id
WHERE a.first_name = 'NICK'
AND a.last_name = 'WAHLBERG';

-- Question 3
SELECT COUNT(DISTINCT(f.film_id))
FROM film f
JOIN inventory i
ON f.film_id = i.inventory_id
WHERE i.inventory_id IN
(SELECT inventory_id
FROM rental
WHERE YEAR(rental_date) = 2005
AND MONTH(rental_date) = 5)
AND LOWER(f.description) like '%lumberjack%';

-- Question 4
SELECT COUNT(*) FROM (
SELECT customer_id
FROM payment
GROUP BY customer_id
HAVING COUNT(DISTINCT(YEAR(payment_date))) > 1) a;

-- Question 5
SELECT COUNT(*) FROM 
(SELECT DISTINCT customer_id
FROM payment
WHERE year(payment_date) = 2006) payments_2006
LEFT OUTER JOIN (SELECT DISTINCT customer_id
FROM payment
WHERE year(payment_date) = 2005) payments_2005
ON payments_2006.customer_id = payments_2005.customer_id
WHERE payments_2005.customer_id IS NULL;
