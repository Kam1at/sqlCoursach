SELECT first_name, last_name, home_phone, region FROM employees
WHERE region IS NULL;

SELECT country FROM customers
INTERSECT
SELECT country FROM suppliers
EXCEPT 
SELECT country FROM employees;