SELECT COUNT(*) AS customers_count FROM customers;

SELECT DISTINCT city, country FROM customers;

SELECT DISTINCT customers.company_name, CONCAT(employees.first_name, ' ', employees.last_name) AS employeer_name
FROM orders
JOIN customers USING(customer_id)
JOIN employees USING(employee_id)
LEFT JOIN shippers ON orders.ship_via=shippers.shipper_id
WHERE employees.city='London'
AND customers.city='London'
AND shippers.company_name='Speedy Express';

SELECT customers.company_name, orders.order_id
FROM customers
FULL JOIN orders USING(customer_id)
WHERE orders.order_id IS NULL;