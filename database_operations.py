import mysql.connector
import math
import store_menu


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
    sqlFormula = "SELECT employee_type from " +db_table+" WHERE( " +db_column+ "='"+db_item+"')"

    mycursor.execute(sqlFormula)

    check = mycursor.fetchone()
    return check[0]


def addStore(store_id):
    sqlformula = "INSERT INTO Stores VALUES('" + store_id + "', '" + store_id + "')"
    mycursor.execute(sqlformula)
    legodb.commit()

    print("**Store Added**")


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

    sqlFormula2 = "SELECT max(employee_id) from employees"

    mycursor.execute(sqlFormula2)

    check = mycursor.fetchone()
    return check[0]


def checkStore(employee_id):
    # check what store an employee is at
    sqlFormula = "SELECT store_id FROM employees WHERE employee_id = " + employee_id
    mycursor.execute(sqlFormula)
    result = mycursor.fetchone()

    return result[0]


def checkItems(store_id, part_number_list, list_amounts):
    # checking the current inventory of brick sets
    sqlFormula = "SELECT brick_id, inventory_quantity FROM Inventory WHERE store_id = '" + store_id + "'"
    mycursor.execute(sqlFormula)
    result = mycursor.fetchall()

    for i in range(len(part_number_list)):
        for brick in result:
            if part_number_list[i] == brick[0]:
                if int(list_amounts[i]) > brick[1]:
                    print("**Items not in Stock**")
                    return False

    # calculating the current inventory of brick sets based on current stock of bricks in the store
    sqlFormula = "SELECT BrickSets.brick_set_id, Inventory.brick_id, quantity, inventory_quantity, BrickSets.description FROM BrickSets INNER JOIN BrickSetItems ON BrickSets.brick_set_id = BrickSetItems.brick_set_id INNER JOIN Inventory ON Inventory.brick_id = BrickSetItems.brick_id WHERE store_id = '" + store_id + "'"
    mycursor.execute(sqlFormula)
    result = mycursor.fetchall()

    set_stocks = {}
    for item in result:
        if item[0] not in set_stocks:
            max_stock = math.floor(item[3] / item[2])
            for item2 in result:
                if item[0] == item2[0]:
                    stock = math.floor(item2[3] / item2[2])
                    if stock < max_stock:
                        max_stock = stock

            set_stocks[item[0]] = max_stock

    for i in range(len(part_number_list)):
        if part_number_list[i] in set_stocks:
            if int(list_amounts[i]) > set_stocks.get(part_number_list[i]):
                print("**Items not in Stock**")
                return False

    print("**Items in Stock**")
    return True


def updateItems(store_id, part_number_list, list_amounts, val):
    new_part_number_list = []
    new_list_amounts = []

    # checking the current inventory of brick sets
    sqlFormula = "SELECT brick_id, inventory_quantity FROM Inventory WHERE store_id = '" + store_id + "'"
    mycursor.execute(sqlFormula)
    result = mycursor.fetchall()

    # adding the singular bricks to a list
    for k in range(len(part_number_list)):
        for brick in result:
            if part_number_list[k] == brick[0]:
                new_part_number_list.append(part_number_list[k])
                new_list_amounts.append(list_amounts[k])

    # calculating brick amounts for brick set
    sqlFormula = "SELECT brick_set_id, brick_id, quantity FROM BrickSetItems"
    mycursor.execute(sqlFormula)
    result = mycursor.fetchall()

    for i in range(len(part_number_list)):
        for brickset in result:
            if part_number_list[i] == brickset[0]:
                if brickset[1] in new_part_number_list:
                    add = int(list_amounts[i]) * brickset[2]
                    index2 = new_part_number_list.index(brickset[1])
                    new_list_amounts[index2] = str(int(new_list_amounts[index2]) + add)
                else:
                    new_part_number_list.append(brickset[1])
                    add = int(list_amounts[i]) * brickset[2]
                    new_list_amounts.append(str(add))

    for j in range(len(new_part_number_list)):
        if val == -1:
            sqlFormula = "UPDATE Inventory SET inventory_quantity = inventory_quantity - " + new_list_amounts[j] + " WHERE brick_id = '" + new_part_number_list[j] + "'"
        else:
            sqlFormula = "UPDATE Inventory SET inventory_quantity = inventory_quantity + " + new_list_amounts[j] + " WHERE brick_id = '" + new_part_number_list[j] + "'"
        mycursor.execute(sqlFormula)
        legodb.commit()

    print("Updated Database")


def orderUpdate(store_id, global_employee_id, payment_type, part_number_list, list_amounts):
    # adding order details to order management
    sqlFormula = "INSERT INTO Orders(store_id, employee_id, payment_method) VALUES('" + store_id + "', " + global_employee_id + ", '" + payment_type + "')"
    mycursor.execute(sqlFormula)
    legodb.commit()

    brick_id = []
    brick_amount = []
    brick_set_id = []
    brick_set_amount = []

    # checking the current inventory of bricks
    sqlFormula = "SELECT brick_id FROM Bricks"
    mycursor.execute(sqlFormula)
    result = mycursor.fetchall()

    # adding the singular bricks to a list
    for k in range(len(part_number_list)):
        for brick in result:
            if part_number_list[k] == brick[0]:
                brick_id.append(part_number_list[k])
                brick_amount.append(list_amounts[k])

    # checking the current inventory of brick sets
    sqlFormula = "SELECT brick_set_id FROM BrickSets"
    mycursor.execute(sqlFormula)
    result = mycursor.fetchall()

    # adding the singular bricks to a list
    for j in range(len(part_number_list)):
        for brick in result:
            if part_number_list[j] == brick[0]:
                brick_set_id.append(part_number_list[j])
                brick_set_amount.append(list_amounts[j])

    sqlFormula = "SELECT order_id FROM Orders WHERE order_id = (SELECT LAST_INSERT_ID())"
    mycursor.execute(sqlFormula)
    result = mycursor.fetchone()

    order_id = result[0]
    print(order_id)

    for i in range(len(brick_id)):
        sqlFormula = "INSERT INTO OrderItems(order_id, brick_id, brick_quantity) VALUES(" + str(order_id) + ", " + brick_id[i] + ", " + str(brick_amount[i]) + ")"
        mycursor.execute(sqlFormula)
        legodb.commit()

    for l in range(len(brick_set_id)):
        sqlFormula = "INSERT INTO OrderItems(order_id, brick_set_id, brick_set_quantity) VALUES(" + str(order_id) + ", " + brick_set_id[l] + ", " + str(brick_set_amount[l]) + ")"
        mycursor.execute(sqlFormula)
        legodb.commit()

    print("**Recorded Order**")


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


#this function will either clock someone in or out and calculate hours worked per shift.
def clock_in_out(employee_id, clock_type, store_id):

    if (clock_type == "in"):
        # this function will clock a user in
        sqlformula = "INSERT INTO Reports(employee_id, time_in_out, type, store_id) VALUES(%s, now(), %s, '" + store_id + "')"
        newcustomer = (employee_id, clock_type)
        mycursor.execute(sqlformula, newcustomer)
        legodb.commit()
    elif (clock_type == "out"):
        # this function will find the latest time an employee has clocked in and calculate time in last shift cycle

        string_employee_id = str(employee_id)
        sqlformula1="SELECT time_in_out FROM reports WHERE (time_in_out in (select max(time_in_out) from reports GROUP BY employee_id) AND employee_id = '" + string_employee_id +"')"
        insert = (employee_id)
        mycursor.execute(sqlformula1)
        j = mycursor.fetchone()
        latest_time = j[0]
        #print("Clocked in at: ", latest_time)

        string_latest_time = str(latest_time)
        #print(string_latest_time)

        sqlformula2 = "Select timestampdiff(MINUTE, '"+ string_latest_time +"', now())"


        mycursor.execute(sqlformula2)
        k = mycursor.fetchone()
        time_diff = k[0]
        string_time_diff = str(time_diff)

        sqlformula = "INSERT INTO Reports(employee_id, time_in_out, type, time_difference, store_id) VALUES(%s, now(), %s, '" + string_time_diff + "', '" + store_id + "')"
        newcustomer = (employee_id, clock_type)
        mycursor.execute(sqlformula, newcustomer)
        legodb.commit()


#this will print a report for the individual employee   
def indEmployeeReport(period, employee_id):
    ei="Employee ID"
    si="Store ID"
    tio= "Time"
    cio= "Clock In/Out"
    td= "Shift Lenght(min)"
    cd= "Orders Completed"

    if (period == "daily"):
        sqlformula1 = "Select * from reports where (time_in_out between date_add(now(), interval -1 day) and now())  AND employee_id = '"+ employee_id +"'"
        mycursor.execute(sqlformula1)
        check = mycursor.fetchall()
        print("|", 
                ei, " "*(20-len(ei)), "|",
                si, " "*(20-len(si)), "|",
                tio, " "*(20-len(tio)), "|",
                cio, " "*(20-len(cio)), "|",
                td, " "*(20-len(td)), "|",
                cd, " "*(20-len(cd)), "|")
        for item in check:
            print("|", 
                item[2], " "*(20-len(str(item[2]))), "|",
                item[3], " "*(20-len(str(item[3]))), "|",
                item[4], " "*(20-len(str(item[4]))), "|",
                item[5], " "*(20-len(str(item[5]))), "|",
                item[6], " "*(20-len(str(item[6]))), "|",
                item[7], " "*(20-len(str(item[7]))), "|") 


        # this function will return hours worked by employee and other information 
        sqlformula1 = "Select sum(time_difference) from reports where (time_in_out between date_add(now(), interval -1 day) and now())  AND employee_id = '"+ employee_id +"'"
        
        
        mycursor.execute(sqlformula1)
        
        
        check = mycursor.fetchone()
        print("\nHours Worked Today: ", check[0]/60) 
        #return check[0]

    elif (period == "weekly"):
        # this function will return hours worked by employee and other information 
        sqlformula1 = "Select * from reports where (time_in_out between date_add(now(), interval -7 day) and now())  AND employee_id = '"+ employee_id +"'"
        mycursor.execute(sqlformula1)
        check = mycursor.fetchall()
        print("|", 
                ei, " "*(20-len(ei)), "|",
                si, " "*(20-len(si)), "|",
                tio, " "*(20-len(tio)), "|",
                cio, " "*(20-len(cio)), "|",
                td, " "*(20-len(td)), "|",
                cd, " "*(20-len(cd)), "|")
        for item in check:
            print("|", 
                item[2], " "*(20-len(str(item[2]))), "|",
                item[3], " "*(20-len(str(item[3]))), "|",
                item[4], " "*(20-len(str(item[4]))), "|",
                item[5], " "*(20-len(str(item[5]))), "|",
                item[6], " "*(20-len(str(item[6]))), "|",
                item[7], " "*(20-len(str(item[7]))), "|") 

        sqlformula1 = "Select sum(time_difference) from reports where (time_in_out between date_add(now(), interval -7 day) and now())  AND employee_id = '"+ employee_id +"'"
        mycursor.execute(sqlformula1)
        check = mycursor.fetchone()
        print("\nHours Worked This Week: ", check[0]/60)


        
    elif (period == "monthly"):
        # this function will return hours worked by employee and other information 
        sqlformula1 = "Select * from reports where (time_in_out between date_add(now(), interval -30 day) and now())  AND employee_id = '"+ employee_id +"'"
        mycursor.execute(sqlformula1)
        check = mycursor.fetchall()
    
        print("|", 
                ei, " "*(20-len(ei)), "|",
                si, " "*(20-len(si)), "|",
                tio, " "*(20-len(tio)), "|",
                cio, " "*(20-len(cio)), "|",
                td, " "*(20-len(td)), "|",
                cd, " "*(20-len(cd)), "|")
        for item in check:
            print("|", 
                item[2], " "*(20-len(str(item[2]))), "|",
                item[3], " "*(20-len(str(item[3]))), "|",
                item[4], " "*(20-len(str(item[4]))), "|",
                item[5], " "*(20-len(str(item[5]))), "|",
                item[6], " "*(20-len(str(item[6]))), "|",
                item[7], " "*(20-len(str(item[7]))), "|")

        sqlformula1 = "Select sum(time_difference) from reports where (time_in_out between date_add(now(), interval -30 day) and now())  AND employee_id = '"+ employee_id +"'"
        
        
        mycursor.execute(sqlformula1)
        
        
        check = mycursor.fetchone()
        print("\nHours Worked This Month: ", check[0]/60) 
    #select sum(time_difference) from reports where employee_id = 1
    #Select sum(time_difference) from reports where DATE(time_in_out)= date_sub(curdate(), interval 1 day) AND employee_id = '1'

    #Select sum(time_difference) from reports where DATE(time_in_out)= date_sub(curdate(), interval 10 day) AND employee_id = '1'
    print("\n\n\n") 

    store_menu.managerMenu(store_menu.global_employee_id)

#this will print a report for the individual store   
def indStoreReport(period, ind_store_id):
    ei="Employee ID"
    si="Store ID"
    tio= "Time"
    cio= "Clock In/Out"
    td= "Shift Lenght(min)"
    cd= "Orders Completed"

    if (period == "daily"):
        sqlformula1 = "Select * from reports where (time_in_out between date_add(now(), interval -1 day) and now())  AND store_id = '"+ ind_store_id +"'"
        mycursor.execute(sqlformula1)
        check = mycursor.fetchall()
        print("|", 
                ei, " "*(20-len(ei)), "|",
                si, " "*(20-len(si)), "|",
                tio, " "*(20-len(tio)), "|",
                cio, " "*(20-len(cio)), "|",
                td, " "*(20-len(td)), "|",
                cd, " "*(20-len(cd)), "|")
        for item in check:
            print("|", 
                item[2], " "*(20-len(str(item[2]))), "|",
                item[3], " "*(20-len(str(item[3]))), "|",
                item[4], " "*(20-len(str(item[4]))), "|",
                item[5], " "*(20-len(str(item[5]))), "|",
                item[6], " "*(20-len(str(item[6]))), "|",
                item[7], " "*(20-len(str(item[7]))), "|") 
        # this function will return hours worked by a store and other information 
        sqlformula1 = "Select sum(time_difference) from reports where (time_in_out between date_add(now(), interval -1 day) and now())  AND store_id = '"+ ind_store_id +"'"
        
        #print(sqlformula1)
        mycursor.execute(sqlformula1)
        
        
        check = mycursor.fetchone()
        #print("\nMinutes Worked Today At This Location: ", check[0]) 

        #return check[0]

    elif (period == "weekly"):
        sqlformula1 = "Select * from reports where (time_in_out between date_add(now(), interval -7 day) and now())  AND store_id = '"+ ind_store_id +"'"
        mycursor.execute(sqlformula1)
        check = mycursor.fetchall()
        print("|", 
                ei, " "*(20-len(ei)), "|",
                si, " "*(20-len(si)), "|",
                tio, " "*(20-len(tio)), "|",
                cio, " "*(20-len(cio)), "|",
                td, " "*(20-len(td)), "|",
                cd, " "*(20-len(cd)), "|")
        for item in check:
            print("|", 
                item[2], " "*(20-len(str(item[2]))), "|",
                item[3], " "*(20-len(str(item[3]))), "|",
                item[4], " "*(20-len(str(item[4]))), "|",
                item[5], " "*(20-len(str(item[5]))), "|",
                item[6], " "*(20-len(str(item[6]))), "|",
                item[7], " "*(20-len(str(item[7]))), "|") 
        # this function will return hours worked by a store and other information 
        sqlformula1 = "Select sum(time_difference) from reports where (time_in_out between date_add(now(), interval -7 day) and now())  AND employee_id = '"+ ind_store_id +"'"

        mycursor.execute(sqlformula1)

        check = mycursor.fetchone()
        # print("\nMinutes Worked This Week At This Location: ", check[0])
        
    elif (period == "monthly"):

        sqlformula1 = "Select * from reports where (time_in_out between date_add(now(), interval -30 day) and now())  AND store_id = '"+ ind_store_id +"'"
        mycursor.execute(sqlformula1)
        check = mycursor.fetchall()
        print("|", 
                ei, " "*(20-len(ei)), "|",
                si, " "*(20-len(si)), "|",
                tio, " "*(20-len(tio)), "|",
                cio, " "*(20-len(cio)), "|",
                td, " "*(20-len(td)), "|",
                cd, " "*(20-len(cd)), "|")
        for item in check:
            print("|", 
                item[2], " "*(20-len(str(item[2]))), "|",
                item[3], " "*(20-len(str(item[3]))), "|",
                item[4], " "*(20-len(str(item[4]))), "|",
                item[5], " "*(20-len(str(item[5]))), "|",
                item[6], " "*(20-len(str(item[6]))), "|",
                item[7], " "*(20-len(str(item[7]))), "|") 
        # this function will return hours worked by a store and other information 
        sqlformula1 = "Select sum(time_difference) from reports where (time_in_out between date_add(now(), interval -30 day) and now())  AND employee_id = '"+ ind_store_id +"'"
        
        
        mycursor.execute(sqlformula1)
        
        
        check = mycursor.fetchone()
        #print("\nMinutes Worked This Month At This Location: ", check[0]) 

    print("\n\n\n") 
    
    store_menu.managerMenu(store_menu.global_employee_id)
