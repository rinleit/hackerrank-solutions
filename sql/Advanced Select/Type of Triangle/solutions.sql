-- MySQL --
select 
 case when a + b > c then
     case
        when a = b and b = c then 'Equilateral'
        when a = b or b = c or a = c then 'Isosceles'
        when a != b or b != c or a != c then 'Scalene'
     end
 else 'Not A Triangle'
 end
from triangles;