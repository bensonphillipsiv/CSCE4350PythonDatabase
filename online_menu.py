from tabulate import tabulate
import database_operations

#this menu will welcome user as well as determine whether they need to login or sign up.
def introOnlineMenu():
    menutext = "Welcome to the Online Lego store. \nPlease Signup/Login.\n(Please Select A Number Choice Below)"
    table = [[menutext]]
    output = tabulate(table, tablefmt='grid')
    print(output)

    # menu options
    print("1.) Signup\n")
    print("2.) Login\n")

    choice = input()

    if choice == "1":
        customerSignup()
    elif choice == "2":
        customerLogin()
    else:
        print("Please Enter a Correct Menu Choice...")

def onlineBaseMenu():
    menutext = "Online Lego store\n(Please Select A Number Choice Below)"
    table = [[menutext]]
    output = tabulate(table, tablefmt='grid')
    print(output)

    # menu options
    print("1.) Search for Sets or Bricks\n")
    print("2.) Order Sets or Bricks\n")
    print("3.) Customer Signup\n")

    choice = input()

    if choice == "1":
        searchMenu()
    elif choice == "2":
        orderMenu()
    else:
        print("Please Enter a Correct Menu Choice...")


def customerSignup():
    menutext = "New Customer Sign Up"
    table = [[menutext]]
    output = tabulate(table, tablefmt='grid')
    print(output)

    # User name input
    print("\nEnter Your Name:")
    customer_name = input()

    #Phone number
    print("\nEnter Your Phone Number:")
    customer_phone = input()

    #customer adress
    print("\nEnter Your Address:")
    customer_address = input()

    #customer email
    print("\nEnter Signup Email:")
    customer_email = input()

    #customer password
    print("\nEnter Password:")
    customer_password = input()

    #verifying password
    print("\nPlease Verify Password:")
    customer_password_verification = input()

    #verifying that the passwords match,
    if (customer_password == customer_password_verification):
        print("\nCongrats, Passwords Matched!")

    else:
        while (customer_password != customer_password_verification):
            print("\nSorry, Passwords Did Not Match, Please try again.")

            #customer password
            print("\nEnter Password:")
            customer_password = input()

            #verifying password
            print("\nPlease Verify Password:")
            customer_password_verification = input()

        print("\nCongrats, Passwords Matched!")

    database_operations.addNewCustomer(customer_name, customer_phone, customer_address, customer_email, customer_password)


    #place user data into database

    #let user know he successfully signed up!
    print("\nWoohoo " + customer_name + ", You Have Succesfully Created an Account!")


def customerLogin():
    print("you loggedin bro")



