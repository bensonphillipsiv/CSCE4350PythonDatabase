from tabulate import tabulate
import database_operations

store = "N/A"


def orderMenu(store_id):
    menutext = "Order Menu"
    table = [[menutext]]
    output = tabulate(table, tablefmt='grid')
    print(output)

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

    # if (database_operations.checkItems(store_id, part_number_list, list_amounts)):  # if there is stock available to buy
    database_operations.updateItems(store_id, part_number_list, list_amounts, -1)  # update database


def searchMenu(store_id):
    menutext = "Search Menu"
    table = [[menutext]]
    output = tabulate(table, tablefmt='grid')
    print(output)

    # menu options
    print("Enter a Keyword to Search for Sets or Bricks:\n")
    keyword = input()

    database_operations.searchItem(keyword, store_id)
