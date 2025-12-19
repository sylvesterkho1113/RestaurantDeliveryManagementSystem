# Project DPL5211 Fundamental of Programming Language
# Group 03: Restaurant Delivery Management System

# 1211207735 See Chwan Kai
# 1211211485 Kho Wei Cong
# 1211211733 Kerk Ming Da
# 1211110456 Yap Meng Yoon

# login.txt // order.txt // menu.txt // hour.txt

# Admin Username: admin
# Admin Password: admin123

import os

def clear_screen():
    ## This function is used to clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')

def user_function():
    clear_screen()
    
    # Display User Page Menu
    print("\n\033[94m--------------------------")
    print("|        \033[1mUSER PAGE\033[0m       \033[94m|")
    print("--------------------------\033[0m\n")
    print("[1] Register")
    print("[2] Login")

    # Ask user to select option
    u_choice = int(input("\nSelect your choice \033[91m[1 or 2]\033[0m : "))

    # Check user input
    while u_choice > 2 or u_choice < 1:
        u_choice = int(
            input("Wrong code input, please try again \033[91m[1 or 2]\033[0m: "))

    # Jump to selected option
    if u_choice == 1:
        # Jump to register section
        register_function()

    elif u_choice == 2:
        # Jump to login section
        login_function()


def register_function():
    clear_screen()
    f_check = True
    l_check = True
    
    # Display User Registration Page Title
    print("\n\033[94m---------------------------------------")
    print("|        \033[1mUSER REGISTRATION PAGE\033[0m       \033[94m|")
    print("---------------------------------------\033[0m\n")

    # Ask user to enter registration credentials
    while True:
        first_name = input("Enter your first name: ")
        if not all(char.isalpha() or char.isspace() or char == "/" for char in first_name):
            print("\n\033[91mInvalid input. First name should only contain alphabets, spaces, or slashes (/). Please try again.\033[0m")
        else:
            break

    while True:
        last_name = input("Enter your last name : ")
        if not all(char.isalpha() or char.isspace() or char == "/" for char in last_name):
            print("\n\033[91mInvalid input. Last name should only contain alphabets, spaces, or slashes (/). Please try again.\033[0m")
        else:
            break
        
    phone_number = input(
        "Enter your phone number \033[91m(Format: 01XXXXXXXX)\033[0m   : ")
    with open("login.txt", "r") as check:
        for line in check:
            stored_firstname, stored_lastname, stored_phonenumber, stored_address, stored_password = line.strip().split(',')

    # Check in file if the credential match
    if stored_phonenumber == phone_number:
        # while we have matched record in the login.txt, told the user and switch to login page
        print("\nPhone number existed, press any key to proceed to login...")
        getchar = input()
        login_function()
        return

    # If phone number is unique, keep asking other details
    address = input(
        "Enter your address \033[91m(without comma)\033[0m             : ")

    password = input("Enter your password    : ")
    confirm_password = input("Confirm your password  : ")

    # Check if both passwords matched
    while password != confirm_password:
        # Display error message
        print("\nPassword unmatch, please check and try again!")

        # Ask user to re-enter password
        password = input("Enter your password    : ")
        confirm_password = input("Confirm your password  : ")

    # Save the records into file
    with open("login.txt", "a") as file:
        file.write(f"{first_name},{last_name},{phone_number},{address},{password}\n")

    # Close the file
    file.close()

    # Display successful message to user
    print("\n\033[32mThank you \033[3m"+first_name + "\033[0m\033[32m, your account has been created successfully!\033[0m")
    print("Press any key to proceed to login...")
    getchar = input()

    # Switch to login_function
    login_function()


def login_function():
    clear_screen()
    # Display User Login Page Title
    print("\n\033[94m--------------------------------")
    print("|        \033[1mUSER LOGIN PAGE\033[0m       \033[94m|")
    print("--------------------------------\033[0m\n")

    login = {}
    with open('login.txt', 'r') as login_file:
        for line in login_file:
            stored_firstname, stored_lastname, stored_phonenumber, stored_address, stored_password = line.strip().split(',')
            login[stored_phonenumber] = {
                'stored_firstname': stored_firstname,
                'stored_lastname': stored_lastname,
                'stored_address': stored_address,
                'stored_password': stored_password
            }

    # get item_id from user
    stored_username = input("Enter phone number \033[91m(Format: 01XXXXXXXX)\033[0m: ")
    stored_password = input("Enter password: ")

    # Check in file if the credential match
    while stored_username not in login or login[stored_username]['stored_password'] != stored_password:
        # Display error message
        print("\nWrong username or password, please try again.")
        # Repeat again login_function until user input correct credential
        stored_username = input("Enter phone number \033[91m(Format: 01XXXXXXXX)\033[0m: ")
        stored_password = input("Enter password: ")

    # Print successful message
    print("\n\033[32mWelcome back, \033[3m" + login[stored_username]['stored_firstname'] + "\033[0m\033[32m!\033[0m")
    print("Press any key to continue...")
    getchar = input()    
    # Jump to user_main function
    user_main(stored_username)

def user_main(username):
    clear_screen()
    # Declare variable
    selection = 1

    # Keep looping the menu until user terminate the program
    while selection != 10:

        # Display user main menu
        print("\n\033[94m-------------------------------")
        print("|        \033[1mUSER MAIN MENU       \033[0m\033[94m|")
        print("-------------------------------\033[0m\n")
        print("[1]  Place A New Order")
        print("[2]  Display History Order")
        print("[3]  Search History Order Based On Status")
        print("[4]  Cancel Ongoing Order\n")

        print("[5]  Update Delivery Address")
        print("[6]  Display User Information\n")

        print("[7]  Display All Restaurant Branch Info and Open Hours")
        print("[8]  Need help or have any feedback? Press here to contact us!")
        
        print("[9]  Logout")
        print("[10] Exit")

        # Ask for user selection
        selection = int(input("\nEnter your selection : "))

        # Do the Action Based on Selected Option
        if selection == 1:
            # This is for user to place a new order
            user_place_order(username)
            print("Press any key to return to main menu...")
            getchar = input()
            clear_screen()
        elif selection == 2:
            # This is to display history customer order
            user_history_order(username)
            print("Press any key to return to main menu...")
            getchar = input()
            clear_screen()
        elif selection == 3:
            # This is to search history customer order
            user_search_order(username)
            print("Press any key to return to main menu...")
            getchar = input()
            clear_screen()
        elif selection == 4:
            # This is to cancel or delete customer order
            user_cancel_order(username)
            clear_screen()
        elif selection == 5:
            # This is to update(edit) user's information
            user_edit_info(username)
            print("Press any key to return to main menu...")
            getchar = input()
            clear_screen()
        elif selection == 6:
            # This is to display user's information
            user_display_info(username)
            print("Press any key to return to main menu...")
            getchar = input()
            clear_screen()
        elif selection == 7:
            # This is to display all branch info
            display_hour()
            print("Press any key to return to main menu...")
            getchar = input()
            clear_screen()
        elif selection == 8:
            clear_screen()
            # This is to show our support hotline
            print("\n\033[36m********************************************")
            print(" We are sorry for the inconvenience caused.")
            print(" Let us assist you at \033[1m\033[4m03-8312 5400\033[0m")
            print("\033[36m********************************************\033[0m")

            print("\nPress any key to return to main menu...")
            getchar = input()
            clear_screen()
        elif selection == 9:
            # This is to login to admin page
            clear_screen()
            print("\nLogging out, press any key to continue...")
            getchar = input()
            main()
        elif selection == 10:
            # This is to terminate the program
            print("\nThank you for using the service, have a nice day.")
            exit(0)
        else:
            # Invalid Code --> Ask user to re-enter the code again
            print("\n\033[91mInvalid code, please enter a valid number [1-10]\033[0m. ")
            print("Press any key to continue...")
            getchar = input()
            clear_screen()

#################### USER MAIN MENU FUNCTION ####################

def user_place_order(username):
    ans = 'y'

    while ans == 'y' or ans == 'Y':
        clear_screen()
        
        # Title
        print("\n\033[94m---------------------------------")
        print("|         \033[1mPLACE NEW ORDER       \033[0m\033[94m|")
        print("---------------------------------\033[0m\n")

        # Retrieved menu item from menu.txt and assign to appropiate variable
        menu = {}
        with open('menu.txt', 'r') as menu_file:
            for line in menu_file:
                item_id, item_name, item_price, item_description = line.strip().split(',')
                menu[item_id] = {
                    'item_name': item_name,
                    'item_price': round(float(item_price), 2),
                    'item_description': item_description
                }
                # Display menu
                print("-----------------")
                print("\033[33m  Item ID #"+str(item_id)+"\033[0m")
                print("-----------------")
                print("\033[1mItem Name        : \033[0m"+item_name)
                print("\033[1mItem Price (RM)  : \033[0m"+"{:.2f}".format(float(item_price)))
                print("\033[1mItem Description : \033[0m"+item_description+"\n")

        # get item_id from user
        item_id = input("Enter selected Item ID: ")

        # Check if item_id user enter existed in menu.txt
        while item_id not in menu:
            print("\n\033[91mSelected Item ID not found, please try again.\033[0m")
            # Ask user to enter valid item id
            item_id = input("Enter selected Item ID: ")

        # Ask for quantity
        quantity = int(input("Enter quantity: "))

        # Calculate total (item_price * quantity + delivery fee)
        total = round(((menu[item_id]["item_price"] * quantity) + 5), 2)

        # Save order information into order.txt
        with open('order.txt', 'a') as order_file:
            order_file.write(f'{username},{item_id},{menu[item_id]["item_name"]},{menu[item_id]["item_price"]},{quantity},{total},{"Order placed"}\n')

        clear_screen()

        # Display successful message
        print("\n\033[32m\033[1mYour order has been placed successful!\033[0m\n")
        print("---------------------")
        print("    \033[33mOrder Details\033[0m")
        print("---------------------")
        print("\033[1mItem Name    \033[0m: "+menu[item_id]["item_name"])
        print("\033[1mItem Price   \033[0m: RM"+"{:.2f}".format(menu[item_id]["item_price"]))
        print("\033[1mQuantity     \033[0m: "+str(quantity))
        print("\033[1mDelivery Fee \033[0m: RM5.00")        
        print("\033[1mTotal        \033[0m: RM"+"{:.2f}".format(total)+"\n")

        # Ask user if they want to make another order
        ans = input("Enter \033[91m[Y]\033[0m if you wish to make another order: ")

def user_history_order(username):
    clear_screen()
    
    # Initialize
    count = 1

    # Title
    print("\n\033[94m--------------------------------")
    print("|         \033[1mHISTORY ORDERS       \033[0m\033[94m|")
    print("--------------------------------\033[0m\n")

    # Read order data from order.txt
    with open('order.txt', 'r') as order_file:
        for line in order_file:
            order_data = line.strip().split(',')
            order_username = order_data[0]

            # Compare username in order.txt with username that user entered
            # Only display order history that match with username
            if order_username == username:
                item_id = order_data[1]
                item_name = order_data[2]
                item_price = float(order_data[3])
                quantity = order_data[4]
                total = float(order_data[5])
                status = order_data[6]

                # Display history order
                print("---------------")
                print("\033[33m  Order No #"+str(count)+"\033[0m")
                print("---------------")
                print(f"\033[1mItem ID\033[0m      : {item_id}\n\033[1mItem Name\033[0m    : {item_name}\n\033[1mItem Price\033[0m   : RM{item_price:.2f}\n\033[1mQuantity\033[0m     : {quantity}\n\033[1mTotal\033[0m        : RM{total:.2f}\n\033[1mOrder Status\033[0m : {status}\n")
                count += 1

def user_search_order(username):
    clear_screen()

    # Title
    print("\n\033[94m-------------------------------")
    print("|         \033[1mSEARCH ORDERS       \033[0m\033[94m|")
    print("-------------------------------\033[0m\n")
    print("[1] Order Placed\n[2] Preparing\n[3] Cancelled\n[4] Out of Delivery\n[5] Delivered")
    
    # Ask uswe to enter status number1

    status_no = int(input("\nEnter status of the order you would like to check \033[91m[1-5]\033[0m: "))

    # Check if status number is valid
    while int(status_no) < 1 or int(status_no) > 5:
        print("\n\033[91mInvalid status number, please try again.\033[0m")
        status_no = int(input("Enter status of the order: "))

    # Convert status number to status name
    if status_no == 1:
        desired_status = "Order placed"
    elif status_no == 2:
        desired_status = "Preparing"
    elif status_no == 3:
        desired_status = "Cancelled"
    elif status_no == 4:
        desired_status = "Out of Delivery"
    elif status_no == 5:
        desired_status = "Delivered"

    count = 1

    clear_screen()

    # Read order data from order.txt
    with open('order.txt', 'r') as order_file:
        for line in order_file:
            order_data = line.strip().split(',')
            order_username = order_data[0]
            status = order_data[6]

            # Display order with matching status and matching username
            if str(status) == str(desired_status) and order_username == username:
                item_id = order_data[1]
                item_name = order_data[2]
                item_price = float(order_data[3])
                quantity = order_data[4]
                total = float(order_data[5])
                
                # Display order details
                print("------------------")
                print("\033[33m  Order No #"+str(count)+"\033[0m")
                print("------------------")
                print(f"\033[1mItem ID\033[0m      : {item_id}\n\033[1mItem Name\033[0m    : {item_name}\n\033[1mItem Price\033[0m   : RM{item_price:.2f}\n\033[1mQuantity\033[0m     : {quantity}\n\033[1mTotal\033[0m        : RM{total:.2f}\n\033[1mOrder Status\033[0m : {status}\n")
                count += 1

    # If no orders found with the desired status
    if count == 1:
        print("\n\033[91mNo orders found with the mentioned status.\033[0m")

def user_cancel_order(username):
    clear_screen()
    
    # Title
    print("\n\033[94m--------------------------------------")
    print("|         \033[1mCANCEL ONGOING ORDER       \033[0m\033[94m|")
    print("--------------------------------------\033[0m\n")    
    
    # Warning message
    print("\033[91m** Please note that only orders in '\033[1mOrder placed\033[0m\033[91m' status can be cancelled.\n** For orders with other statuses, please contact our customer service.\033[0m")
    ans = input("\nPress \033[91m[1]\033[0m to continue to cancel an order, or press any key to return to the main menu: ")

    if ans == '1':
        # Initialize
        count = 1
        order_number_mapping = {}

        # Read order data from order.txt
        with open('order.txt', 'r') as order_file:
            order_lines = order_file.readlines()
            total_orders = len(order_lines)

            # Seperate order data by line and assigned into array
            for i, line in enumerate(order_lines):
                order_data = line.strip().split(',')
                order_username = order_data[0]
                status = str(order_data[6])

                # Display orders with matching username and "Order placed" status
                if order_username == username and status == "Order placed":
                    item_id = order_data[1]
                    item_name = order_data[2]
                    item_price = float(order_data[3])
                    quantity = order_data[4]
                    total = float(order_data[5])

                    # Display order details
                    print("\n------------------")
                    print("\033[33m  Order No #"+str(count)+"\033[0m")
                    print("------------------")
                    print(f"\033[1mItem ID\033[0m      : {item_id}\n\033[1mItem Name\033[0m    : {item_name}\n\033[1mItem Price\033[0m   : RM{item_price:.2f}\n\033[1mQuantity\033[0m     : {quantity}\n\033[1mTotal\033[0m        : RM{total:.2f}\n\033[1mOrder Status\033[0m : {status}")
                    order_number_mapping[count] = i
                    count += 1

            # Prompt user to input the order number to be deleted
            order_number = int(input("\nEnter the Order Number to be cancelled: "))

            # Check if the order number is valid
            while order_number < 1 or order_number > count - 1:
                print("\n\033[91mInvalid order number, please try again.\033[0m")
                order_number = int(input("Enter the Order Number to be cancelled: "))

            # Delete the order from order_lines list
            order_index = order_number_mapping[order_number]
            order_lines.pop(order_index)

            # Write the updated order_lines back to order.txt
            with open('order.txt', 'w') as order_file:
                order_file.writelines(order_lines)

            clear_screen()

            # Display success message
            print("\n\033[32mYour order has been cancelled!\033[0m")
            print("Press any key to return to main menu...")
            getchar = input()
    else:
        return


def user_edit_info(username):
    clear_screen()

    # Title
    print("\n\033[94m-------------------------------------")
    print("|       \033[1mEdit User Information       \033[0m\033[94m|")
    print("-------------------------------------\033[0m\n")

    # Read the contents of login.txt file
    with open("login.txt", "r") as login_file:
        lines = login_file.readlines()

    found = False

    # Search for the MMU ID in the file
    for i, line in enumerate(lines):
        data = line.strip().split(",")
        # Find the line that matches the username
        if data[2] == username:
            found = True
            # Store the old address into the array
            old_address = str(data[3])
            # Display current address
            print("\033[1mYour current address is\033[0m >>>>>>>>>>> " + old_address)
            # Ask user to input new address
            new_address = str(input("\033[1mEnter new address \033[91m(Without comma)\033[0m : "))
            # Store new address into the array
            lines[i] = f"{data[0]},{data[1]},{data[2]},{str(new_address)},{data[4]}\n"
            break

    # Write the updated contents back to login.txt file
    with open("login.txt", "w") as file:
        file.writelines(lines)

    clear_screen()

    # Diplay successful message
    print("\n\033[32mYour address has been updated successfully!\033[0m\n")
    print("\033[1mOld address\033[0m: " + old_address)
    print("\033[1mNew address\033[0m: " + new_address+"\n")

def user_display_info(username):
    clear_screen()

    # Title
    print("\n\033[94m-------------------------")
    print("|      \033[1mUSER PROFILE     \033[0m\033[94m|")
    print("-------------------------\033[0m\n")

    # Read user login data from login.txt
    with open('login.txt', 'r') as login_file:
        for line in login_file:
            login_data = line.strip().split(',')
            login_username = login_data[2]

            # Display data with only same username
            if login_username == username:
                first_name = login_data[0]
                last_name = login_data[1]
                address = login_data[3]
                password = login_data[4]

                # Display user data
                print(f"\033[1mFirst Name\033[0m : {first_name}\n\033[1mLast Name\033[0m  : {last_name}\n\033[1mContact No\033[0m : {username}\n\033[1mAddress\033[0m    : {address}\n")

def display_hour():
    clear_screen()

    # Title
    print("\n\033[94m----------------------------------")
    print("|        \033[1mBRANCH INFORMATION      \033[0m\033[94m|")
    print("----------------------------------\033[0m\n")

    # Read branch data from hour.txt
    with open('hour.txt', 'r') as hour_file:
        for line in hour_file:
            hours_data = line.strip().split(',')
            branch_id = hours_data[0]
            branch_name = hours_data[1]
            branch_address = hours_data[2]
            branch_phone = hours_data[3]
            operating_hours = hours_data[4]

            # Display branches details
            print("-------------")
            print("\033[33m  Branch #" + str(branch_id)+ "\033[0m")
            print("-------------")
            print(f"\033[1mBranch Name\033[0m    : {branch_name}\n\033[1mBranch Address\033[0m : {branch_address}\n\033[1mContact Number\033[0m : {branch_phone}\n\033[1mOpen Hours\033[0m     : {operating_hours}\n")

#################### ADMIN MAIN MENU FUNCTION ####################

def display_order():
    clear_screen()

    # Title
    print("\n\033[35m-------------------------------")
    print("|        \033[1mHISTORY ORDERS       \033[0m\033[35m|")
    print("-------------------------------\033[0m\n")
    
    count = 1

    # Read order data from order.txt
    with open('order.txt', 'r') as order_file:
        for line in order_file:
            order_data = line.strip().split(',')
            username = order_data[0]
            item_id = order_data[1]
            item_name = order_data[2]
            item_price = float(order_data[3])
            quantity = order_data[4]
            total = float(order_data[5])
            status = order_data[6]

            # Display history order
            print("------------------")
            print("\033[33m  Order No #"+str(count)+"\033[0m")
            print("------------------")
            print(f"\033[1mItem Name\033[0m : {item_name}\n\033[1mQuantity\033[0m  : {quantity}\n\033[1mTotal\033[0m     : RM{total:.2f}\n\033[1mOrder by\033[0m  : {username}\n\033[1mStatus\033[0m    : {status}\n")
            count += 1

def edit_order():
    clear_screen()

    # Select  to edit
    # Retrieved from order.txt
    # Select new status and overwrite into order.txt
    
    # Title
    print("\n\033[35m----------------------------------")
    print("|        \033[1mEDIT ORDER STATUS       \033[0m\033[35m|")
    print("----------------------------------\033[0m\n")

    count = 1

    # Read order data from order.txt
    with open('order.txt', 'r') as order_file:
        order_lines = order_file.readlines()
        total_orders = len(order_lines)
        for line in order_lines:
            order_data = line.strip().split(',')
            username = order_data[0]
            item_id = order_data[1]
            item_name = order_data[2]
            item_price = float(order_data[3])
            quantity = order_data[4]
            total = float(order_data[5])
            status = order_data[6]

            # Display order details
            print("------------------")
            print("\033[33m  Order No #"+str(count)+"\033[0m")
            print("------------------")
            print(f"\033[1mOrder by\033[0m : {username}\n\033[1mStatus\033[0m   : {status}\n")
            count += 1

        # Prompt user to input the order number to modify status
        order_number = int(input("Enter Order No that need to be modified: "))

        # Check if the order number is valid
        while order_number < 1 or order_number > total_orders:
            print("\n\033[91mOrder No not existed, please try again.\033[0m")
            order_number = int(input("Enter Order No that need to be modified : "))

        clear_screen()

        # Prompt user to input the new status
        print("\n\033[4m\033[1mStatus List:\033[0m\n1. Order Placed\n2. Preparing\n3. Cancelled\n4. Out of Delivery\n5. Delivered")
        status_no = int(input("\nEnter new status of the order: "))

        # Check if the status number is valid
        while int(status_no) < 1 or int(status_no) > 5:
            print("\n\033[91mInvalid status number, please try again.\033[0m")
            status_no = int(input("Enter new status of the order \033[91m[1-5]\033[0m : "))

        # Convert status number to status name
        if status_no == 1:
            new_status = "Order placed"
        elif status_no == 2:
            new_status = "Preparing"
        elif status_no == 3:
            new_status = "Cancelled"
        elif status_no == 4:
            new_status = "Out of Delivery"
        elif status_no == 5:
            new_status = "Delivered"

        # Update the status in order.txt
        updated_order_lines = []
        for i, line in enumerate(order_lines):
            order_data = line.strip().split(',')
            if i == order_number - 1:
                order_data[6] = new_status
            updated_order_lines.append(','.join(order_data) + '\n')

        # Write the updated order data into order.txt
        with open('order.txt', 'w') as order_file:
            order_file.writelines(updated_order_lines)

        clear_screen()

        # Display the success message
        print("\n\033[32mNew order status updated!\033[0m")

def delete_order():
    clear_screen()
    
    # Title
    print("\n\033[35m------------------------------")
    print("|        \033[1mDELETE ORDERS       \033[0m\033[35m|")
    print("------------------------------\033[0m\n")
    
    count = 1
    order_lines = []

    # Read order data from order.txt
    with open('order.txt', 'r') as order_file:
        order_lines = order_file.readlines()

    # Display all orders
    for line in order_lines:
        order_data = line.strip().split(',')
        username = order_data[0]
        item_name = order_data[2]
        quantity = order_data[4]
        total = float(order_data[5])
        status = order_data[6]

        # Display order details
        print("------------------")
        print("\033[33m  Order No #"+str(count)+"\033[0m")
        print("------------------")
        print(f"\033[1mItem Name\033[0m : {item_name}\n\033[1mQuantity\033[0m  : {quantity}\n\033[1mTotal\033[0m     : RM{total:.2f}\n\033[1mOrder by\033[0m  : {username}\n\033[1mStatus\033[0m    : {status}\n")
        count += 1

    # Prompt user to input the order number to delete
    order_number = int(input("Enter the order number that you wish to delete : "))

    # Check if the order number is valid
    while order_number < 1 or order_number > len(order_lines):
        print("\n\033[91mInvalid order number, please try again.\033[0m")
        order_number = int(input("Enter the order number that you wish to delete : "))

    # Remove the selected order from the list
    deleted_order = order_lines.pop(order_number - 1)

    # Save the updated orders back to order.txt
    with open('order.txt', 'w') as order_file:
        order_file.writelines(order_lines)

    clear_screen()
    
    # Display the success message
    print("\n\033[32mOrder deleted successfully!\033[0m")

def search_cust():
    clear_screen()
    
    ans = 'y'

    while ans == 'Y' or ans == 'y':
        
        # Title
        print("\n\033[35m--------------------------------------------")
        print("|        \033[1mSEARCH CUSTOMER INFORMATION       \033[0m\033[35m|")
        print("--------------------------------------------\033[0m\n")   

        # Prompt admin to input the username to search
        username = input("Enter customer Contact No to retrieve info \033[91m(Format:01XXXXXXXX)\033[0m : ")

        # Read order data from login.txt
        with open('login.txt', 'r') as login_file:
            found = False
            for line in login_file:
                login_data = line.strip().split(',')
                login_username = login_data[2]

                # Display record with only same username
                if login_username == username:
                    first_name = login_data[0]
                    last_name = login_data[1]
                    address = login_data[3]
                    password = login_data[4]

                    # Display record
                    print("\n---------------------------")
                    print("\033[33mInfo of Cust ID #"+str(username)+"\033[0m")
                    print("---------------------------")
                    print(f"\033[1mFirst Name\033[0m: {first_name}\n\033[1mLast Name\033[0m: {last_name}\n\033[1mContact Number\033[0m: {username}\n\033[1mAddress\033[0m: {address}\n")

                    found = True

            # Prompt user to do another search
            ans = input("Press \033[91m[Y]\033[0m if you want to do another search, or any key to return to the main menu: ")
            clear_screen()
                    
            if not found:
                print("\n\033[91mNo record found, press [Enter] to try again.\033[0m")
                getchar = input()
                clear_screen()
                search_cust()

def add_item():
    ans = 'y'
    count = 0
    
    while ans == 'y' or ans == 'Y':
        clear_screen()
        
        # Title
        print("\n\033[35m---------------------------------")
        print("|          \033[1mADD MENU ITEM        \033[0m\033[35m|")
        print("---------------------------------\033[0m\n")
        
        item_id = input("Enter item ID          : ")

        with open("menu.txt", "r") as file:
            for line in file:
                existing_id = line.strip().split(",")[0]
                if existing_id == item_id:
                    print("\n\033[91mItem ID already exists. Please try again.\033[0m")
                    getchar = input("Press [Enter] to continue...")
                    add_item()
                    return
            else:
                # Item ID is unique
                item_name = input("Enter item name        : ")
                item_price = round(float(input("Enter item price       : RM")), 2)
                item_desc = input("Enter item description : ")

                with open("menu.txt", "a") as file:
                    file.write(f"{item_id},{item_name},{item_price},{item_desc}\n")

                count += 1

                clear_screen()

                print("\n\033[32mItem added successfully!\033[0m\n")
                print("----------------------------")
                print("\033[33m  Details of Item ID #" + item_id + "\033[0m")
                print("----------------------------")
                print("\033[1mItem Name       \033[0m : " + item_name)
                print("\033[1mItem Price\033[0m       : RM{:.2f}".format(item_price))
                print("\033[1mItem Description\033[0m : " + item_desc+"\n")

        ans = input("Press [Y] to add another item, or any other key to exit: ")

    clear_screen()

    print("\033[32mYou have successfully add " + str(count) + " item(s) into the system.\033[0m")

def display_item():
    clear_screen()
    
    # Title
    print("\n\033[35m--------------------------------------")
    print("|          \033[1mDISPLAY  MENU ITEM        \033[0m\033[35m|")
    print("--------------------------------------\033[0m\n")    
    
    count = 1

    # Read from the menu.txt file
    with open("menu.txt", "r") as file:
        for line in file:
            # Remove blank
            line = line.strip()

            # Seperate data
            item_id, item_name, item_price, item_desc, = line.split(",")

            # Display data
            print("-----------------")
            print("\033[33m  Item ID #"+str(item_id)+"\033[0m")
            print("-----------------")
            print("\033[1mItem Name       \033[0m : "+item_name)
            print("\033[1mItem Price      \033[0m : RM{:.2f}".format(float(item_price)))
            print("\033[1mItem Description\033[0m : "+item_desc + "\n")

            # Increase count
            count = count + 1

    # Close the file
    file.close()

def edit_item():
    ans = 'y'
    
    while ans == 'y' or ans == 'Y':
        
        clear_screen()
        
        # Title
        print("\n\033[35m-------------------------------")
        print("|        \033[1mEDIT MENU PRICE      \033[0m\033[35m|")
        print("-------------------------------\033[0m\n") 
    
        item_id = input("Enter Item ID: ")

        # Read the contents of menu.txt file
        with open("menu.txt", "r") as file:
            lines = file.readlines()

        found = False

        # Search for the item ID in the file
        for i, line in enumerate(lines):
            data = line.strip().split(",")
            if data[0] == item_id:
                found = True
                old_price = round(float(data[2]), 2)
                new_price = round(float(input("Please enter new item price: RM")), 2)
                lines[i] = f"{data[0]},{data[1]},{new_price},{data[3]}\n"
                break

        # If item ID not found, ask user to re-enter
        if not found:
            print("\n\033[91mItem ID not found. Please enter a valid item ID.\033[0m")
            getchar = input("Press [Enter] to continue...")
            edit_item()
            return

        # Write the updated contents back to menu.txt file
        with open("menu.txt", "w") as file:
            file.writelines(lines)

        clear_screen()

        print("\n\033[32mItem price updated successfully!\033[0m\n")
        #print("\033[1mOld price \033[0m: RM" + str(old_price))
        print("\033[1mOld price\033[0m : RM{:.2f}".format(old_price))
        print("\033[1mOld price\033[0m : RM{:.2f}".format(new_price))
        #print("\033[1mNew price \033[0m: RM" + str(new_price))

        ans = input("\nPress [Y] to edit another item, or any other key to exit to main menu: ")

def delete_item():
    ans = 'y'
    
    while ans == 'y' or ans == 'Y':
        clear_screen()
        
        # Title
        print("\n\033[35m-------------------------------")
        print("|        \033[1mDELETE MENU ITEM      \033[0m\033[35m|")
        print("-------------------------------\033[0m\n") 
        
        item_id = input("Enter Item ID: ")

        # Read the contents of menu.txt file
        with open("menu.txt", "r") as file:
            lines = file.readlines()

        found = False

        # Search for the item ID in the file
        for i, line in enumerate(lines):
            data = line.strip().split(",")
            if data[0] == item_id:
                found = True
                del lines[i]
                break

        # If item ID not found, ask user to re-enter
        if not found:
            print("\n\033[91mItem ID not found. Please enter a valid item ID.\033[0m")
            getchar = input("Press [Enter] to continue...")
            delete_item()
            return

        # Write the updated contents back to menu.txt file
        with open("menu.txt", "w") as file:
            file.writelines(lines)

        clear_screen()

        print("\033[32mItem ID #"+data[0]+" deleted successfully!\033[0m")
        
        ans = input("\nPress [Y] to delete another item, or any other key to exit to main menu: ")


def add_branch():
    ans = "Y"

    while ans == "Y" or ans == "y":
        clear_screen()
        
        # Title
        print("\n\033[35m-----------------------------")
        print("|       \033[1mADD NEW BRANCH      \033[0m\033[35m|")
        print("-----------------------------\033[0m\n") 
        
        # Ask for branches details
        branch_ID = input("Enter Branch ID   : ")
        
        with open("hour.txt", "r") as file:
            for line in file:
                exist_id = line.strip().split(",")[0]
                if exist_id == branch_ID:
                    print("\n\033[91mBranch ID already exist. Please enter a valid branch ID.\033[0m")
                    getchar = input("Press [Enter] to continue...")
                    add_branch()
                    return
            else:
                branch_name = input("Enter Branch Name : ")
                address = input("Enter Address (without comma ',')   : ")
                phone = input("Enter Phone Number (01X-XXXXXXX)     : ")
                hours = input("Enter Operating Hours (XX:XX-XX:XX) : ")

                # Open and write to file menu.txt
                with open("hour.txt", "a") as file:
                    file.write(f"{branch_ID},{branch_name},{address},{phone},{hours}\n")

                # Close the file
                file.close()
                
                clear_screen()

                # Display success message and info, then ask if admin wants to add another item
                print("\n\033[32mNew branch added successfully!\033[0m\n")
                print("-------------------------")
                print("\033[33m Details of Branch ID #" + branch_ID + "\033[0m")
                print("-------------------------")
                print("\033[1mBranch Name     \033[0m: " + branch_name)
                print("\033[1mAddress         \033[0m: " + address)
                print("\033[1mContact Number  \033[0m: " + phone)
                print("\033[1mOperating Hours \033[0m: " + hours)

        # Ask if admin wants to add another item
        ans = input("\nPress [Y] to add another branch, or any key to return to main menu: ")

def admin_display_hour():
    clear_screen()

    # Title
    print("\n\033[35m----------------------------------")
    print("|        \033[1mBRANCH INFORMATION      \033[0m\033[35m|")
    print("----------------------------------\033[0m\n")

    # Read branch data from hour.txt
    with open('hour.txt', 'r') as hour_file:
        for line in hour_file:
            hours_data = line.strip().split(',')
            branch_id = hours_data[0]
            branch_name = hours_data[1]
            branch_address = hours_data[2]
            branch_phone = hours_data[3]
            operating_hours = hours_data[4]

            # Display branches details
            print("-------------")
            print("\033[33m  Branch #" + str(branch_id)+"\033[0m")
            print("-------------")
            print(f"\033[1mBranch Name\033[0m    : {branch_name}\n\033[1mBranch Address\033[0m : {branch_address}\n\033[1mContact Number\033[0m : {branch_phone}\n\033[1mOpen Hours\033[0m     : {operating_hours}\n")

def adjust_hour():
    ans="y"
    
    while ans == "y" or ans == "Y":
        clear_screen()

        # Title
        print("\n\033[35m----------------------------")
        print("|     \033[1mUPDATE OPEN HOURS    \033[0m\033[35m|")
        print("----------------------------\033[0m\n") 
        

        with open('hour.txt', 'r') as hours_file:
            hours_lines = hours_file.readlines()
            hours = len(hours_lines)
            for line in hours_lines:
                hours_data = line.strip().split(',')
                branch_id = hours_data[0]
                branch_name = hours_data[1]
                branch_address = hours_data[2]
                branch_phone = hours_data[3]
                operating_hours = hours_data[4]

                # Display branches details
                print("------------------")
                print("\033[33m  Branch #" + str(branch_id)+"\033[0m")
                print("------------------")
                print(f"\033[1mBranch Name\033[0m: {branch_name}\n\033[1mCurrent Operating Hours\033[0m: {operating_hours}\n")

            # Prompt user to input the order number to modify status
            option = int(input("Enter Branch ID that need to be modified: "))

            # Check if the Branch ID is valid
            while option < 1 or option > hours:
                print("\n\033[91mInvalid ID, please try again\033[0m")
                option = int(input("Enter Branch ID that need to be modified: "))

            # Prompt user to input the new status
            new_hours = input("Enter new operating hours \033[91m(xx:xx-xx:xx)\033[m: ")

            # Update the status in hour.txt
            updated_hours_lines = []
            for i, line in enumerate(hours_lines):
                hours_data = line.strip().split(',')
                if i == option - 1:
                    hours_data[4] = new_hours
                updated_hours_lines.append(','.join(hours_data) + '\n')

            with open('hour.txt', 'w') as order_file:
                order_file.writelines(updated_hours_lines)

            clear_screen()

            print("\n\033[32mOperating hours of Branch ID #" + str(branch_id)+ " was updated!\033[0m")
            print("\033[1mOld Operating Hours \033[0m: " + operating_hours)
            print("\033[1mNew Operating Hours \033[0m: " + new_hours)
            
            ans = input("\nPress [Y] to update another branch, or any other key to return to main menu: ")

def admin_function():
    clear_screen()
    # Declare variable
    choice = 1

    # Display Admin Page Menu
    print("\n\033[35m---------------------------")
    print("|        \033[1mADMIN PAGE       \033[0m\033[35m|")
    print("---------------------------\033[0m\n")

    # Ask admin to enter credential
    a_username = input("Enter admin username : ")
    a_password = input("Enter admin password : ")

    # Check admin credential
    # Username: admin
    # Password: admin123
    while a_username != "admin" or a_password != "admin123":
        print("\n\033[91mWrong username or password, please try again!\033[0m")
        a_username = input("Enter admin username: ")
        a_password = input("Enter admin password: ")

    # Login Successful, Enter Admin Main Menu
    print("\n\033[32mAdmin page login successful, press any key to continue...\033[0m")
    getchar = input()

    clear_screen()

    # Keep looping the menu until user terminate the program
    while choice != 13:

        # Display Admin Main Menu
        print("\n\033[35m--------------------------------")
        print("|        \033[1mADMIN MAIN MENU       \033[0m\033[35m|")
        print("--------------------------------\033[0m\n")
        print("[1]  Display All Customer Order")
        print("[2]  Edit Customer Order Status")
        print("[3]  Delete Customer Order")
        print("[4]  Search Customer Information\n")
        print("[5]  Add Menu Item")
        print("[6]  Display All Menu Item")
        print("[7]  Edit Menu Item Price")
        print("[8]  Delete Menu Item\n")
        print("[9]  Add New Branches and information")
        print("[10] Display All Restaurant Branch Info and Operating Hours")
        print("[11] Adjust Restaurant Operating Hours\n")
        print("[12] Logout")
        print("[13] Exit\n")

        # Ask user to select option
        choice = int(input("Enter your choice \033[91m[1-13]\033[0m : "))

        # Do the Action Based on Selected Option
        if choice == 1:
            # This is to display all customer order
            display_order()
            print("Press any key to return to main menu...")
            getchar = input()
            clear_screen()
        elif choice == 2:
            # This is to edit customer order status
            edit_order()
            print("Press any key to return to main menu...")
            getchar = input()
            clear_screen()
        elif choice == 3:
            # This is to delete customer order
            delete_order()
            print("Press any key to return to main menu...")
            getchar = input()
            clear_screen()
        elif choice == 4:
            # This is to search customer order
            search_cust()
            clear_screen()
        elif choice == 5:
            # This is to add menu item
            add_item()
            print("Press any key to return to main menu...")
            getchar = input()
            clear_screen()
        elif choice == 6:
            # This is to display all menu item
            display_item()
            print("Press any key to return to main menu...")
            getchar = input()
            clear_screen()
        elif choice == 7:
            # This is to edit menu item price
            edit_item()
            clear_screen()
        elif choice == 8:
            # This is to delete menu item
            delete_item()
            clear_screen()
        elif choice == 9:
            # This is to add new brances and information
            add_branch()
            clear_screen()
        elif choice == 10:
            # This is to display all branch info
            admin_display_hour()
            print("Press any key to return to main menu...")
            getchar = input()
            clear_screen()
        elif choice == 11:
            # This is to adjust restaurant operating hours
            adjust_hour()
            clear_screen()
        elif choice == 12:
            clear_screen()
            print("\nLogging out, press any key to continue...")
            getchar = input()
            main()
        elif choice == 13:
            # This is to terminate the program
            print("Thank you for using the service, have a nice day.")
            exit(0)
        else:
            # Invalid Code --> Ask user to re-enter the code again
            print("\n\033[91mInvalid code, please try again.\033[0m ")
            print("Press any key to return to continue...")
            getchar = input()

def main():
    #################### SUPER MAIN HYPER MAIN HERE ####################
    # Display Menu
    clear_screen()
    print("\033[94m-------------------------------------------------------")
    print("\t\033[1mWELCOME TO RESTAURANT DELIVERY SYSTEM\033[0m")
    print("\033[94m-------------------------------------------------------\033[0m")
    print("[1] User")
    print("[2] Admin")
    print("[3] Exit\n")

    # Ask user to select option
    answer = int(input("Select your role \033[91m[1-3]\033[0m : "))

    # Check user input
    while answer > 3 or answer < 1:
        answer = int(input("\n\033[91mWrong code input, please try again [1-3]\033[0m : "))

    # Jump to selected option
    if answer == 1:
        user_function()

    elif answer == 2:
        admin_function()
        
    elif answer == 3:
        print("\nThank you for using the service, have a nice day :)")
        exit(0)

# Call main function
main()