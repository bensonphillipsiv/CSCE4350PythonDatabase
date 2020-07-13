import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1234"
)

print(mydb)  

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE testdb")