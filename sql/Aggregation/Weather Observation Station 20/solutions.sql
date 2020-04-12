/* --- Oracle --- */
select round(lat_n, 4)
from 
(select lat_n, row_number() over (order by lat_n asc) as rn
 from station)
where rn > round((select count(*) from station)/2 - 1) and
      rn < round((select count(*) from station)/2 + 1);