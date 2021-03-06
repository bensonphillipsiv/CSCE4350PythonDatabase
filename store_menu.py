import database_operations
import search_order
import introMenu

store_id = "N/A"
global_employee_id = "N/A"


def introStoreMenu():
    print("----Employee Login/ Signup---")

    # menu options
    print("1.) Signup\n")
    print("2.) Login\n")

    choice = input()

    if choice == "1":
        employeeSignup()
    elif choice == "2":
        employeeLogin()
    else:
        print("Please Enter a Correct Menu Choice...")


def employeeSignup():
    print("---New Employee Sign Up---")

    # Name input
    print("\nEnter Your Name:")
    employee_name = input()

    # Employee Type
    print("Enter Employee Type:\n")
    print("1.) Salesman\n")
    print("2.) Manager\n")

    choice = input()

    if choice == "1":
        employee_type = "salesman"
    else:
        employee_type = "manager"

    # Employee Store
    print("Enter Employee Store:\n")
    print("1.) New York\n")
    print("2.) Los Angeles\n")

    choice = input()

    global store_id
    if choice == "1":
        store_id = "newyork"
    else:
        store_id = "losangeles"

    # Employee password
    print("\nEnter Password:")
    employee_password = input()

    # verifying password
    print("\nPlease Verify Password:")
    employee_password_verification = input()

    # verifying that the passwords match,
    if (employee_password == employee_password_verification):
        print("\nCongrats, Passwords Matched!")
    else:
        while (employee_password != employee_password_verification):
            print("\nSorry, Passwords Did Not Match, Please try again.")

            # employee password
            print("\nEnter Password:")
            employee_password = input()

            # verifying password
            print("\nPlease Verify Password:")
            employee_password_verification = input()

        print("\nCongrats, Passwords Matched!")

    em_id = str(database_operations.addNewEmployee(employee_name, employee_type, store_id, employee_password))  

    # place user data into database
    # let user know he successfully signed up!
    print("\nWoohoo " + employee_name + ", You Have Successfully Created an Account! Your Employee ID is: " + em_id + "\nPlease Login to verify your account.\n")
    employeeLogin()


def employeeLogin():
    #employee email
    print("\nEmployee ID:")
    employee_id = input()

    global global_employee_id
    global_employee_id = employee_id

    print("\nPassword:")
    employee_password = input()

    #this is where we check whether the credentials work.
    login_check = database_operations.loginAuth(employee_id, employee_password, "Employees", "employee_id", "employee_password")
     
    if (login_check == 1):
        global store_id
        store_id = database_operations.checkStore(employee_id)

        employee_rank = database_operations.employee_rank_check("Employees", "employee_id", employee_id)
        #print(employee_rank)
        if (employee_rank == "salesman"):

            database_operations.clock_in_out(employee_id, "in", store_id)
            salesmanMenu(employee_id)
        elif (employee_rank == "manager"):
            database_operations.clock_in_out(employee_id, "in", store_id)
            managerMenu(employee_id)   
    else:
        employeeLogin()   


# manager menu to update
def managerMenu(employee_id):
    global global_employee_id 
    global_employee_id = (employee_id)

    print("---Manager Menu---")

    # menu options
    print("1.) Add Inventory\n")
    print("2.) Add Store\n")
    print("3.) Generate Report\n")
    print("4.) Clock Out/ Return to Main Menu\n")
    choice = input()

    if choice == "1":
        addInventory()
    elif choice == "2":
        addStore()
    elif choice == "3":
        generateReport()
    elif choice == "4":
        database_operations.clock_in_out(employee_id, "out", store_id)
        introMenu.intro()
    else:
        print("Please Enter a Correct Menu Choice...")
        managerMenu(employee_id)


def salesmanMenu(employee_id):
    print("---Salesman Menu---")

    # menu options
    print("1.) Sell Items\n")
    print("2.) Search Items\n")
    print("3.) Clock Out/ Return to Main Menu\n")
    choice = input()

    global store_id
    if choice == "1":
        search_order.orderMenu(store_id)
        salesmanMenu(employee_id)
    elif choice == "2":
        search_order.searchMenu(store_id)
        salesmanMenu(employee_id)
    elif choice == "3":
        database_operations.clock_in_out(employee_id, "out", store_id)
        introMenu.intro()
    else:
        print("Please Enter a Correct Menu Choice...")
        salesmanMenu(employee_id)


def paymentMenu(store_id, part_number_list, list_amounts):
    global global_employee_id
    print("---Payment Menu---")

    # payment type
    print("Payment Type:\n")
    print("1.) Cash\n")
    print("2.) Card\n")
    choice = input()
    if choice == "1":
        payment_type = "cash"
    else:
        payment_type = "card"
        print("Card Type:\n")
        print("1.) VISA\n")
        print("2.) AMEX\n")
        print("3.) MC\n")
        choice = input()
        if choice == "1":
            card_type = "VISA"
        elif choice == "2":
            card_type = "AMEX"
        elif choice == "3":
            card_type = "MC"

        # Card Number
        print("Enter Card Number:\n")
        card_number = input()

    database_operations.orderUpdate(store_id, global_employee_id, payment_type, part_number_list, list_amounts)
    print("Thank you for your payment")
    salesmanMenu(global_employee_id)


def addInventory():
    print("What Store do you want to add inventory to?")
    print("1.) New York\n")
    print("2.) Los Angeles\n")
    print("3.) Online\n")

    choice = input()
    global store_id
    global global_employee_id
    if choice == "1":
        store_id = "newyork"
    elif choice == "2":
        store_id = "losangeles"
    elif choice == "3":
        store_id = "online"

    part_number = 'N/A'
    part_number_list = []
    list_amounts = []
    while (part_number != '0'):
        print("Enter the Part Number to update or Enter '0' to Complete Update:")
        part_number = input()
        if part_number == '0':
            break
        part_number_list.append(part_number)  # adding each part to a list

        print("Enter the Amount to increase:")
        amount = input()
        list_amounts.append(amount)

    database_operations.updateItems(store_id, part_number_list, list_amounts, 1)  # update database

    managerMenu(global_employee_id)


def addStore():
    print("Enter the store name: ")
    store_id = input()

    database_operations.addStore(store_id)
    managerMenu(global_employee_id)


def generateReport():
    print("---Report Generator---")

    # menu options
    print("1.) Generate Employee Report For The Store\n")
    print("2.) Generate Individual Employee Report\n")
    print("3.) Generate Orders Report\n")
    choice = input()

    if choice == "1":
        #print("DEV IS STILL WORKING ON THIS FEATURE")
        print("Which Store Would You Like To Generate a Report On?\n(Please Type in location)\n")
        store_input = input()
        employee_check = database_operations.columnCheck("stores", "store_id", store_input)
        #print(employee_check)
        if (employee_check == 1):
            print("\nWhat kind of report would you like to generate?")
            print("1.) Daily Report\n")
            print("2.) Weekly Report\n")
            print("3.) Monthly Report\n")
            choice1 = input()

            if (choice1=="1"):
                database_operations.indStoreReport("daily", store_input)
            elif (choice1=="2"):
                database_operations.indStoreReport("weekly", store_input)
            elif (choice1=="3"):
                database_operations.indStoreReport("monthly", store_input)
            else:
                print("Invalid choice!")
                generateReport()
        else:
            print("\nINVALID LOCATION! \n")
            generateReport() 
    elif choice == "2":
        print("Which Employee Would You Like To Generate a Report On?\n(Please Type in Employee ID)\n")
        employee_input = input()
        employee_check = database_operations.columnCheck("employees", "employee_id", employee_input)
        #print(employee_check)
        if (employee_check == 1):
            print("\nWhat kind of report would you like to generate?")
            print("1.) Daily Report\n")
            print("2.) Weekly Report\n")
            print("3.) Monthly Report\n")
            choice1 = input()

            if (choice1=="1"):
                database_operations.indEmployeeReport("daily", employee_input)
            elif (choice1=="2"):
                database_operations.indEmployeeReport("weekly", employee_input)
            elif (choice1=="3"):
                database_operations.indEmployeeReport("monthly", employee_input)
            else:
                print("Invalid choice!")
                generateReport()
        else:
            print("\nINVALID EMPLOYEE ID! \n")
            generateReport() 
    elif choice == "3":
        database_operations.generateOrdersReport()

    managerMenu(global_employee_id)