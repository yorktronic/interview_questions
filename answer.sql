# The result of this query is a table that has all user_id's and the average time between their orders
SELECT user_id a, (DATEDIFF(MAX(order_date), MIN(order_date))) / (count(order_id) - 1) b 
FROM orders 
GROUP BY user_id 
HAVING count(order_id) > 1

# This query is the same as above but shows the average time between orders across all users
# Each user is weighted equally in this calculation
SELECT AVG(b) AS 'non_weighted_average'
    FROM (
        SELECT user_id a, (DATEDIFF(MAX(order_date), MIN(order_date))) / (count(order_id) - 1) b 
        FROM orders 
        GROUP BY user_id 
        HAVING count(order_id) > 1
) AS x;

# Finally, this query calculates the weighted average
# The total number of days in between orders is summed for all users, and then divided by the sum of the total number of gaps between orders 
SELECT (SUM(c) / SUM(b)) AS 'weighted_average'
FROM (
    SELECT user_id a, (COUNT(order_id) - 1) b, (DATEDIFF(MAX(order_date), MIN(order_date))) c
    FROM orders
    GROUP BY user_id
    HAVING count(order_id) > 1 
) AS x;