import mysql.connector

legodb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1234"
)

mycursor = legodb.cursor()
# mycursor.execute("DROP DATABASE LegoStoreDatabase")

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
    "customer_id INT, "
    "customer_password VARCHAR(255), "
    "customer_name VARCHAR(255), "
    "customer_phone INT, "
    "customer_address VARCHAR(255), "
    "customer_email INT(255), "
    "PRIMARY KEY (customer_id))"
)

# creating the Stores table
mycursor.execute(
    "CREATE TABLE Stores (store_id INT, "
    "store_name VARCHAR(255), "
    "store_type int, "
    "PRIMARY KEY (store_id))"
)

# creating the Employee table
mycursor.execute(
    "CREATE TABLE Employees (employee_id INT, "
    "employee_name VARCHAR(255), "
    "employee_password VARCHAR(255), "
    "store_id INT, "
    "employee_type INT, "
    "PRIMARY KEY (employee_id), "
    "FOREIGN KEY (store_id) REFERENCES Stores(store_id))"
)

# creating the BrickSet table
mycursor.execute(
    "CREATE TABLE BrickSets (brick_set_id INT, "
    "description VARCHAR(255), "
    "PRIMARY KEY (brick_set_id))"
)

# creating the Bricks Table
mycursor.execute(
    "CREATE TABLE Bricks ("
    "brick_id VARCHAR(255), "
    "brick_price INT, "
    "description VARCHAR(255), "
    "PRIMARY KEY (brick_id))"
)

# creating the Inventory Table
mycursor.execute(
    "CREATE TABLE Inventory ("
    "brick_id VARCHAR(255), "
    "store_id INT, "
    "inventory_quantity INT, "
    "FOREIGN KEY (store_id) REFERENCES Stores(store_id), "
    "FOREIGN KEY (brick_id) REFERENCES Bricks(brick_id))"
)

# creating the BrickSetItems table
mycursor.execute(
    "CREATE TABLE BrickSetItems ("
    "brick_set_id INT, "
    "brick_id VARCHAR(255), "
    "quantity INT, "
    "FOREIGN KEY (brick_id) REFERENCES Bricks(brick_id), "
    "FOREIGN KEY (brick_set_id) REFERENCES BrickSets(brick_set_id))"
)

# creating the Orders Table
mycursor.execute(
    "CREATE TABLE Orders ("
    "order_id INT, "
    "customer_id INT, "
    "employee_id INT, "
    "payment_method VARCHAR(255), "
    "delivery_date TIMESTAMP, "
    "order_date TIMESTAMP, "
    "PRIMARY KEY (order_id), "
    "FOREIGN KEY (customer_id) REFERENCES Customers(customer_id), "
    "FOREIGN KEY (employee_id) REFERENCES Employees(employee_id))"
)

# creating the OrderItems Table
mycursor.execute(
    "CREATE TABLE OrderItems ("
    "order_id INT, "
    "brick_id VARCHAR(255), "
    "brick_set_id INT, "
    "brick_quantity INT, "
    "brick_set_quantity INT, "
    "FOREIGN KEY (order_id) REFERENCES Orders(order_id), "
    "FOREIGN KEY (brick_id) REFERENCES Bricks(brick_id), "
    "FOREIGN KEY (brick_set_id) REFERENCES BrickSets(brick_set_id))"

)
