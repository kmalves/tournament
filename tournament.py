#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def dbManager(query):
    conn = connect()
    c = conn.cursor()
    c.execute(query)
    conn.commit()
    conn.close()


def deleteMatches():
    """Remove all the match records from the database."""
    query = "delete from matches;"
    dbManager(query)


def deletePlayers():
    """Remove all the player records from the database."""
    query = "delete from players;"
    dbManager(query)


def countPlayers():
    """Returns the number of players currently registered."""
    conn = connect()
    c = conn.cursor()
    c.execute("select count(*) as num from players;")
    players = c.fetchone()
    conn.close()    
    return players[0]


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    conn = connect()
    c = conn.cursor()
    c.execute("insert into players (player_name) values (%s);", (name,))
    conn.commit()
    conn.close()
    


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    conn = connect()
    c = conn.cursor()
    c.execute("select * from standings;")
    standings = c.fetchall()
    conn.close()
    return standings


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    conn = connect()
    c = conn.cursor()
    c.execute("select matches from standings where player_id = %s;", (winner,))
    winner_prev_match = c.fetchone()[0]
    winner_current_match = winner_prev_match + 1
    c.execute("select matches from standings where player_id = %s;", (loser,))
    loser_prev_match = c.fetchone()[0]
    loser_current_match = loser_prev_match + 1
    c.execute("insert into matches (player_id, match_num, result) values (%s, %s, 1);", (winner, winner_current_match))
    conn.commit()  
    c.execute("insert into matches (player_id, match_num, result) values (%s, %s, 0);", (loser, loser_current_match))
    conn.commit() 
    conn.close()
 
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    conn = connect()
    c = conn.cursor()
    c.execute("select player_id, player_name from standings;")
    standings_names = c.fetchall()
    conn.close()
    pairngs_list = []
    while len(pairngs_list) < len(standings_names)/2:
        n = 0
        pairing = [standings_names[n][0], standings_names[n][1], standings_names[n+1][0], standings_names[n+1][1]]
        pairngs_list.append(tuple(pairing))
        n = n+2
    return pairngs_list       
