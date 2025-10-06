# this program checks on thr user inputs and validates it
print("this program needs the credentials to verify this to grant acces to users")
print()

username = input("Enter your username: ")
password = input("Enter your password: ")


if username == "Maxwell" and password == "Maxwell2025":
    print("Access granted")

elif username != "Maxwell" and password == "Maxwell2025":
    print("Access granted")
    
else:
    print("Wrong credentials, access denied")
