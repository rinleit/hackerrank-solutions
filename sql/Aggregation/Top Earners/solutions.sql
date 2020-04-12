select (months * salary), count(*)
from Employee
where (months * salary) = (select max(months * salary) from Employee)
group by (months * salary);