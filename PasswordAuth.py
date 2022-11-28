import getpass

database = {"cDeponte": "abc123", "jDeponte": "tallyho", "aDeponte": "yahoo"}
username = input("Please enter your username: ")
password = getpass.getpass("Please enter your password: ")

for user in database.keys():
    if username == user:
        while password != database.get(user):
            password = getpass.getpass("Please try again: ")
            print("Access denied.")
            break
        if password in database.values():
            print("Entry granted")
            break
    else:
        print("Username does not exist.")
        break
