Project Specification:

Develop a database schema to store details of Swiss tournament matches between players.
Write a Python module to rank the players and pair them up in matches in a tournament.

Files:

tournament.py

Contains the implementation for the Swiss tournament

tournament.sql

Contains the SQL queries to create the database, tables and views

tournament_test.py

Contains the test cases for tournament.py

Prerequisites:

The latest vagrant build for the Udacity tournament project 
https://docs.google.com/document/d/16IgOm4XprTaKxAa8w02y028oBECOoB1EI1ReddADEeY/pub?embedded=true

Instructions:

Start Vagrant
Open Terminal or cmd and browse to the vagrant folder
Type vagrant up (powers on the virtual machine)
In the same terminal type vagrant ssh (logs into the virtual machine)
Change to the correct folder - type cd /vagrant/tournament
Open PSQL and run the tournament.sql to create the database
Type \q to exit PSQL 
In the terminal type python tournament_test.py to run the tests

Expected Outcome:

Success! All tests pass!
vagrant@vagrant-ubuntu-trusty-32:/vagrant/tournament$ python tournament_test.py
1. Old matches can be deleted.
2. Player records can be deleted.
3. After deleting, countPlayers() returns zero.
4. After registering a player, countPlayers() returns 1.
5. Players can be registered and deleted.
6. Newly registered players appear in the standings with no matches.
7. After a match, players have updated standings.
8. After one match, players with one win are paired.
Success! All tests pass!
