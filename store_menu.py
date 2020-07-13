from tabulate import tabulate


def menu():
   
    print("\n")
    menutext = "Welcome to the Lego store"
    table = [[menutext]]
    output = tabulate(table, tablefmt='grid')
    print(output)

    print("1.) \n")

    print("2.) \n")

    print("3.) \n")

    print("4.) \n")

    print("5.) \n")
    
    choice = input()

    if choice ==  "1":
        print("You have 1 tussy \n")
        menu()
    
    if choice ==  "2":
        print("You have 2 tussy \n")
        menu()

    if choice ==  "3":
        print("You have 3 tussy \n")
        menu()

    if choice ==  "4":
        print("You have 4 tussy \n")
        menu()

    if choice ==  "5":
        print("You have 5 tussy \n")
        menu()

menu()
