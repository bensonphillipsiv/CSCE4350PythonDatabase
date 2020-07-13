import mysql.connector

legodb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "1234"   
)

mycursor = legodb.cursor()
mycursor.execute("DROP DATABASE LegoStoreDatabase")

mycursor.execute("CREATE DATABASE LegoStoreDatabase")

legodb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "1234",
    database = "LegoStoreDatabase"   
)

mycursor = legodb.cursor()

#creating the customer table
mycursor.execute("CREATE TABLE Persons (ID int NOT NULL, LastName varchar(255) NOT NULL, FirstName varchar(255), Age int, PRIMARY KEY (ID))")


