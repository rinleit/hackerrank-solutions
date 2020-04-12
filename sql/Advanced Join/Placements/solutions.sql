select s.name
from students s
    inner join friends f on f.id = s.id
    inner join packages p1 on p1.id = s.id
    inner join packages p2 on p2.id = f.friend_id
where p2.salary > p1.salary
order by p2.salary;