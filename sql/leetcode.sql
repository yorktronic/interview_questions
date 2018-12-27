/* 176 - Second Highest Salary
https://leetcode.com/problems/second-highest-salary/
*/
SELECT ifnull(
                (SELECT DISTINCT salary
                 FROM Employee
                 ORDER BY salary DESC LIMIT 1, 1), NULL) AS SecondHighestSalary /* 177 - Nth Highest Salary
https://leetcode.com/problems/nth-highest-salary/
*/
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT BEGIN
SET N=N-1; RETURN (# WRITE your MySQL query STATEMENT below.
                   SELECT Salary
                   FROM Employee
                   GROUP BY Salary
                   ORDER BY Salary DESC LIMIT 1
                   OFFSET N); END

