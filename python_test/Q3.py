correct_password = "Python123"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    user_input = input("Enter password:")
    if user_input == correct_password:
        print("Access Granted.")
        break
    else:
        attempts += 1

if attempts == max_attempts:
    print("Access Denied. Try again Later.")