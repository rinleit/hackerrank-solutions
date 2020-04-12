----- use round() ---
select round(avg(salary) - avg(replace(salary, '0', '')) + 0.5)
from employees;
----- use ceil() ----
select ceil(avg(salary) - avg(replace(salary, '0', '')))
from employees;