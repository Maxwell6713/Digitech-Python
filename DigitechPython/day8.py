 # defining a function
# def get_pass(name, age):
#     if age <= 17:
#         return f"{name}, you are not allowed to enter the club."
#     else:
#         return f"{name}, you are allowed to enter the club."
    
#     # generate the actual name and age
# user_name = input("Enter your name: ")
# user_age = int(input("Enter your age: "))

# final = get_pass(user_name, user_age)
# print(final)





def get_access():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    if age <= 17:
        print (f"{name}, you are not allowed to enter the club.")
    else:
        print (f"{name}, you are allowed to enter the club.")

get_access() 