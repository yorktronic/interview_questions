/* 176 - Second Highest Salary 
https://leetcode.com/problems/second-highest-salary/
*/
select ifnull(
    (select distinct salary 
     from Employee
     order by salary desc
     limit 1, offset 1),
    NULL
    ) as SecondHighestSalary