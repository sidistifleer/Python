import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "toor",
    database = "ms-shop"
)
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM users")

nyrseult = mycursor.fetchall()

for x in nyrseult:
    print(x)