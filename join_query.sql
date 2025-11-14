SELECT 
    c.name AS customer_name,
    c.city,
    p.name AS product_name,
    p.category,
    oi.quantity AS quantity_ordered,
    o.order_date,
    (oi.quantity * p.price) AS total_amount
FROM 
    customers c
    INNER JOIN orders o ON c.customer_id = o.customer_id
    INNER JOIN order_items oi ON o.order_id = oi.order_id
    INNER JOIN products p ON oi.product_id = p.product_id
ORDER BY 
    o.order_date DESC, c.name;

