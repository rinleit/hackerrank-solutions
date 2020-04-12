--- MySQL mode ---
select distinct city
from station
where left(city, 1) in ('a', 'e', 'i', 'o', 'u');

--- Oracle mode ---
select distinct city
from station
where substr(city, 1, 1) in ('a', 'e', 'i', 'o', 'u');