/* The result of this query is the sum of all orders for each date  */
SELECT SUM(amount), date
FROM a
GROUP by date
ORDER by SUM(amount) DESC

/* The result of this query is the maximum order in the month of june */
SELECT order_id, amount 
FROM june join (SELECT max(amount) from june) b ON june.amount = b.max(amount)