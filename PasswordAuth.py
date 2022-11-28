import getpass

database = {"cDeponte": "abc123", "jDeponte": "tallyho", "aDeponte": "yahoo"}
username = input("Please enter your username: ")
password = getpass.getpass("Please enter your password: ")

for user in database.keys():
    if username == user:
        while password != database.get(i):
            password = getpass.getpass("Please try again: ")
        break

print("Entry granted")
