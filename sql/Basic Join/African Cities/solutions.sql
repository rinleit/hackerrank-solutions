select ci.name
from city ci
    left join country co on co.code = ci.countrycode
where co.continent = 'Africa';