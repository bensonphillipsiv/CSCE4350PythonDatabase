from tabulate import tabulate
import database_operations
import search_order


def introStoreMenu():
    menutext = "Employee Login/ Signup"
    table = [[menutext]]
    output = tabulate(table, tablefmt='grid')
    print(output)

    # menu options
    print("1.) Signup\n")
    print("2.) Login\n")

    choice = input()

    if choice == "1":
        employeeSignup()
    elif choice == "2":
        employeeSignup()
    else:
        print("Please Enter a Correct Menu Choice...")


def employeeSignup():
    menutext = "New Employee Sign Up"
    table = [[menutext]]
    output = tabulate(table, tablefmt='grid')
    print(output)

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
    elif choice == "2":
        employee_type = "manager"

    # Employee Store
    print("Enter Employee Store:\n")
    print("1.) New York\n")
    print("2.) Los Angeles\n")

    choice = input()

    if choice == "1":
        employee_store = "newyork"
    elif choice == "2":
        employee_store = "losangles"

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

    database_operations.addNewEmployee(employee_name, employee_type, employee_store, employee_password)

    # place user data into database
    # let user know he successfully signed up!
    print("\nWoohoo " + employee_name + ", You Have Successfully Created an Account!")

    if employee_type == "manager":
        managerMenu()
    else:
        salesmanMenu()


# manager menu to update
def managerMenu():
    menutext = "Manager Menu"
    table = [[menutext]]
    output = tabulate(table, tablefmt='grid')
    print(output)

    # menu options
    print("1.) Add Inventory\n")
    print("2.) Add Store\n")
    print("3.) Generate Report\n")
    choice = input()

    if choice == "1":
        addInventory()
    elif choice == "2":
        addStore()
    elif choice == "3":
        print("beep... boop... report generated")
    else:
        print("Please Enter a Correct Menu Choice...")


def salesmanMenu():
    menutext = "Salesman Menu"
    table = [[menutext]]
    output = tabulate(table, tablefmt='grid')
    print(output)

    # menu options
    print("1.) Sell Items\n")
    choice = input()

    if choice == "1":
        search_order.orderMenu()
        paymentMenu()


def paymentMenu():
    menutext = "Payment Menu"
    table = [[menutext]]
    output = tabulate(table, tablefmt='grid')
    print(output)

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
    

def addInventory():
    print("adding inventory")


def addStore():
    print("adding a new store")
