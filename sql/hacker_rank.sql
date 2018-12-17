/* Type of Triangle */
select a, b, c
case
    when (a > 0 and b > 0 and c > 0 and (a + b > c) and (b + c > a) and (a + c > b))
    then (                                                                         
        case
            when (a = b or b = c or a = c) then "Isosceles"
            when (a = b and b = c) then "Equilateral"
            else 'Scalene'
        end
    )
    else 'Not A Triangle'
end                                                                        
from triangles;

/* The PADS 
https://www.hackerrank.com/challenges/the-pads/problem
*/
select str_out
from (
    select concat(name, '(', left(occupation, 1), ')') as str_out, 1 as sort_key
    from occupations
    union
    select concat('There are a total of ', o.ct, ' ', lower(o.occupation), 's.' ) as str_out, 2 as sort_key
    from (
        select occupation, count(name) ct
        from occupations
        group by occupation
        order by ct, occupation
    ) o
    order by sort_key, str_out
) a

/* Occupations
https://www.hackerrank.com/challenges/occupations/problem 
*/
set @r1=0, @r2=0, @r3=0, @r4=0;
select min(doctor), min(professor), min(singer), min(actor)
from (
select 
    case 
        when occupation = 'Doctor' then (@r1:=@r1+1)
        when occupation = 'Professor' then (@r2:=@r2+1)
        when occupation = 'Singer' then (@r3:=@r3+1)
        when occupation = 'Actor' then (@r4:=@r4+1) end as row_number,
    case when occupation = 'Doctor' then name end doctor,
    case when occupation = 'Professor' then name end professor,
    case when occupation = 'Singer' then name end singer,
    case when occupation = 'Actor' then name end actor
from occupations
order by name
) t
group by row_number;

/*
Binary Tree Nodes
https://www.hackerrank.com/challenges/binary-search-tree-1/problem
root: node has no parents
leaf: node has a parent and no children
inner: node has a parent and children 
*/
select n,
       if(p is null, 'Root',
          if((select count(*) from bst where p = b.n) > 0, 'Inner', 'Leaf'))
from bst as b order by n;

select n,
    case 
        when p is null then 'Root'
        when n in (select p from bst) then 'Inner'
        else 'Leaf'
    end as bin
from bst
order by n;

/*
New Companies
https://www.hackerrank.com/challenges/the-company/problem
- Founder -> Lead Manager -> Senior Manager -> Manager -> Employee
- Print company_code, founder_name, total # of lead managers, total # of 
  senior managers, total number of managers, total number of employees
- order by company_code
- tables may contain duplicate records
- company code is str
- lead_manager always reports to founder (match just company name)
- start with getting founders and lead managers for each company
*/

SELECT c.company_code, c.founder, lm.lead_managers, sm.senior_managers,
       m.managers, e.employees
FROM company c
INNER JOIN
(
    SELECT company_code, COUNT(DISTINCT lead_manager_code) lead_managers
    FROM lead_manager
    GROUP BY company_code
) lm
INNER JOIN
(
    SELECT company_code, COUNT(DISTINCT senior_manager_code) senior_managers
    FROM senior_manager
    GROUP BY company_code
) sm
INNER JOIN
(
    SELECT company_code, COUNT(DISTINCT manager_code) managers
    FROM manager
    GROUP BY company_code
) m
INNER JOIN
(
    SELECT company_code, COUNT(DISTINCT employee_code) employees
    FROM employee
    GROUP BY company_code
) e
ON c.company_code = lm.company_code
AND c.company_code = sm.company_code
AND c.company_code = m.company_code
AND c.company_code = e.company_code
ORDER BY c.company_code

/* OR */

SELECT c.company_code, c.founder, 
    COUNT(DISTINCT lm.lead_manager_code) lead_managers, 
    COUNT(DISTINCT sm.senior_manager_code) senior_managers, 
    COUNT(DISTINCT m.manager_code) manager_codes,
    COUNT(DISTINCT e.employee_code) employee_codes
FROM company c
INNER JOIN lead_manager lm
INNER JOIN senior_manager sm
INNER JOIN manager m
INNER JOIN employee e
ON c.company_code = lm.company_code
AND sm.lead_manager_code = lm.lead_manager_code
AND m.senior_manager_code = sm.senior_manager_code
AND e.manager_code = m.manager_code
GROUP BY c.company_code, c.founder
ORDER BY c.company_code ASC

/* Placements 
https://www.hackerrank.com/challenges/placements/problem
Output the names of students whose best friends got offered a higher salary than them
Find all pairs where the transpose exists
*/
SELECT s.name
FROM (
students s 
JOIN friends f ON s.id = f.id
JOIN packages p1 ON s.id = p1.id
JOIN packages p2 ON f.friend_id = p2.id
)
WHERE p2.salary > p1.salary
ORDER BY p2.salary

/*
Symmetric Pairs
https://www.hackerrank.com/challenges/symmetric-pairs/problem

*/
SELECT f4.x, f4.y
FROM (
    (SELECT f1.x, f1.y
    FROM functions f1
    INNER JOIN (
        SELECT y as x, x as y
        FROM functions
    ) f2
    ON f1.x = f2.x
    AND f1.y = f2.y
    WHERE f1.x < f1.y
    UNION
    SELECT f3.x, f3.y
    FROM (
        SELECT x, y, COUNT(*) ct
        FROM functions
        GROUP BY x, y
        ORDER BY x
    ) f3
    WHERE f3.ct > 1)
) f4
ORDER BY f4.x

/*
Top Earners
https://www.hackerrank.com/challenges/earnings-of-employees
*/
select (salary * months) as earnings, count(*)
from employee
group by 1
order by earnings desc
limit 1

/*
Weather Observation Station 18
https://www.hackerrank.com/challenges/weather-observation-station-18/
*/

select round((abs(a - c) + abs(b - d)), 4)
from (
    select min(lat_n) as a, min(long_w) as b, max(lat_n) as c, max(long_w) as d
    from station
) z

/*
Weather Observation Station 19
https://www.hackerrank.com/challenges/weather-observation-station-19/
*/
select round(sqrt(pow((a - b), 2) + pow((c - d), 2)), 4)
from (
    select min(lat_n) a, max(lat_n) b, min(long_w) c, max(long_w) d
    from station
) z