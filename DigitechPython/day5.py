# we are perdorming teh for loop in our program

for number in range(0,10):
    if number %2 ==1:
        print(number)

# we are performing the while loop in our program

trial=3
attempt=0
while attempt<trial:
    value=input("Enter the Password: ")
    if value=="Maxwell2025":
        print("Login successful")
        break
    else:
        print("Your password is wrong try again")
        attempt+=1
else:
    print("You failed your login attempts are over")
