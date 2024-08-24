"""
Exercise 1: User Authentication System
Objective: Implement a basic user authentication system.

Instructions:

User Registration:

Ask the user to input a username and password.
Store the username and a hashed version of the password in a dictionary.
Save the dictionary to a file (users.txt) using file handling.
User Login:

Ask the user to input a username and password.
Verify the username and password by checking the stored dictionary.
Use conditional statements to validate the login credentials.
Error Handling:

If the file doesn't exist when trying to read the user data, handle the FileNotFoundError and create a new file.
Handle incorrect login attempts and raise custom exceptions if the username is not found or the password is incorrect.
"""

account = {}

# Registration function
def UserRegistration():
        try:
            user = input("Enter a username: ")
            passwd = input("Enter a password: ")
            print('-' * 40)

            account["user"] = user
            account["password"] = passwd

            with open('users.txt', 'a', encoding='utf-8') as WriteUser:
                WriteUser.writelines([account["user"], ",", account["password"], "\n"])
                print("Registered Successfully")
                for line in WriteUser:
                    line = line.strip()
                    account["user"], account["password"] = line.split(',')
        except ValueError:
            print("")

# Login function
def UserLogin():
    try:
        user = input("Enter a username: ")
        passwd = input("Enter a password: ")
        print('-' * 40)

        account["user"] = user
        account["password"] = passwd

        with open('users.txt', 'r', encoding='utf-8') as WriteUser:

            for line in WriteUser:
                line = line.strip()
                account["user"], account["password"] = line.split(',')

        if user == account["user"] and passwd == account["password"]:
            print("Login Successfully \n")
        else:
            print("Log in Failed. Try Again")
            print('-' * 40)
    except ValueError:
        print("")


# Main function
def main():
    # printing the menu options
    print("Menu: ")
    print("1. Register an Account")
    print("2. Log in")
    print("0. Exit")
    print('-'*40)
    # while true the system will continue asking choose an option
    while True:
        try:
            user = int(input("Choose an option (1-2): "))
            print('-'*40)

            if user not in [1,2,0]:
                print("Invalid input. Please try again")
                print('-'*40)
                continue

            if user == 1:
                UserRegistration()
                continue
            elif user == 2:
                UserLogin()
            else:
                break
        except ValueError:
            print("Invalid Input. Enter a valid Value!.")
            print('-' * 40)

main()