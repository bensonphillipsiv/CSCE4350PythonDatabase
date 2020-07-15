from tabulate import tabulate
import database_operations


def searchMenu():
    menutext = "Search Menu"
    table = [[menutext]]
    output = tabulate(table, tablefmt='grid')
    print(output)

    # menu options
    print("Enter a Keyword to Search for Sets or Bricks:\n")
    keyword = input()

    # search through descriptions in database and return items that match description


def paymentMenu():
    menutext = "Payment Menu"
    table = [[menutext]]
    output = tabulate(table, tablefmt='grid')
    print(output)

    print("Are you a New or Returning Customer?\n")
    print("1.) New Customer\n")
    print("2.) Returning Customer\n")

    choice = input()
    if choice == "1":       # new customer login and
        # username and password
        print("Enter New Username:\n")
        username = input()
        print("Enter New Password:\n")
        password = input()

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
            if choice == "1": card_type = "VISA"
            elif choice == "2": card_type = "AMEX"
            elif choice == "3": card_type = "MC"

        # Card Number
        print("Enter Card Number:\n")
        card_number = input()

    elif choice == "2":
        print("Enter Username:\n")
        username = input()
        print("Enter Password:\n")
        password = input()

        # check if a user and use information
    else:
        print("Please Input Correct Choice...")
        paymentMenu()


def orderMenu():
    menutext = "Order Menu"
    table = [[menutext]]
    output = tabulate(table, tablefmt='grid')
    print(output)

    print("What Store are you Shopping at?")
    print("1.) New York\n")
    print("2.) Los Angeles\n")
    print("3.) Online\n")
    store_number = input()

    part_number = 'N/A'
    part_number_list = []
    list_amounts = []
    while(part_number != '0'):
        print("Enter the Part Number to Order or Enter '0' to Complete Order:")
        part_number = input()
        if part_number == '0':
            break
        part_number_list.append(part_number)      # adding each part to a list

        print("Enter the Amount to Buy:")
        amount = input()
        list_amounts.append(amount)

    if (database_operations.checkItems(store_number, part_number_list, list_amounts)):      # if there is stock available to buy
        database_operations.updateItems(store_number, part_number_list, list_amounts, -1)       # update database
        paymentMenu() # pay for items
    else:
        print("Out of Stock on Items")



def employeeMenu():
    menutext = "Employee Menu"
    table = [[menutext]]
    output = tabulate(table, tablefmt='grid')
    print(output)


def employeeLogin():
    menutext = "Employee Login"
    table = [[menutext]]
    output = tabulate(table, tablefmt='grid')
    print(output)

    # Login
    print("Enter Employee Login Username:")
    username = input()
    print("Enter Employee Login Password:")
    password = input()

    # perform database checking operations
    login = True
    if (login):
        employeeMenu()
    else:   # return to base menu
        print("Incorrect Login")
        baseMenu()


def baseMenu():
    menutext = "Welcome to the Lego store"
    table = [[menutext]]
    output = tabulate(table, tablefmt='grid')
    print(output)

    # menu options
    print("1.) Search for Sets or Bricks\n")
    print("2.) Order Sets or Bricks\n")
    print("3.) Employee Login\n")

    choice = input()

    if choice == "1":
        searchMenu()
    elif choice == "2":
        orderMenu()
    elif choice == "3":
        employeeLogin()
    else:
        print("Please Enter a Correct Menu Choice...")


baseMenu()
