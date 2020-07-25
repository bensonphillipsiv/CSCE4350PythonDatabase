import mysql.connector

legodb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1234"
)

mycursor = legodb.cursor()
try:
     mycursor.execute("DROP DATABASE LegoStoreDatabase")
except:
    pass

mycursor.execute("CREATE DATABASE LegoStoreDatabase")

legodb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1234",
    database="LegoStoreDatabase"
)

mycursor = legodb.cursor()

# creating the Customer table
mycursor.execute(
    "CREATE TABLE Customers ("
    "customer_id INT AUTO_INCREMENT, "
    "customer_password VARCHAR(255), "
    "customer_name VARCHAR(255), "
    "customer_phone VARCHAR(255), "
    "customer_address VARCHAR(255), "
    "customer_email VARCHAR(255), "
    "customer_credit_card VARCHAR(255), "
    "PRIMARY KEY (customer_id))"
)

# creating the Stores table
mycursor.execute(
    "CREATE TABLE Stores ("
    "store_id VARCHAR(255), "
    "store_name VARCHAR(255), "
    "PRIMARY KEY (store_id))"
)

mycursor.execute("INSERT INTO Stores VALUES('newyork', 'newyork')")
mycursor.execute("INSERT INTO Stores VALUES('losangeles', 'losangeles')")
mycursor.execute("INSERT INTO Stores VALUES('online', 'online')")

# creating the Employee table
mycursor.execute(
    "CREATE TABLE Employees ("
    "employee_id INT AUTO_INCREMENT, "
    "employee_name VARCHAR(255), "
    "employee_type VARCHAR(255), "
    "store_id VARCHAR(255), "
    "employee_password VARCHAR(255), "
    "PRIMARY KEY (employee_id), "
    "FOREIGN KEY (store_id) REFERENCES Stores(store_id))"
)

mycursor.execute("INSERT INTO Employees(employee_name, employee_type, store_id, employee_password) VALUES('bob', 'salesman', 'newyork', 'password')")
mycursor.execute("INSERT INTO Employees(employee_name, employee_type, store_id, employee_password) VALUES('frank', 'salesman', 'losangeles', 'password')")


# creating the BrickSet table
mycursor.execute(
    "CREATE TABLE BrickSets ("
    "brick_set_id VARCHAR(255), "
    "description VARCHAR(255), "
    "PRIMARY KEY (brick_set_id))"
)

mycursor.execute("INSERT INTO BrickSets VALUES('12', 'yellow and blue brick')")
mycursor.execute("INSERT INTO BrickSets VALUES('23', 'blue and red brick')")
mycursor.execute("INSERT INTO BrickSets VALUES('345', 'red and green and blue brick')")
mycursor.execute("INSERT INTO BrickSets VALUES('25', 'blue and purple brick')")
mycursor.execute("INSERT INTO BrickSets VALUES('45', 'green and purple brick')")

# creating the Bricks Table
mycursor.execute(
    "CREATE TABLE Bricks ("
    "brick_id VARCHAR(255), "
    "brick_price INT, "
    "description VARCHAR(255), "
    "PRIMARY KEY (brick_id))"
)

mycursor.execute("INSERT INTO Bricks VALUES('1', '15', 'yellow brick')")
mycursor.execute("INSERT INTO Bricks VALUES('2', '12', 'blue brick')")
mycursor.execute("INSERT INTO Bricks VALUES('3', '30', 'red brick')")
mycursor.execute("INSERT INTO Bricks VALUES('4', '54', 'green brick')")
mycursor.execute("INSERT INTO Bricks VALUES('5', '7', 'purple brick')")


# creating the Inventory Table
mycursor.execute(
    "CREATE TABLE Inventory ("
    "brick_id VARCHAR(255), "
    "store_id VARCHAR(255), "
    "inventory_quantity INT, "
    "FOREIGN KEY (store_id) REFERENCES Stores(store_id), "
    "FOREIGN KEY (brick_id) REFERENCES Bricks(brick_id))"
)

mycursor.execute("INSERT INTO Inventory VALUES('1', 'newyork', '15')")
mycursor.execute("INSERT INTO Inventory VALUES('2', 'newyork', '15')")
mycursor.execute("INSERT INTO Inventory VALUES('3', 'newyork', '20')")
mycursor.execute("INSERT INTO Inventory VALUES('4', 'newyork', '5')")
mycursor.execute("INSERT INTO Inventory VALUES('5', 'newyork', '50')")

mycursor.execute("INSERT INTO Inventory VALUES('1', 'losangeles', '55')")
mycursor.execute("INSERT INTO Inventory VALUES('2', 'losangeles', '15')")
mycursor.execute("INSERT INTO Inventory VALUES('3', 'losangeles', '10')")
mycursor.execute("INSERT INTO Inventory VALUES('4', 'losangeles', '25')")
mycursor.execute("INSERT INTO Inventory VALUES('5', 'losangeles', '35')")

mycursor.execute("INSERT INTO Inventory VALUES('1', 'online', '45')")
mycursor.execute("INSERT INTO Inventory VALUES('2', 'online', '60')")
mycursor.execute("INSERT INTO Inventory VALUES('3', 'online', '100')")
mycursor.execute("INSERT INTO Inventory VALUES('4', 'online', '0')")
mycursor.execute("INSERT INTO Inventory VALUES('5', 'online', '25')")


# creating the BrickSetItems table
mycursor.execute(
    "CREATE TABLE BrickSetItems ("
    "brick_set_id VARCHAR(255), "
    "brick_id VARCHAR(255), "
    "quantity INT, "
    "FOREIGN KEY (brick_id) REFERENCES Bricks(brick_id), "
    "FOREIGN KEY (brick_set_id) REFERENCES BrickSets(brick_set_id))"
)


mycursor.execute("INSERT INTO BrickSetItems VALUES('12', '1', '2')")
mycursor.execute("INSERT INTO BrickSetItems VALUES('12', '2', '3')")

mycursor.execute("INSERT INTO BrickSetItems VALUES('23', '2', '1')")
mycursor.execute("INSERT INTO BrickSetItems VALUES('23', '3', '5')")

mycursor.execute("INSERT INTO BrickSetItems VALUES('345', '3', '1')")
mycursor.execute("INSERT INTO BrickSetItems VALUES('345', '4', '4')")
mycursor.execute("INSERT INTO BrickSetItems VALUES('345', '5', '2')")

mycursor.execute("INSERT INTO BrickSetItems VALUES('25', '2', '1')")
mycursor.execute("INSERT INTO BrickSetItems VALUES('25', '5', '6')")

mycursor.execute("INSERT INTO BrickSetItems VALUES('45', '4', '3')")
mycursor.execute("INSERT INTO BrickSetItems VALUES('45', '5', '4')")


# creating the Orders Table
mycursor.execute(
    "CREATE TABLE Orders ("
    "order_id INT AUTO_INCREMENT, "
    "store_id VARCHAR(255)," 
    "customer_id INT, "
    "employee_id INT, "
    "payment_method VARCHAR(255), "
    "delivery_date TIMESTAMP, "
    "order_date TIMESTAMP, "
    "PRIMARY KEY (order_id), "
    "FOREIGN KEY (store_id) REFERENCES Stores(store_id), "
    "FOREIGN KEY (customer_id) REFERENCES Customers(customer_id), "
    "FOREIGN KEY (employee_id) REFERENCES Employees(employee_id))"
)

mycursor.execute("INSERT INTO Orders(store_id, employee_id, payment_method) VALUES('newyork', '1', 'cash')")
mycursor.execute("INSERT INTO Orders(store_id, employee_id, payment_method) VALUES('losangeles', '2', 'card')")

# creating the OrderItems Table
mycursor.execute(
    "CREATE TABLE OrderItems ("
    "order_id INT, "
    "brick_id VARCHAR(255), "
    "brick_set_id VARCHAR(255), "
    "brick_quantity INT, "
    "brick_set_quantity INT, "
    "FOREIGN KEY (order_id) REFERENCES Orders(order_id), "
    "FOREIGN KEY (brick_id) REFERENCES Bricks(brick_id), "
    "FOREIGN KEY (brick_set_id) REFERENCES BrickSets(brick_set_id))"
)

mycursor.execute("INSERT INTO OrderItems(order_id, brick_id, brick_quantity) VALUES('1', '1', '5')")
mycursor.execute("INSERT INTO OrderItems(order_id, brick_id, brick_quantity) VALUES('2', '1', '100')")

# creating the report table
mycursor.execute(
    "CREATE TABLE Reports ("
    "report_id INT NOT NULL AUTO_INCREMENT, "
    "report_time DATETIME NULL, "
    "employee_id INT, "
    "store_id VARCHAR(255), "
    "time_in_out DATETIME NULL, "
    "type ENUM('in', 'out') NULL, "
    "time_difference int, "
    "customer_order INT, "
    "FOREIGN KEY (employee_id) REFERENCES Employees(employee_id), "
    "FOREIGN KEY (store_id) REFERENCES Stores(store_id), "
    "PRIMARY KEY (report_id))"
)

mycursor.execute("INSERT INTO reports(report_id, employee_id, store_id, time_in_out,type) VALUES('1', '1', 'newyork', '2020-07-24 00:09:00', 'in')")

legodb.commit()