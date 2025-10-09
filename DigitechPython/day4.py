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

print()










#Login System with Access Control

# Step 1: Store users and their details
users = {
    "shaniz": {"password": "shaniz123@", "role": "user"},
    "Maxwell": {"password": "Maxwell2025", "role": "admin"},
    "guest": {"password": "guest123", "role": "guest"}
}

# Step 2: Login
print("LOGIN PAGE")
username = input("Enter username: ")
password = input("Enter password: ")

# Step 3: Check credentials
if username in users and users[username]["password"] == password:
    role = users[username]["role"]
    print(f"\nWelcome, {username}! You are logged in as a {role}.\n")

    # Step 4: Display menu
    print("=== MAIN MENU ===")
    print("1. View Profile")
    print("2. Admin Panel")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    # Step 5: Menu actions
    if choice == "1":
        print("\n--- Profile ---")
        print(f"Name: {username}")
        print(f"Role: {role}")

    elif choice == "2":
        if role == "admin":
            print("\n--- Admin Panel ---")
            print("Access granted! You have full control.")
        else:
            print("\nAccess Denied! Only admins can view this section.")

    elif choice == "3":
        print("\nGoodbye! Logging out...")
    else:
        print("\nInvalid choice!")

else:
    print("\n❌ Invalid username or password. Please try again.")
