SELECT product_name, units_on_order, suppliers.contact_name, suppliers.phone 
FROM products
JOIN suppliers USING(supplier_id)
JOIN categories USING(category_id)
WHERE discontinued = 0 AND category_name IN('Beverages', 'Seafood') AND units_on_order < 20
ORDER BY units_on_order DESC