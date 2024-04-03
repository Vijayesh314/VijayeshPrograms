
import math

def pizza_party():
    try:
        wholeCost = float(input("What is the cost of the whole pizza? "))
    except ValueError:
        print("I'm afraid you have entered an invalid input. Please enter a valid decimal.")
        return

    try:
        wholeSize = int(input("What is the size of the pizza (diameter)? "))
    except ValueError:
        print("I'm afraid you have entered an invalid input. Please enter a valid integer.")
        return

    wholeArea = math.pi * wholeSize
    costperinch = round(wholeCost / wholeArea, 2)

    print(f"The cost of the pizza per square inch is ${costperinch}.")

    try:
        sliceperperson = int(input("How many slices does each person want? "))
    except ValueError:
        print("I'm afraid you have entered an invalid input. Please enter a valid integer.")
        return

    try:
        numberofpeople = int(input("How many people are coming? "))
    except ValueError:
        print("I'm afraid you have entered an invalid input. Please enter a valid integer.")
        return

    try:
        slicesperpizza = int(input("How many slices are in a pizza? "))
    except ValueError:
        print("I'm afraid you have entered an invalid input. Please enter a valid integer.")
        return

    numberofpizzas = math.ceil(sliceperperson * numberofpeople / slicesperpizza)
    print(f"If we assume that each pizza has {slicesperpizza} slices, you need to buy {numberofpizzas} pizzas.")

    costperperson = round(numberofpizzas * costperinch, 2)
    print(f"Each person needs to pay ${costperperson} for {sliceperperson} slices.")

def pizza_comparison():
    try:
        pizza1size = int(input("What is the size of the first pizza (diameter)? "))
    except ValueError:
        print("I'm afraid you have entered an invalid input. Please enter a valid integer.")
        return

    try:
        pizza1cost = float(input("What is the cost of the first pizza? "))
    except ValueError:
        print("I'm afraid you have entered an invalid input. Please enter a valid decimal.")
        return

    try:
        pizza2size = int(input("What is the size of the second pizza (diameter)? "))
    except ValueError:
        print("I'm afraid you have entered an invalid input. Please enter a valid integer.")
        return

    try:
        pizza2cost = float(input("What is the cost of the second pizza? "))
    except ValueError:
        print("I'm afraid you have entered an invalid input. Please enter a valid decimal.")
        return

    costperinch1 = pizza1cost / pizza1size
    costperinch2 = pizza2cost / pizza2size

    if costperinch1 < costperinch2:
        print("Pizza 1 is the better deal because it costs less than Pizza 2 per square inch.")
    elif costperinch2 < costperinch1:
        print("Pizza 2 is the better deal because it costs less than Pizza 1 per square inch.")

print("Welcome to the pizza application.")
userChoice = input("Do you want to use this application to help you plan a pizza party (type 'a') or to see which pizza has a better deal (type 'b')? ")
while userChoice != 'a' and userChoice != 'b':
    print(f"Invalid choice: {userChoice}. Please enter 'a' or 'b'.")
    userChoice = input("Do you want to use this application to help you plan a pizza party (type 'a') or to see which pizza has a better deal (type 'b')? ")

if userChoice == 'a':
    pizza_party()
elif userChoice == 'b':
    pizza_comparison()
