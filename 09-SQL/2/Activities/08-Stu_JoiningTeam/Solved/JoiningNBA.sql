SELECT players.player, players.height, players.weight, players.collage, players.born, seasons_stats.pos, seasons_stats.tm
FROM players
INNER JOIN seasons_stats ON
players.player = seasons_stats.player;

SELECT players.player, seasons_stats.year, seasons_stats.pos,`seasons_stats`.`2P%`,
`seasons_stats`.`FG%`, `seasons_stats`.`FT%`, `seasons_stats`.`TS%`
FROM seasons_stats
INNER JOIN players ON
players.player = seasons_stats.player;