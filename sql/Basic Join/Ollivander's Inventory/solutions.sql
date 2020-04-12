-- Oracle mode --
SELECT T.id, T.age, T.coins_needed, T.power 
from 
    (SELECT w1.id as id, age, coins_needed, power,
    row_number() OVER(PARTITION BY age, power ORDER BY coins_needed asc) as rn
    FROM wands w1 inner join wands_property w2 on w1.code = w2.code and w2.is_evil = 0) T
-- find min coins_needed -- 
where T.rn = 1
order by power desc, age desc;