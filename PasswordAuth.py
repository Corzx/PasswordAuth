import getpass
import emoji

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
            print("Access denied.")
            break
    else:
        print(emoji.emojize("Username does not exist. :stop_sign:"))
        break
