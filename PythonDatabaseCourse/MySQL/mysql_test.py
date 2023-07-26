import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "admin",
    password = "ropedi@4",
    database = "pysports"
)

mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")

print('printing databases...')
for x in mycursor:
    print(x)

print('\n')

print('printing tables...')
mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)