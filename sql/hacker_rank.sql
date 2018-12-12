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

/* The PADS */
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

/* Occupations */
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