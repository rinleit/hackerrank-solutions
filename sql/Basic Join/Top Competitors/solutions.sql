-- Oracle mode --
select total.hacker_id, h.name
from Hackers h
inner join 
    (select s.hacker_id, count(s.hacker_id) as num_submit
     from submissions s
     inner join challenges c on c.challenge_id = s.challenge_id
     inner join difficulty d on (d.difficulty_level = c.difficulty_level and s.score = d.score)
     group by s.hacker_id) total on total.hacker_id = h.hacker_id
where total.num_submit > 1
order by num_submit desc, hacker_id asc;