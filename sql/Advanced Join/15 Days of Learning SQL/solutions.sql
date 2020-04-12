/* Oracle mode */
select s1.submission_date, s2.hacker_cnt, h.hacker_id, h.name
from Hackers h
left join
    (select submission_date, 
           hacker_id, 
           count(*),
           row_number() over (partition by submission_date order by count(*) desc, hacker_id asc) as row_num
    from submissions
    group by submission_date, hacker_id) s1 on (s1.hacker_id = h.hacker_id and s1.row_num = 1)
inner join 
    (select submission_date, count(distinct hacker_id) as hacker_cnt
    from (select s.*, 
          dense_rank() over (order by submission_date) as date_rank,
          dense_rank() over (partition by hacker_id order by submission_date) as hacker_rank
          from submissions s) 
    where date_rank = hacker_rank
    group by submission_date) s2 on (s2.submission_date = s1.submission_date)
order by submission_date;