# Registration function
account = {}

def UserRegistration():
        try:
            user = input("Enter a username: ")
            passwd = input("Enter a password: ")
            print('-' * 40)

            account["user"] = user
            account["password"] = passwd

            with open('users.txt', 'a', encoding='utf-8') as WriteUser:
                WriteUser.writelines(f"{user},{passwd}\n")
                print("Registered Successfully")
        except ValueError:
            print("")

# Login function
def UserLogin():
    try:
        user = input("Enter a username: ")
        passwd = input("Enter a password: ")
        print('-' * 40)

        with open('users.txt', 'r', encoding='utf-8') as WriteUser:
            for line in WriteUser:
                registered_user, registered_password = line.strip().split(',')

                if user == registered_user and passwd == registered_password:
                    print("Login Successfully \n")
                    return
            print("Login Failed. Try again.")
    except ValueError:
        print("")

