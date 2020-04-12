--- Oracle mode ----
select t.city, t.len
from 
(select distinct city, 
        length(city) as len, 
        row_number() over (partition by length(city) order by length(city), city) as rn
 from station
 where length(city) = (select min(length(city)) from station) or 
       length(city) = (select max(length(city)) from station)) t
where rn = 1;

--- MySQL mode ---
select distinct city, length(city)
from station
where length(city) = (select min(length(city)) from station) or 
      length(city) = (select max(length(city)) from station)
order by length(city) desc, city
limit 2;