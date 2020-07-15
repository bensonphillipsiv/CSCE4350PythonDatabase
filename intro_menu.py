from tabulate import tabulate
import database_operations
import online_menu
import store_menu

def introMenu():
    menutext = "Welcome to the Lego store. \nWould You Like To Shop Online or In Store?\n(Please Select A Number Choice Below)"
    table = [[menutext]]
    output = tabulate(table, tablefmt='grid')
    print(output)

    # menu options
    print("1.) Online\n")
    print("2.) In Store\n")

    choice = input()

    if choice == "1":
        online_menu.introOnlineMenu()
    elif choice == "2":
        store_menu.introStoreMenu()
    else:
        print("Please Enter a Correct Menu Choice...")

introMenu()