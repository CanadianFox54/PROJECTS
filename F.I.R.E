import datetime
usermaker = input("Create your username: ")
passwordmaker = input("Create your password: ")

passwordlength = len(passwordmaker)

if passwordlength < 4:
    print("Password must be at least 4 characters long.")
else:
    user = input("Please enter your username: ")
    password = input("Please enter your password: ")

    if usermaker == user and passwordmaker == password:
        Enter = True
    elif usermaker != user and passwordmaker != password:
        print("Username and password are not correct.")
        Enter = False
    elif usermaker != user or passwordmaker != password:
        print("Username or password is not correct.")
        Enter = False

if Enter == True:
    print("Welcome to your computer")
    name = input("To verify it is you please state your name: ")
    birth = input("for extra verifacation please state your date of birth (please use numbers): ")
    info = input("If this infomation is correct plese type yes:")
    if info == "yes":
        print("Thank you for your verifacation.")
        verify = True
    elif info == "no":
        print("Please restart the program.")
        verify = False
    else:
        print("Please only enter yes or no.")
        verify = False

    if verify == True:
        app_selection = input("You have got TWO apps installed please chose either: calculator or calander")
        if app_selection == "calculator":
            calculator_selection = input("Times, Divide, Add, Subtract.")
            if calculator_selection == "times":
                num1 = int(input("please enter your first number: "))
                num2 = int(input("please enter your second  number: "))
                num_A = num1 * num2
                print(num_A)
            if calculator_selection == "divide":
                num1 = int(input("please enter your first number: "))
                num2 = int(input("please enter your second  number: "))
                num_A = num1 / num2
                print(num_A)
            if calculator_selection == "add":
                num1 = int(input("please enter your first number: "))
                num2 = int(input("please enter your second  number: "))
                num_A = num1 + num2
                print(num_A)
            if calculator_selection == "subtract":
                num1 = int(input("please enter your first number: "))
                num2 = int(input("please enter your second  number: "))
                num_A = num1 - num2
                print(num_A)
        if app_selection == "calander":
            current_datetime = datetime.datetime.now()
            print("Current Date and Time:", current_datetime)



else:
    exit()
