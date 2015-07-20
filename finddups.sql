select title, dtp, count(*)
from Reddit
group by title, dtp
having count(*) > 1