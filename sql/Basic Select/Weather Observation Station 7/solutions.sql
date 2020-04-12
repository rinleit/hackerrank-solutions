--- MySQL mode ---
select distinct city
from station
where right(city, 1) in ('a', 'e', 'i', 'o', 'u');

--- Oracle mode ---
select distinct city
from station
where substr(city, -1, length(city)) in ('a', 'e', 'i', 'o', 'u');