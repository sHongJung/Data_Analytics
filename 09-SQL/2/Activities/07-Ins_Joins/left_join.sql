use miscellaneous_db;

select p.*, s.*
from players as p
left join seasons_stats as s on p.Player = s.Player;