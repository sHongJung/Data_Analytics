-- #1
SELECT customer.first_name, customer.last_name, address.address
FROM customer
INNER JOIN address
ON (customer.address_id = address.address_id);

-- #2
SELECT rental.rental_id, payment.amount, rental.rental_date, rental.return_date
FROM payment
INNER JOIN rental
ON (payment.rental_id = rental.rental_id);
