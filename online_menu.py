import database_operations
import search_order
import introMenu


# this menu will welcome user as well as determine whether they need to login or sign up.
def introOnlineMenu():
    print("---Welcome to the Online Lego store. \nPlease Signup/Login.\n(Please Select A Number Choice Below)---")

    # menu options
    print("1.) Signup\n")
    print("2.) Login\n")
    print("3.) Return to Main Menu\n")

    choice = input()

    if choice == "1":
        customerSignup()
    elif choice == "2":
        customerLogin()
    elif choice == "3":
        introMenu.intro()
    else:
        print("Please Enter a Correct Menu Choice...")


def customerSignup():
    print("---New Customer Sign Up---")

    # User name input
    print("\nEnter Your Name:")
    customer_name = input()

    # User card input
    print("\nEnter Your card 16 digit card number:")
    customer_card = input()

    #Phone number
    print("\nEnter Your Phone Number:")
    customer_phone = input()

    #customer adress
    print("\nEnter Your Address:")
    customer_address = input()

    email_check = 1
    
    #
    #Checks if email is already in Use
    #
    while (email_check == 1):
        #customer email
        print("\nEnter Signup Email:")
        customer_email = input()

        #
        #Checks if email is already in Use
        #
        email_check = database_operations.columnCheck("Customers", "customer_email", customer_email)
        
        if (email_check == 0):
            print("Email Has Been Accepted.\n")
        else:
            print("Email Is Already In The System, Please Use An Alternative Email.\n")

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

    database_operations.addNewCustomer(customer_name, customer_phone, customer_address, customer_email, customer_password, customer_card)

    #place user data into database
    #let user know he successfully signed up!
    print("\nWoohoo " + customer_name + ", You Have Succesfully Created an Account!")

    loggedInMenu()


#this function will login in the customer
def customerLogin():
    #customer email
    print("\nEmail:")
    customer_email = input()

    print("\nPassword:")
    customer_password = input()

    #this is where we check whether the creedentials work.
    login_check = database_operations.loginAuth(customer_email, customer_password, "Customers", "customer_email", "customer_password")
     
    if (login_check == 1):
        loggedInMenu()
    else:
        print("Incorrect Login Information")
        customerLogin()
    

def loggedInMenu():
    print("---Customer Menu---")

    # menu options
    print("1.) Buy Items\n")
    print("2.) Search Items\n")
    choice = input()

    if choice == "1":
        search_order.orderMenu("online")
        loggedInMenu()
    elif choice == "2":
        search_order.searchMenu("online")
        loggedInMenu()
