import mysql.connector


legodb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1234",
    database="LegoStoreDatabase"
)

mycursor = legodb.cursor()

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