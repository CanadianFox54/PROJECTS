password_min_length = 7

user_maker = input("create a username")
password_maker = input("create a password")

while len(password_maker) < password_min_length:
    print (f"password must be {password_min_length} characters long")
    password_maker = input("create a password")

while True:
    user = input("enter your username")
    password = input("enter your password")

    if user == user_maker and password == password_maker:
        print("welcome")
        break
    else:
        print("username or password is incorrect")