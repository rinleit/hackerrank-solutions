--- Oracle ---
select rpad('*', level*2, ' *') as num_star
from dual connect by level <= 20;