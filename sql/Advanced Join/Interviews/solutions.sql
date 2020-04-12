select ct.contest_id, ct.hacker_id, ct.name, 
       sum(total_submissions.total_submissions), 
       sum(total_submissions.total_accepted_submissions),
       sum(total_views.total_views), 
       sum(total_views.total_unique_views)
from contests ct
inner join colleges cl on ct.contest_id = cl.contest_id
inner join challenges ch on ch.college_id = cl.college_id
left join (select challenge_id, 
                  sum(total_views) as total_views, 
                  sum(total_unique_views) as total_unique_views
           from view_stats
           group by challenge_id) total_views on total_views.challenge_id = ch.challenge_id
left join (select challenge_id, 
                  sum(total_submissions) as total_submissions, 
                  sum(total_accepted_submissions) as total_accepted_submissions
           from submission_stats
           group by challenge_id) total_submissions on total_submissions.challenge_id = ch.challenge_id
group by ct.contest_id, ct.hacker_id, ct.name
having sum(total_submissions.total_submissions) != 0 or
       sum(total_submissions.total_accepted_submissions) != 0 or
       sum(total_views.total_views) != 0 or
       sum(total_views.total_unique_views) != 0
order by ct.contest_id;