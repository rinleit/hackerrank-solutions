select co.continent, floor(avg(ci.population))
from country co
inner join city ci on ci.countrycode = co.code
group by co.continent;