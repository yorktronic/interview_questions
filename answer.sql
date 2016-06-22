# The result of this query is a table that has all user_id's and the average time between their orders
SELECT user_id a, (DATEDIFF(MAX(order_date), MIN(order_date))) / (count(order_id) - 1) b 
FROM orders 
GROUP BY user_id 
HAVING count(order_id) > 1

# This query is the same as above but shows the average time between orders across all users
SELECT AVG(b)
    FROM (
        SELECT user_id a, (DATEDIFF(MAX(order_date), MIN(order_date))) / (count(order_id) - 1) b 
        FROM orders 
        GROUP BY user_id 
        HAVING count(order_id) > 1
    ) AS x;

