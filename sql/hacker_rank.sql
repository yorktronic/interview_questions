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

/*
Weather Observation Station 20
https://www.hackerrank.com/challenges/weather-observation-station-20/
*/
set @row_number = -1;

select round(avg(z.lat_n), 4)
from (
select (@row_number:=@row_number + 1) as r, lat_n
from station
order by lat_n
) z
where z.r IN (FLOOR(@row_number / 2), CEIL(@row_number / 2));

/*
The Report
https://www.hackerrank.com/challenges/the-report/
*/
select case when grade >= 8 then name else NULL end as name, grade, marks
from (
    select students.name, grades.grade, students.marks
    from students
    inner join grades
    on students.marks between grades.min_mark
    and grades.max_mark
    order by grades.grade desc, students.name
) a

/*
Top Competitors
https://www.hackerrank.com/challenges/full-score/problem
*/
select hacker_id, name
from (
    select hacker_id, name, count(*) cnt
    from (
        select s.hacker_id, h.name, s.challenge_id, c.difficulty_level, s.score actual_score, d.score diff_score
        from submissions s
        inner join challenges c
        on s.challenge_id = c.challenge_id
        inner join difficulty d
        on c.difficulty_level = d.difficulty_level
        inner join hackers h
        on s.hacker_id = h.hacker_id
        where s.score = d.score
    ) a
    group by hacker_id, name
    order by cnt desc, hacker_id
) b
where cnt > 1;

/*or*/
select h.hacker_id, h.name
from submissions s
inner join challenges c
on s.challenge_id = c.challenge_id
inner join difficulty d
on c.difficulty_level = d.difficulty_level 
inner join hackers h
on s.hacker_id = h.hacker_id
where s.score = d.score and c.difficulty_level = d.difficulty_level
group by h.hacker_id, h.name
having count(s.hacker_id) > 1
order by count(s.hacker_id) desc, s.hacker_id asc

/*
Ollivander's Inventory
https://www.hackerrank.com/challenges/harry-potter-and-wands/problem
*/
select w.id, wp.age, w.coins_needed, w.power
from wands w
inner join wands_property wp
on w.code = wp.code
where wp.is_evil = 0
and w.coins_needed = (
    select min(coins_needed) 
    from wands w1 
    inner join wands_property wp1 
    on w1.code = wp1.code
    where w1.power = w.power
    and wp1.age = wp.age)
order by w.power desc, wp.age desc

/*
Challenges
https://www.hackerrank.com/challenges/challenges/
*/
select H.hacker_id, H.name, count(*) as total
from Hackers H, Challenges C
where H.hacker_id = C.hacker_id
group by H.hacker_id, H.name
having total = 
    (select count(*) 
     from challenges
     group by hacker_id 
     order by count(*) desc limit 1
     )
or total in
    (select total
     from (
        select count(*) as total
        from Hackers H, Challenges C
        where H.hacker_id = C.hacker_id
        group by H.hacker_id, H.name
      ) counts
     group by total
     having count(*) = 1)
order by total desc, H.hacker_id asc
;

/*
Contest Leaderboard
https://www.hackerrank.com/challenges/contest-leaderboard/
*/
select h.hacker_id, h.name, SUM(s.max_score) total_score
from hackers h
inner join (
select hacker_id, challenge_id, max(score) max_score
from submissions
group by hacker_id, challenge_id
) s
on h.hacker_id = s.hacker_id
group by h.hacker_id, h.name
having sum(s.max_score) > 0
order by total_score desc, hacker_id

/*
Interviews
https://www.hackerrank.com/challenges/interviews/
*/
select con.contest_id, con.hacker_id, con.name,
       sum(ss.ts) ts, sum(ss.tas) tas,
       sum(vs.tv) tv, sum(vs.tuv) tuv
from contests con
inner join colleges col
on con.contest_id = col.contest_id
inner join challenges cha
on col.college_id = cha.college_id
left join (
    select challenge_id, sum(total_views) tv, sum(total_unique_views) tuv
    from view_stats
    group by challenge_id
) vs
on cha.challenge_id = vs.challenge_id
left join (
    select challenge_id, sum(total_submissions) ts, sum(total_accepted_submissions) tas
    from submission_stats
    group by challenge_id
) ss
on cha.challenge_id = ss.challenge_id
group by con.contest_id, con.hacker_id, con.name
having sum(ss.ts) != 0 or
       sum(ss.tas) != 0 or
       sum(vs.tv) != 0 or
       sum(vs.tuv) != 0
order by contest_id;
