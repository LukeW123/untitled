# Luke's Project 27/01/2020
'''

print("Hello, this is my project.")



x = 1
if x == 1:
     print("x is 1.")

myint = 7
print(myint)

myfloat = 7.0
print(myfloat)
myfloat = float(7)
print(myfloat)

mystring = 'hello'
print(mystring)
mystring = "hello"
print(mystring)

mystring = "Hello"
myfloat = 10.0
myint = 20

if mystring == "Hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.00:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print ("Integer: %d" % myint)



mylist = []
mylist.append(1)
mylist.append(2)'''
#Import Section
import tkinter.messagebox
import sys
import math
'''def again():
    print("Would you like to calculate again, Yes or No?")'''
#Functions
def Again():
    # Options
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square")
    print("6. Square Root")
    print("7. Exit")

    # User Input for options
    choice = input("Please select one of the following options:   ")

    if choice == '7':
        print("Goodbye!")
        sys.exit()

    # User input for calculator

    # If and else statements for the selecting the choice.
    while choice:

        if choice == '1':
            num1 = float(input("Please select your first number:  "))
            num2 = float(input("Please select your second number:  "))
            print(num1, "+", num2, "=", Add(num1, num2))
            Play_again()
        elif choice == '2':
            num1 = float(input("Please select your first number:  "))
            num2 = float(input("Please select your second number:  "))
            print(num1, "-", num2, "=", Sub(num1, num2))
            Play_again()
        elif choice == '3':
            num1 = float(input("Please select your first number:  "))
            num2 = float(input("Please select your second number:  "))
            print(num1, "x", num2, "=", Mul(num1, num2))
            Play_again()
        elif choice == '4':
            num1 = float(input("Please select your first number:  "))
            num2 = float(input("Please select your second number:  "))
            print(num1, "/", num2, "=", Div(num1, num2))
            Play_again()
        elif choice == '5':
            num1 = float(input("Please enter the number you would like to square:  "))
            print(num1, "**", num1, "=", Square(num1))
            Play_again()
        elif choice == '6':
            num1 = float(input("Please enter the number you would like to find the square root of:  "))
            print(math.sqrt(num1))
            Play_again()
        else:
            print("Invalid Input!")
            Again()

    ''''again()

    again = str(input("    "))

    if again == 'Yes':


    elif again == 'No':
        sys.exit()'''
    # Function which has a while loop to ask to calculate again.
    Play_again()
def Add(x, y):
    return x + y


def Sub(x, y):
    return x - y


def Mul(x, y):
    return x * y


def Div(x, y):
    return x / y

#Square function
def Square(x):
    return x*x

def SquareRoot():
    return



def Exit():
    sys.exit()

def Invalid():
    return

def Calculate():
    return Play_again()

def Play_again():
    while True:
        while True:
            answer = input("Calculate again ? Yes/No: ").upper()

            if answer in ('YES', 'NO'):
                break
            print('Invalid input.')
        if answer == 'YES':
            Again()
        elif answer == 'NO':
            print("Goodbye!")
            sys.exit()
        else:
            continue




username = input("Please Create a Username:  ")
password = input("Please Create a Password:  ")




#tkinter.messageboxshowinfo("Welcome to the Calculator!")
#Options
tkinter.messagebox.showinfo("Calculator","Welcome!!")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Square")
print("6. Square Root")
print("7. Exit")

#User Input for options
choice = input("Please select one of the following options:   ")

if choice == '7':
    print("Goodbye!")
    sys.exit()


# User input for calculator



#If and else statements for the selecting the choice.
while choice:

    if choice == '1':
        num1 = float(input("Please select your first number:  "))
        num2 = float(input("Please select your second number:  "))
        print(num1, "+", num2, "=", Add(num1, num2))
        Play_again()
    elif choice == '2':
        num1 = float(input("Please select your first number:  "))
        num2 = float(input("Please select your second number:  "))
        print(num1, "-", num2, "=", Sub(num1, num2))
        Play_again()
    elif choice == '3':
        num1 = float(input("Please select your first number:  "))
        num2 = float(input("Please select your second number:  "))
        print(num1, "x", num2, "=", Mul(num1, num2))
        Play_again()
    elif choice == '4':
        num1 = float(input("Please select your first number:  "))
        num2 = float(input("Please select your second number:  "))
        print(num1, "/", num2, "=", Div(num1, num2))
        Play_again()
    elif choice == '5':
        num1 = float(input("Please enter the number you would like to square:  "))
        print(num1, "**", num1, "=", Square(num1))
        Play_again()
    elif choice == '6':
        num1 = float(input("Please enter the number you would like to find the square root of:  "))
        print(math.sqrt(num1))
        Play_again()
    else:
        print("Invalid Input!")
        Again()





''''again()

again = str(input("    "))

if again == 'Yes':
    

elif again == 'No':
    sys.exit()'''
#Function which has a while loop to ask to calculate again.
Play_again()