# Homework 3: User Login
# Program By: Tyler Serio
# File Name: H3_Login.py
# Function: This program will authenticate user access

users = {"1": ["Mikey", "pizzatime", "standard"],
         "2": ["Donny", "halfshell", "standard"],
         "3": ["Raph", "shredhead", "standard"],
         "4": ["Leo", "cowabunga", "admin"]}

def verify():
    print("Hello!!")
    while True:
        print("Do you have an account?!")
        print("[y] - yes, [n] - no, [e] - exit")
        answer = input()
        if answer == "e":
            exit()
        if answer == "n":
            print("Please enter your desired username:")
            name = input(" > ")
            print("Please enter your desired password:")
            password = input("> ")
            print("Thank you, your information has been stored.")
            print("")
            users.update({str(len(users) + 1): [name, password, "standard"]})
        elif answer == "y":
            print("Please enter your username:")
            uname = input("> ")
            print("Please enter your password:")
            upassword = input("> ")
            # if info found
            userid = 1
            while True:
                if uname == str(users[str(userid)][0]) and upassword == users[str(userid)][1]:
                    if users[str(userid)][2] == "standard":
                        print("")
                        print("ACCESS GRANTED: Welcome to the Secret Sewer System, dude!")
                        print("")
                    if users[str(userid)][2] == "admin":
                        print("")
                        print("COWABUNGA, DUDE!!")
                        print("ADMIN ACCESS GRANTED: Welcome to the Secret Sewer System, dude!")
                        print("Here are the current users:")
                        print("UserID    Username    Password    Role")
                        for key in users:
                            print(key + "    " + users[key][0]+ "    " + users[key][1]+ "    " + users[key][2])
                        print("")
                    break
                userid += 1
                if userid > len(users):
                    print("")
                    print("ACCESS DENIED, DUDE!!")
                    break      
        else:
            print("")
            print("You must select a proper choice!")
verify()
