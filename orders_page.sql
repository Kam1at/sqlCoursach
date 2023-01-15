SELECT * FROM orders
ORDER BY required_date DESC, shipped_date;

SELECT AVG(shipped_date - order_date) AS average_days FROM orders
WHERE ship_country = 'USA';

SELECT SUM(unit_price * units_in_stock) AS total FROM products
WHERE discontinued = 0;