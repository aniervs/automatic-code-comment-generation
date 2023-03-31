SELECT 
    customers.customer_name,
    SUM(order_items.quantity * order_items.price) AS total_spent
FROM
    customers
INNER JOIN orders
    ON customers.customer_id = orders.customer_id
INNER JOIN (
    SELECT 
        order_id, 
        SUM(quantity * price) AS total_order_cost 
    FROM 
        order_items 
    GROUP BY 
        order_id
) AS order_costs
    ON orders.order_id = order_costs.order_id
INNER JOIN (
    SELECT 
        order_id, 
        SUM(payment_amount) AS total_payments 
    FROM 
        payments 
    GROUP BY 
        order_id
) AS payment_totals
    ON orders.order_id = payment_totals.order_id
WHERE 
    total_payments >= total_order_cost
GROUP BY 
    customers.customer_id
HAVING 
    total_spent > 1000
ORDER BY 
    total_spent DESC;
