import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def exponent(x, y):
    return (x ** y)

def sqrt(x):
    return(x)**(1/2)

def nthroot(x, y):
    return pow(y,(1/x))

def log(x, y):
    return math.log(x, y)


print("Select an operation:\n")
print("   addition\n   subtraction\n   multiplication\n   division\n   exponents\n   square root\n   nth root\n   logarithm\n")


while True:
    # User input
    choice = input("Enter operation's name: ")

    # Check if choice is one of the options
    if choice in ("addition", "subtraction", "multiplication", "division", "exponents", "nth root", "logarithm"):
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))

        if choice == "addition":
            print(x, "+", y, "=", add(x, y))

        elif choice == "subtraction":
            print(x, "-", y, "=", subtract(x, y))

        elif choice == "multiplication":
            print(x, "*", y, "=", multiply(x, y))

        elif choice == "division":
            print(x, "/", y, "=", divide(x, y))

        elif choice == "exponents":
            print(x, "^", y, "=", exponent(x, y))

        elif choice == "nth root":
            print(x, "^√", y, "=", nthroot(x, y))

        elif choice == "logarithm":
            print(f'log({x} [, {y}]) = ', log(x, y)) #el fixed.

        else:
            print("Invalid Input")


    if choice in ("square root"):
        x = float(input("Enter first number: "))

        if choice == "square root":
            print("√", x, "=", sqrt(x))


        else:
            print("Invalid Input")
