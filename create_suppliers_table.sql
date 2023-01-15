CREATE TABLE suppliers
(
    supplier_id serial PRIMARY KEY,
    company_name varchar(250) UNIQUE NOT NULL,
    contact_name varchar(250) NOT NULL,
    contact_post varchar(250) NOT NULL,
    country varchar(100) NOT NULL,
    address varchar(250) NOT NULL,
    phone varchar(25) NOT NULL,
    fax varchar (25),
    homepage varchar (100)
);

ALTER TABLE products 
ADD supplier_id int REFERENCES suppliers(supplier_id); 
