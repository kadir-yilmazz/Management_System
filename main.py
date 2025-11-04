import functions
import os
os.makedirs("PMS", exist_ok=True)

while True:
    choice = functions.main_menu() #Main Menu
    if choice == "1":# User Login
        username = functions.user_login()
        if username:
            while True:
                print("\n--- User Panel ---")
                print("1. Logout to Main Menu")
                user_choice = input("Please choose an option: ")

                if user_choice == "1":
                    functions.quit_session(username)
                    break

    elif choice == "2": # Admin Login
        admin_name = functions.admin_login()
        if admin_name:
            while True:
                print("\n--- Admin Panel ---")
                print("1. Logout to Main Menu")
                admin_choice = input("Please choose an option: ")

                if admin_choice == "1":
                    functions.quit_session(admin_name)
                    break

    elif choice == "3": # Quit
        print("Quitting the program. Goodbye!")
        break

    else: # Invalid option
        print("Invalid option. Please try again.")