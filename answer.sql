/* -----------------------------------MYSQL QUERIES-----------------------------------------------------*/

/* The result of this query is a table that has all user_id's and the average time between their orders */
SELECT user_id a, (DATEDIFF(MAX(order_date), MIN(order_date))) / (count(order_id) - 1) b 
FROM orders 
GROUP BY user_id 
HAVING count(order_id) > 1

/* This query is the same as above but shows the average time between orders across all users */
/* Each user is weighted equally in this calculation */
SELECT AVG(b) AS 'non_weighted_average'
    FROM (
        SELECT user_id a, (DATEDIFF(MAX(order_date), MIN(order_date))) / (count(order_id) - 1) b 
        FROM orders 
        GROUP BY user_id 
        HAVING count(order_id) > 1
) AS x;

/* This query calculates the weighted average */
/* The total number of days in between orders is summed for all users, and then divided by the sum of the total number of gaps between orders */
SELECT (SUM(c) / SUM(b)) AS 'weighted_average'
FROM (
    SELECT user_id a, (COUNT(order_id) - 1) b, (DATEDIFF(MAX(order_date), MIN(order_date))) c
    FROM orders
    GROUP BY user_id
    HAVING count(order_id) > 1 
) AS x;

/* ----------------------------AWS REDSHIFT QUERIES USING WINDOW FUNCTIONS------------------------------*/

/* This query results in a table that has all user_id's and the average time between their orders */
/* Uses the LEAD window function */
SELECT user_id, (SUM(diff) / COUNT(user_id)) avg_diff
FROM (
    SELECT a.user_id, DATEDIFF(day, a.order_date, a.next_order_date) diff
    FROM ( 
        SELECT user_id, order_id, order_date, LEAD(order_date, 1) OVER (ORDER BY user_id ASC, order_date ASC) next_order_date
        FROM orders) a JOIN orders b ON a.user_id = b.user_id AND b.order_date = a.next_order_date)
GROUP BY user_id

/* Average time between orders across all users, with each user weighted equally */
SELECT AVG(non_weighted_avg) non_weighted_avg
FROM (
  SELECT user_id, (SUM(diff) / COUNT(user_id)) non_weighted_avg
  FROM (
    SELECT a.user_id, DATEDIFF(day, a.order_date, a.next_order_date) diff
    FROM ( 
      SELECT user_id, order_id, order_date, LEAD(order_date, 1) OVER (ORDER BY user_id ASC, order_date ASC) next_order_date
        FROM orders) a JOIN orders b ON a.user_id = b.user_id AND b.order_date = a.next_order_date)
     GROUP BY user_id)

/* Weighted average time between orders across all users */
SELECT (SUM(diff) / COUNT(user_id)) weighted_avg
  FROM (
    SELECT a.user_id, DATEDIFF(day, a.order_date, a.next_order_date) diff
    FROM ( 
      SELECT user_id, order_id, order_date, LEAD(order_date, 1) OVER (ORDER BY user_id ASC, order_date ASC) next_order_date
      FROM orders) a JOIN orders b ON a.user_id = b.user_id AND b.order_date = a.next_order_date)