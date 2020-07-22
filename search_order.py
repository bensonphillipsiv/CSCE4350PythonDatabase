from tabulate import tabulate
import database_operations

store = "N/A"


def orderMenu():
    menutext = "Order Menu"
    table = [[menutext]]
    output = tabulate(table, tablefmt='grid')
    print(output)

    print("What Store are you Shopping at?")
    print("1.) New York\n")
    print("2.) Los Angeles\n")
    print("3.) Online\n")

    choice = input()
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
        print("Enter the Part Number to Order or Enter '0' to Complete Order:")
        part_number = input()
        if part_number == '0':
            break
        part_number_list.append(part_number)  # adding each part to a list

        print("Enter the Amount to Buy:")
        amount = input()
        list_amounts.append(amount)

    if (database_operations.checkItems(store_id, part_number_list, list_amounts)):  # if there is stock available to buy
        database_operations.updateItems(store_id, part_number_list, list_amounts, -1)  # update database
    else:
        print("Out of Stock on Items")


def searchMenu(store_id):
    menutext = "Search Menu"
    table = [[menutext]]
    output = tabulate(table, tablefmt='grid')
    print(output)

    # menu options
    print("Enter a Keyword to Search for Sets or Bricks:\n")
    keyword = input()

    database_operations.searchItem(keyword, store_id)