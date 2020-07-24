import online_menu
import store_menu


def intro():
    print("---Welcome to the Lego store. \nPlease Select Store Mode or Online Mode---")

    # menu options
    print("1.) Store Mode (Employees)\n")
    print("2.) Online Mode (Customers)\n")

    choice = input()

    if choice == "1":
        store_menu.introStoreMenu()
    elif choice == "2":
        online_menu.introOnlineMenu()
    else:
        print("Please Enter a Correct Menu Choice...")
        intro()


if __name__ == "__main__":
    intro()
