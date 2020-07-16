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
def columnCheck(db_table, db_column, db_item):
    #print("Checking db_item: ", db_item)
    sqlFormula = "SELECT EXISTS(SELECT * from " +db_table+" WHERE( " +db_column+ "='"+db_item+"'))"
    
    #print(sqlFormula)
    mycursor.execute(sqlFormula)
     
    check = mycursor.fetchone()
    #legodb.commit()
    
    return check[0] 


def addNewCustomer(customer_name, customer_phone, customer_address, customer_email, customer_password):

    # this function will add a user to the database
    sqlformula = "INSERT INTO Customers(customer_name, customer_phone, customer_address, customer_email, customer_password) VALUES(%s, %s, %s, %s, %s)"
    newcustomer = (customer_name, customer_phone, customer_address, customer_email, customer_password)
    mycursor.execute(sqlformula, newcustomer)
    legodb.commit()



def checkItems(store_number, part_number_list, list_amounts):
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