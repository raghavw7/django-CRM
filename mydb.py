import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'rootpass'
)


cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE elderco")

print("Databse Done!")