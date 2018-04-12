use miscellaneous_db;

select p.*, m.*
from matches as m
inner join players as p on p.player_id = m.loser_id;
-- group by player_id
-- order by count(*) desc;