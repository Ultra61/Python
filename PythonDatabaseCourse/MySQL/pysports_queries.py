import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "admin",
    password = "ropedi@4",
    database = "pysports"
)

mycursor = mydb.cursor() #create cursor

mycursor.execute("SELECT team_id, team_name, mascot FROM team") #query for team table

print("-- DISPLAYING TEAM RECORDS --")
teams = mycursor.fetchall()
for team in teams:
    print("Team ID: {}".format(team[0]))
    print("Team Name: {}".format(team[1]))
    print("Mascot: {}".format(team[2]))
    print(" ")

print(" ")

mycursor.execute("SELECT player_id,first_name, last_name, team_id FROM player") #query for player table

print("-- DISPLAYING PLAYER RECORDS --")
players = mycursor.fetchall()
for player in players:
    print("Player ID: {}".format(player[0]))
    print("First Name: {}".format(player[1]))
    print("Last Name: {}".format(player[2]))
    print("Team ID: {}".format(player[3]))
    print(" ")