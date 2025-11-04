import os

#To print main menu and continue to next menu(Ayşenur)
def main_menu():
    print("\n----Main Menu----")
    print("1. User Login")
    print("2. Admin Login")
    print("3. Quit")
    selection = input("Please select an option: ")
    return selection

#To login as a user and check for password and username(Ayşenur)
def user_login():
    username=input("Enter your username: ")
    password=input("Enter your password: ")
    try:
        with open("PMS/users.txt", "r",encoding="utf8") as user:
            for line in user:
                parts=line.strip().split("-")
                if len(parts)==2:
                    correct_username, correct_password = parts
                    if username == correct_username and password == correct_password:
                        print(f"----Welcome {username} !----")
                        return username
        print("Incorrect username or password")
    except FileNotFoundError:
        print("Error: 'PMS/users.txt' file not found")

#To login as a admin and check for password and usernmae(Ayşenur)
def admin_login():
    username=input("Enter your username: ")
    password= input("Enter your password: ")
    try:
        with open("PMS/admins.txt", "r",encoding="utf8") as admin:
            for line in admin:
                parts=line.strip().split("-")
                if len(parts)==2:
                    correct_admin_username, correct_admin_password = parts
                    if username == correct_admin_username and password == correct_admin_password:
                        print(f"----Welcome {username} !----")
                        return username
        print("Incorrect username or password")
    except FileNotFoundError:
        print("Error: 'PMS/admins.txt' file not found")

#To quit seesion for both user and admin(Ayşenur)
def quit_session(username):
    if username:
        print(f"----{username} has logged out successfully.----")
    else:
        print("Quitting the program. Goodbye!")
