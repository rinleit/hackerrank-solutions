select A.hacker_id, A.name, A.challenges_created
from 
    (select h.hacker_id as hacker_id, h.name as name, count(1) as challenges_created
     from Hackers h left join Challenges c on (h.hacker_id = c.hacker_id)
     group by h.hacker_id, h.name) A
where A.challenges_created = (select max(count(1)) from Challenges group by hacker_id)
      or
      A.challenges_created in 
        (select B.challenges_created
         from (select count(1) as challenges_created from Challenges group by hacker_id) B
         group by B.challenges_created
         having count(B.challenges_created) = 1)
order by A.challenges_created desc, A.hacker_id;