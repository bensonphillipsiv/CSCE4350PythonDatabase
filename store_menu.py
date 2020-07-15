from tabulate import tabulate


def searchMenu():
    menutext = "Search Menu"
    table = [[menutext]]
    output = tabulate(table, tablefmt='grid')
    print(output)

    # menu options
    print("Enter a Keyword to Search for Sets or Bricks:\n")
    keyword = input()

    # search through descriptions in database and return items that match description


def orderMenu():
    menutext = "Order Menu"
    table = [[menutext]]
    output = tabulate(table, tablefmt='grid')
    print(output)

    part_number = 'N/A'
    part_number_list = []
    while(part_number != '0'):
        print("Enter the Part Number to Order or Enter '0' to Complete Order:")
        part_number = input()

        if part_number == '0':
            break

        part_number_list.append(part_number)      # adding each part to a list


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
