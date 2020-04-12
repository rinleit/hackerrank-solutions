--- MySQL ---
SELECT REPEAT('* ', @NUMBER := @NUMBER - 1) 
FROM information_schema.tables, (SELECT @NUMBER:=21) t 
LIMIT 20

--- Oracle ---
select rpad('*', level*2, ' *') as num_star
from dual connect by level <= 20
order by length(num_star) desc;