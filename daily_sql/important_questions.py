'''I have customer table with id, name
product table --> id, name, price
orders_table --> id, prod_id, cust_id, quantity, date

frame questions for writing sql queries'''

# Retrieve all customers:

SELECT * FROM customer;

# Find a specific product:

SELECT name, price FROM product WHERE id = [specific_product_id];

# Write an SQL query to list all the orders along with the product names, customer names, quantities, and dates.

SELECT 
    o.id AS order_id,
    p.name AS product_name,
    c.name AS customer_name,
    o.quantity,
    o.date
FROM 
    orders_table o
JOIN 
    product p ON o.prod_id = p.id
JOIN 
    customer c ON o.cust_id = c.id;


# Total quantity ordered for each product:

SELECT 
    p.name, 
    SUM(o.quantity) AS total_quantity
FROM 
    orders_table o
JOIN 
    product p ON o.prod_id = p.id
GROUP BY 
    p.name;


# Write an SQL query to fetch all the orders made by a specific customer.

SELECT 
    o.id AS order_id,
    p.name AS product_name,
    o.quantity,
    o.date
FROM 
    orders_table o
JOIN 
    product p ON o.prod_id = p.id
WHERE 
    o.cust_id = [specific_customer_id];


# Write an SQL query to find the most recent orders made in the orders table.

SELECT 
    o.id AS order_id,
    p.name AS product_name,
    c.name AS customer_name,
    o.quantity,
    o.date
FROM 
    orders_table o
JOIN 
    product p ON o.prod_id = p.id
JOIN 
    customer c ON o.cust_id = c.id
ORDER BY 
    o.date DESC;


# Write an SQL query to find the top 5 most expensive products in the product table.

SELECT 
    name, 
    price 
FROM 
    product
ORDER BY 
    price DESC
LIMIT 5;


# Write an SQL query to find the customer who has placed the most orders.

SELECT 
    c.name, 
    COUNT(o.id) AS order_count
FROM 
    orders_table o
JOIN 
    customer c ON o.cust_id = c.id
GROUP BY 
    c.name
ORDER BY 
    order_count DESC
LIMIT 1;


# Write an SQL query to calculate the total revenue generated for each product.

SELECT 
    p.name, 
    SUM(o.quantity * p.price) AS total_revenue
FROM 
    orders_table o
JOIN 
    product p ON o.prod_id = p.id
GROUP BY 
    p.name;


# Write an SQL query to fetch all orders placed within a specific date range.


SELECT 
    o.id AS order_id,
    p.name AS product_name,
    c.name AS customer_name,
    o.quantity,
    o.date
FROM 
    orders_table o
JOIN 
    product p ON o.prod_id = p.id
JOIN 
    customer c ON o.cust_id = c.id
WHERE 
    o.date BETWEEN [start_date] AND [end_date];


# Write an SQL query to find the average price of the products that have been ordered.

SELECT 
    AVG(p.price) AS average_price
FROM 
    orders_table o
JOIN 
    product p ON o.prod_id = p.id;


# Write an SQL query to find products that have never been ordered.

SELECT 
    p.id,
    p.name,
    p.price
FROM 
    product p
LEFT JOIN 
    orders_table o ON p.id = o.prod_id
WHERE 
    o.prod_id IS NULL;


# Write an SQL query to calculate the total revenue generated from each customer.

SELECT 
    c.name, 
    SUM(o.quantity * p.price) AS total_revenue
FROM 
    orders_table o
JOIN 
    customer c ON o.cust_id = c.id
JOIN 
    product p ON o.prod_id = p.id
GROUP BY 
    c.name;


# Write an SQL query to find all customers who have ordered a specific product.

SELECT 
    DISTINCT c.name
FROM 
    orders_table o
JOIN 
    customer c ON o.cust_id = c.id
WHERE 
    o.prod_id = [specific_product_id];


# Write an SQL query to list all products ordered by a specific customer along with the order details.

SELECT 
    p.name, 
    o.quantity,
    o.date
FROM 
    orders_table o
JOIN 
    product p ON o.prod_id = p.id
WHERE 
    o.cust_id = [specific_customer_id];


# To find customers who have not placed any orders within the last 7 days, you can use a query that combines the customer table with the orders_table using a LEFT JOIN and then filters out customers who have placed orders in the last 7 days using a WHERE clause with a NULL check on the order date.


SELECT 
    c.id,
    c.name
FROM 
    customer c
LEFT JOIN 
    orders_table o ON c.id = o.cust_id AND o.date >= CURDATE() - INTERVAL 7 DAY
WHERE 
    o.id IS NULL;



# Write an SQL query to count the total number of orders placed in the orders table.

SELECT COUNT(*) AS total_orders FROM orders_table;

# Write an SQL query to find customers who have ordered more than a certain quantity of any product.

SELECT DISTINCT c.id, c.name
FROM customer c
JOIN orders_table o ON c.id = o.cust_id
WHERE o.quantity > [specified_quantity];

# Write an SQL query to calculate the average quantity of products ordered by each customer.

SELECT c.id, c.name, AVG(o.quantity) AS average_quantity
FROM customer c
JOIN orders_table o ON c.id = o.cust_id
GROUP BY c.id, c.name;

# Write an SQL query to find products that have been ordered by more than one customer.

SELECT p.id, p.name
FROM product p
JOIN orders_table o ON p.id = o.prod_id
GROUP BY p.id, p.name
HAVING COUNT(DISTINCT o.cust_id) > 1;

# Write an SQL query to list all orders placed on a specific date.


SELECT o.id AS order_id, p.name AS product_name, c.name AS customer_name, o.quantity, o.date
FROM orders_table o
JOIN product p ON o.prod_id = p.id
JOIN customer c ON o.cust_id = c.id
WHERE o.date = '[specific_date]';

# Write an SQL query to identify customers who have ordered every product available in the product table.

SELECT c.id, c.name
FROM customer c
JOIN orders_table o ON c.id = o.cust_id
JOIN product p ON o.prod_id = p.id
GROUP BY c.id, c.name
HAVING COUNT(DISTINCT p.id) = (SELECT COUNT(*) FROM product);

# Write an SQL query to calculate the average revenue generated per order.

SELECT AVG(o.quantity * p.price) AS average_revenue_per_order
FROM orders_table o
JOIN product p ON o.prod_id = p.id;

# Write an SQL query to find products that have been ordered more than a specified number of times.

SELECT p.id, p.name, COUNT(o.id) AS order_count
FROM product p
JOIN orders_table o ON p.id = o.prod_id
GROUP BY p.id, p.name
HAVING COUNT(o.id) > [specified_number];


# Write an SQL query to find the customer who has spent the most money on orders.

SELECT c.id, c.name, SUM(o.quantity * p.price) AS total_spent
FROM customer c
JOIN orders_table o ON c.id = o.cust_id
JOIN product p ON o.prod_id = p.id
GROUP BY c.id, c.name
ORDER BY total_spent DESC
LIMIT 1;

# Write an SQL query to find the product with the highest total quantity ordered.


SELECT p.id, p.name, SUM(o.quantity) AS total_quantity
FROM product p
JOIN orders_table o ON p.id = o.prod_id
GROUP BY p.id, p.name
ORDER BY total_quantity DESC
LIMIT 1;


# Write an SQL query to list customers who have never placed any order.

SELECT c.id, c.name
FROM customer c
LEFT JOIN orders_table o ON c.id = o.cust_id
WHERE o.id IS NULL;


# Write an SQL query to find the most ordered product for each month.

SELECT 
    DATE_FORMAT(o.date, '%Y-%m') AS month,
    p.name,
    SUM(o.quantity) AS total_quantity
FROM 
    orders_table o
JOIN 
    product p ON o.prod_id = p.id
GROUP BY 
    DATE_FORMAT(o.date, '%Y-%m'), p.name
ORDER BY 
    month, total_quantity DESC;

# Write an SQL query to list all orders placed within the last month.


SELECT o.id AS order_id, p.name AS product_name, c.name AS customer_name, o.quantity, o.date
FROM orders_table o
JOIN product p ON o.prod_id = p.id
JOIN customer c ON o.cust_id = c.id
WHERE o.date >= CURDATE() - INTERVAL 1 MONTH;


# Write an SQL query to find the total quantity of products ordered by each customer.


SELECT c.id, c.name, SUM(o.quantity) AS total_quantity
FROM customer c
JOIN orders_table o ON c.id = o.cust_id
GROUP BY c.id, c.name;


# Write an SQL query to list all products and the number of times each product has been ordered.

SELECT p.id, p.name, COUNT(o.id) AS order_count
FROM product p
JOIN orders_table o ON p.id = o.prod_id
GROUP BY p.id, p.name;


# Write an SQL query to calculate the total revenue generated from orders placed in the last year.

SELECT SUM(o.quantity * p.price) AS total_revenue
FROM orders_table o
JOIN product p ON o.prod_id = p.id
WHERE o.date >= CURDATE() - INTERVAL 1 YEAR;

# Write an SQL query to identify orders that contain more than one type of product.

SELECT o.id AS order_id
FROM orders_table o
GROUP BY o.id
HAVING COUNT(DISTINCT o.prod_id) > 1;

# Write an SQL query to find customers who have placed orders on weekends (Saturday and Sunday).

SELECT DISTINCT c.id, c.name
FROM customer c
JOIN orders_table o ON c.id = o.cust_id
WHERE DAYOFWEEK(o.date) IN (1, 7);

# Write an SQL query to identify the product that has been ordered the fewest times.

SELECT p.id, p.name, COUNT(o.id) AS order_count
FROM product p
JOIN orders_table o ON p.id = o.prod_id
GROUP BY p.id, p.name
ORDER BY order_count ASC
LIMIT 1;

# Write an SQL query to list all customers and the total number of orders each has placed.

SELECT c.id, c.name, COUNT(o.id) AS order_count
FROM customer c
LEFT JOIN orders_table o ON c.id = o.cust_id
GROUP BY c.id, c.name;









