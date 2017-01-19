-- Table definitions for the tournament project.
drop database [if exists] tournament;
create database tournament;
    \c tournament
    create table players (player_id serial primary key,
    	                  player_name text);
    create table matches (player_id integer references players(player_id),
    	                  match_num integer,
    	                  result integer,
    	                  primary key(player_id, match_num));
    create view standings as select players.player_id, players.player_name,
    	                  count((select matches.result where matches.result = 1)) as wins,
    	                  count(matches.match_num) as matches 
    	                  from players left join matches on players.player_id = matches.player_id
    	                  group by players.player_id
    	                  order by wins desc; 

 