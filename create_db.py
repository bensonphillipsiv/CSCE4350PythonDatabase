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

#creating the Employee table
mycursor.execute(
    "CREATE TABLE Employees (employee_id INT, "
    "employee_name VARCHAR(255), "
    "employee_password VARCHAR(255), "
    "store_id INT, "
    "employee_type INT, "
    "PRIMARY KEY (employee_id))"
)

#creating the Stores table
mycursor.execute(
    "CREATE TABLE Stores (store_id INT, "
    "store_name VARCHAR(255), "
    "store_type int, "
    "PRIMARY KEY (store_id))"
)

#creating the BrickSetItems table
mycursor.execute(
    "CREATE TABLE BrickSetItems (brick_set_id INT, "
    "brick_id INT, "
    "quanity INT)"
)

#creating the BrickSet table
mycursor.execute(
    "CREATE TABLE BrickSet (brick_set_id INT, "
    "description VARCHAR(255), "
    "PRIMARY KEY (brick_set_id))"
)