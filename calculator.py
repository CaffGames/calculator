import math 

#A
def add(x, y):
    return x + y
#B
def subtract(x, y):
    return x - y
#C
def multiply(x, y):
    return x * y
#D
def divide(x, y):
    return x / y
#E
def exponent(x, y):
    return (x ** y)
#F
def sqrt(x):
    return(x)**(1/2)

pi = math.pi


print("Select an operation:\n")
print("   A: addition\n   B: subtraction\n   C: multiplication\n   D: division\n   E: exponents\n   F: square root\n")


while True:
    # User imput
    choice = input("Enter operation's code letter: ")

    # Check if choice is one of the options
    if choice in ("A", "B", "C", "D", "E"):
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))

        if choice == "A":
            print(x, "+", y, "=", add(x, y))

        elif choice == "B":
            print(x, "-", y, "=", subtract(x, y))

        elif choice == "C":
            print(x, "*", y, "=", multiply(x, y))

        elif choice == "D":
            print(x, "/", y, "=", divide(x, y))

        elif choice == "E":
            print(x, "^", y, "=", exponent(x, y))

            break
        else:
            print("Invalid Input")


    if choice in ("F"):
        x = float(input("Enter first number: "))

        if choice == "F":
            print("√", x, "=", sqrt(x))

            break
        else:
            print("Invalid Input")
