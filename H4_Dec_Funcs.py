# Homework 4: Numeric Processing
# Program By: Tyler Serio
# File Name: H4_Dec_Funcs.py
# Function: This program displays decorated (fancy) calculator functions

def menu():
    """This function is the main menu of the program"""
    while True:
        print("Choose an operation:")
        print("[1] - Add")
        print("[2] - Subtract")
        print("[3] - Multiply")
        print("[4] - Divide")
        print("[0] - Quit")
        choice = input("> ")
        calc(choice)

def decor1(func):
    """This function lets the user know which action is being performed"""
    def prettier(a, b):
        if func.__name__ == "add":
            print("Performing addition!")
        if func.__name__ == "sub":
            print("Performing subtraction!")
        if func.__name__ == "mult":
            print("Performing multiplication!")
        if func.__name__ == "div":
            print("Performing division!")
        return func(a, b)
    return prettier

def decor2(func):
    """This function lets the user know that a certain input is invalid"""
    def prettier(x):
        if x == "1" or x == "2" or x == "3" or x == "4" or x == "0":
            return func(x)
        else:
            print("That is not a proper choice. Please choose from the listed options.")
            print("")
            return None
    return prettier
    
def get_operand():
    """This function collects two operands for the calculations"""
    while True:
        x = input("Enter an operand: ")
        if x.isdigit() == True:
            break
        else:
            print("That is not a proper value, please enter a number.")
            print("")
    while True:
        y = input("Enter another operand: ")
        if y.isdigit() == True:
            break
        else:
            print("That is not a proper value, please enter a number.")
            print("")
    return int(x), int(y)

@decor1
def add(x, y):
    """This function adds two operands together"""
    z = x + y
    return z

@decor1
def sub(x, y):
    """This function subtracts one operand from another"""
    z = x - y
    return z

@decor1
def mult(x, y):
    """This function multiplies two operands"""
    z = x * y
    return z

@decor1  
def div(x, y):
    """This function divides one operand by another"""
    z = x / y
    return z

@decor2      
def calc(x):
    """This function performs the calculations"""
    if x == "0":
        print("Good Bye!!")
        exit()
    elif x == "1" or x == "2" or x == "3" or x == "4":     
        a, b = get_operand()
        if x == "1":
            print("Your result is " + str(add(a, b)))
            print("")
        if x == "2":
            print("Your result is " + str(sub(a, b)))
            print("")       
        if x == "3":
            print("Your result is " + str(mult(a, b)))
            print("")    
        if x == "4":
            print("Your result is " + str(div(a, b)))
            print("")
            
menu()

