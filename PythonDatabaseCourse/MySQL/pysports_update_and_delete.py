import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "admin",
    password = "ropedi@4",
    database = "pysports"
)

mycursor = mydb.cursor() #create cursor

mycursor.execute("INSERT INTO player (first_name, last_name, team_id) VALUES ('Smeagol', 'Shire Fork', 1); ") #insert new player
mydb.commit
mycursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id;") #inner join
players = mycursor.fetchall()

print("-- DISPLAYING PLAYERS AFTER INSERT --")

x = 0
for player in players:
    print("Player ID: {}".format(players[x][0]))
    print("First Name: {}".format(players[x][1]))
    print("Last Name: {}".format(players[x][2]))
    print("Team Name: {}".format(players[x][3]))
    print(" ")
    x += 1

mycursor.execute("UPDATE player SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol'; ") #update record
mydb.commit()
mycursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id;") #inner join
players = mycursor.fetchall()

print("-- DISPLAYING PLAYERS AFTER UPDATE --")

x = 0
for player in players:
    print("Player ID: {}".format(players[x][0]))
    print("First Name: {}".format(players[x][1]))
    print("Last Name: {}".format(players[x][2]))
    print("Team Name: {}".format(players[x][3]))
    print(" ")
    x += 1

mycursor.execute("DELETE FROM player WHERE first_name = 'Gollum';") #delete record
mydb.commit()
mycursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id;") #inner join
players = mycursor.fetchall()

print("-- DISPLAYING PLAYERS AFTER DELETE --")

x = 0
for player in players:
    print("Player ID: {}".format(players[x][0]))
    print("First Name: {}".format(players[x][1]))
    print("Last Name: {}".format(players[x][2]))
    print("Team Name: {}".format(players[x][3]))
    print(" ")
    x += 1