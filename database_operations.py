import mysql.connector


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


def searchItem(keyword):
    sqlFormula = "SELECT brick_id, brick_price, description FROM Bricks WHERE description LIKE '%" + keyword + "%'"
    mycursor.execute(sqlFormula)

    result = mycursor.fetchall()
    print(result)

    sqlFormula = "SELECT brick_set_id, description FROM BrickSets WHERE description LIKE '%" + keyword + "%'"
    mycursor.execute(sqlFormula)

    result = mycursor.fetchall()
    print(result)


def columnCheck(db_table, db_column, db_item):
    #print("Checking db_item: ", db_item)
    sqlFormula = "SELECT EXISTS(SELECT * from " +db_table+" WHERE( " +db_column+ "='"+db_item+"'))"
    
    #print(sqlFormula)
    mycursor.execute(sqlFormula)
     
    check = mycursor.fetchone()
    #legodb.commit()
    
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
            print ("Login Succesful!\n\n\n")
            return 1

        else:
            print ("\nUsername or Password Failed! Please Try Again.\n")
            return 0

    else:
        print ("\nUsername or Password Failed! Please Try Again.\n")
        return 0



    #return check[0] 
