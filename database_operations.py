import mysql.connector
import math

legodb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1234",
    database="LegoStoreDatabase"
)
mycursor = legodb.cursor()

#This function will check if your data base has a single item already inserted in the column
#for example if you want to verify that an email isnt already in the system run
#email_check = database_operations.columnCheck("Customers", "customer_email", "hellokitty@gmail.com")
#
#This function will run an SQL command that looks like so...
#SELECT EXISTS(SELECT * from Customers WHERE (customer_email = hellokitty@gmail.com))
#if hellokitty@gmail exists in the Customers table under the customer_email column then it will return a 1 for TRUE or a 0 for FALSE
#True = It exists
#False = It does not exist


def searchItem(keyword, store_id):

    print("Items from " + store_id + " store:\n")
    sqlFormula = "SELECT Bricks.brick_id, Bricks.brick_price, Inventory.inventory_quantity, Bricks.description FROM Bricks INNER JOIN Inventory ON Bricks.brick_id = Inventory.brick_id WHERE description LIKE '%" + keyword + "%' AND store_id = '" + store_id + "'"
    mycursor.execute(sqlFormula)

    result = mycursor.fetchall()
    print("Bricks:")

    for x in result:
        print("Brick ID: " + x[0] + "\t\tPrice: " + str(x[1]) + "\t\tStock: " + str(x[2]) + "\t\tDescription: " + x[3])

    # calculating the price of the brick sets based on the individual bricks
    sqlFormula = "SELECT BrickSetItems.brick_set_id, Bricks.brick_id, Bricks.brick_price, BrickSetItems.quantity FROM BrickSetItems INNER JOIN Bricks ON BrickSetItems.brick_id = Bricks.brick_id"
    mycursor.execute(sqlFormula)
    result = mycursor.fetchall()

    set_prices = {}
    for item in result:
        if item[0] not in set_prices:
            price = 0
            for item2 in result:
                if item[0] == item2[0]:
                    price += item2[2] * item2[3]

            set_prices[item[0]] = price

    # calculating the current inventory of brick sets based on current stock of bricks in the store
    sqlFormula = "SELECT BrickSets.brick_set_id, Inventory.brick_id, quantity, inventory_quantity, BrickSets.description FROM BrickSets INNER JOIN BrickSetItems ON BrickSets.brick_set_id = BrickSetItems.brick_set_id INNER JOIN Inventory ON Inventory.brick_id = BrickSetItems.brick_id WHERE store_id = '" + store_id + "'"
    mycursor.execute(sqlFormula)
    result = mycursor.fetchall()

    set_stocks = {}
    for item in result:
        if item[0] not in set_stocks:
            max_stock = math.floor(item[3]/item[2])
            for item2 in result:
                if item[0] == item2[0]:
                    stock = math.floor(item2[3]/item2[2])
                    if stock < max_stock:
                        max_stock = stock

            set_stocks[item[0]] = max_stock

    # joining all the brick data together
    sqlFormula = "SELECT BrickSets.brick_set_id, BrickSets.description FROM BrickSets WHERE description LIKE '%" + keyword + "%'"
    mycursor.execute(sqlFormula)
    result = mycursor.fetchall()

    print("\nBrick Sets:")
    for x in result:
        price = set_prices.get(x[0])
        stock = set_stocks.get(x[0])
        print("BrickSet ID: " + x[0] + "\t\tPrice: " + str(price) + "\t\tStock: " + str(stock) + "\t\tDescription: " + x[1])


def columnCheck(db_table, db_column, db_item):
    #print("Checking db_item: ", db_item)
    sqlFormula = "SELECT EXISTS(SELECT * from " + db_table + " WHERE( " + db_column + "='" + db_item + "'))"
    
    #print(sqlFormula)
    mycursor.execute(sqlFormula)
     
    check = mycursor.fetchone()
    #legodb.commit()
    
    return check[0] 

def employee_rank_check(db_table, db_column, db_item):
    #print("Checking db_item: ", db_item)
    sqlFormula = "SELECT employee_type from " +db_table+" WHERE( " +db_column+ "='"+db_item+"')"
    
    #print(sqlFormula)
    mycursor.execute(sqlFormula)
    
    check = mycursor.fetchone()
    #print(check) 
    return check[0]


def addNewCustomer(customer_name, customer_phone, customer_address, customer_email, customer_password, customer_card):
    # this function will add a user to the database
    sqlformula = "INSERT INTO Customers(customer_name, customer_phone, customer_address, customer_email, customer_password, customer_credit_card) VALUES(%s, %s, %s, %s, %s, %s)"
    newcustomer = (customer_name, customer_phone, customer_address, customer_email, customer_password, customer_card)
    mycursor.execute(sqlformula, newcustomer)
    legodb.commit()


def addNewEmployee(employee_name, employee_type, employee_store, employee_password):
    # this function will add a user to the database
    sqlformula = "INSERT INTO Employees(employee_name, employee_type, store_id, employee_password) VALUES(%s, %s, %s, %s)"
    newemployee = (employee_name, employee_type, employee_store, employee_password)
    
    mycursor.execute(sqlformula, newemployee)
    legodb.commit()


def checkItems(store_id, part_number_list, list_amounts):
    for i in range(len(part_number_list)):
        # check each part number in the store_number provided
        part_number_list[i]
        list_amounts[i]

        items = True
        if items:
            return True
        else:
            return False


def updateItems(store_number, part_number_list, list_amounts, val):
    if val == -1:
        # subtract amounts from database to update
        print("Updated Database")
    elif val == 1:
        # add amounts from database to update
        print("Updated Database")
    else:
        print("error adding or subtracting to update DB")


#this function will verify password and login, will return a 1 for login and 0 for failure
def loginAuth(email, password, db_table, db_column, password_cat):

    email_check = columnCheck(db_table, db_column, email)
    
    # this will verify whether the email exists in the database
    if (email_check == 1):
        sqlFormula = "SELECT " +password_cat+" FROM " +db_table+ " WHERE " +db_column+ " = '" + email+ "'"
        mycursor.execute(sqlFormula)
        check = mycursor.fetchone()
        check_string = str(check[0])
        password_string = str(password)
        
        # this will verify whether the submitted password matches the one the pertaining to the account
        if (check_string == password_string):
            print("Login Succesful!\n\n\n")
            return 1

        else:
            print ("\nUsername or Password Failed! Please Try Again.\n")
            return 0

    else:
        print ("\nUsername or Password Failed! Please Try Again.\n")
        return 0

