import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "admin",
    password = "ropedi@4",
    database = "pysports"
)

mycursor = mydb.cursor() #create cursor

mycursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id;")
players = mycursor.fetchall()

print("-- DISPLAYING PLAYER RECORDS --")

x = 0
for player in players:
    print("Player ID: {}".format(players[x][0]))
    print("First Name: {}".format(players[x][1]))
    print("Last Name: {}".format(players[x][2]))
    print("Team Name: {}".format(players[x][3]))
    print(" ")
    x += 1
