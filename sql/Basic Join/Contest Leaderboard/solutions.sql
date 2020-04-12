-- Oracle mode --
select h.hacker_id, h.name, sum(max_score_t.score)
from Hackers h
    inner join
        (select distinct challenge_id, hacker_id, max(score) as score
         from Submissions
         group by challenge_id, hacker_id) max_score_t
    on (max_score_t.hacker_id = h.hacker_id)
group by h.hacker_id, h.name
having sum(max_score_t.score) > 0
order by sum(max_score_t.score) desc, h.hacker_id;