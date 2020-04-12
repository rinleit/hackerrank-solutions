select sum(ci.population)
from city ci left join country co on co.code = ci.countrycode
where continent = 'Asia';