select b.N, 
    case when P is NULL then 'Root'
         when (select count(P) 
               from BST 
               where b.N in (select P from BST)) > 0 then 'Inner'
         else 'Leaf'
    end
from BST b
order by N;