--- Oracle ---
select
 min(case when occupation = 'Doctor' then COALESCE(name, NULL) end),
 min(case when occupation = 'Professor' then COALESCE(name, NULL) end),
 min(case when occupation = 'Singer' then COALESCE(name, NULL) end),
 min(case when occupation = 'Actor' then COALESCE(name, NULL) end)
from (select name, 
             occupation,
             row_number() over (partition by occupation order by name) as rn
       from occupations)
group by rn
order by rn;
