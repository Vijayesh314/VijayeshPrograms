global user_burger
user_burger=None
global beverage_option
beverage_option=None
global beverage_size
beverage_size=None
global actual_beverage
actual_beverage=None
global subtotal
subtotal=None
global frenchfries_option
frenchfries_option=None
global frenchfries_size
frenchfries_size=None
global megasizefries
megasizefries=None 
global count
count=None

def error_check(variable, dict, inputqs):
    count = 1
    while variable not in dict:
        count += 1
        if count==11:
            print("You have entered the input wrong ten times. KYS.")
            exit()
        print(variable)
        print("I'm afraid this is an invalid input.")
        variable = input(inputqs).lower()
    return variable

options = {"yes", "no"}
order_list = []

print("Welcome to The Habit Burger Grill, the best burger place in the country. We have burgers, beverages, and sides.")

burger_list = {"chicken":5.25, "beef":6.25, "tofu":5.75}
input1=input("Do you want Chicken for $5.25, Beef for $6.25, or Tofu for $5.75? Please type in the name given: ")
user_burger = error_check(input1.lower(), burger_list, "Do you want Chicken for $5.25, Beef for $6.25, or Tofu for $5.75? Please type in the name given: ")
order_list.append(f"{user_burger}")

print(f"Thanks for ordering {user_burger}. Thats a great choice")

beverage_option = input("Do you want a beverage with your burger? yes or no: ")
beverage_option = error_check(beverage_option.lower(), options, "Do you want a beverage with your burger? yes or no: ")

if beverage_option == "yes":
    beverage_list = {"small":1.00, "medium":1.75, "large":2.25}
    beverage_size = input("What size drink do you want: Small for $1.00, Medium for $1.75, or Large for $2.25? ")
    beverage_size = error_check(beverage_size.lower(), beverage_list, "What size drink do you want: Small for $1.00, Medium for $1.75, or Large for $2.25? ")
    
    actual_beverage = input("What beverage do you want: sprite, coke, or fanta? ")
    actual_beverage = error_check(actual_beverage.lower(), {"sprite", "coke", "fanta"}, "What beverage do you want: sprite, coke, or fanta? ")
    print(f"So you want a {beverage_size} {actual_beverage}.")
    order_list.append(f"{beverage_size} {actual_beverage}")
    subtotal = burger_list[user_burger] + beverage_list[beverage_size]
elif beverage_option == "no":
    print("Okay. Totally alright.")
    subtotal = burger_list[user_burger]
else:
    print("You have entered an invalid input")

frenchfries_option = input("Do you want french fries with your meal? Yes or No: ")
frenchfries_option = error_check(frenchfries_option.lower(), options, "Do you want french fries with your meal? Yes or No: ")

if frenchfries_option == "yes":
    frenchfries_list = {"small":1.00, "medium":1.50, "large":2.00}
    frenchfries_size = input("What size french fries do you want: small for $1.00, medium for $1.50, or large $2.00? ")
    frenchfries_size = error_check(frenchfries_size.lower(), frenchfries_list, "What size french fries do you want: small for $1.00, medium for $1.50, or large $2.00? ")
    if frenchfries_size == "small":
        megasizefries = input("Do you want to mega size your fries? yes or no: ")
        megasizefries = error_check(megasizefries.lower(), options, "Do you want to mega size your fries? Yes or No: ")
        if megasizefries == "yes":
            print("The cost of the fries is $2")
            subtotal += 2
            order_list.append("Large fries")
        else:
            print("That's alright.")
            print("The cost of the fries is $1")
            order_list.append(f"Small fries")
            subtotal += 1
    else:
        print("The cost of the fries is",frenchfries_list[frenchfries_size])
        order_list.append(f"{frenchfries_size} fries")
        subtotal += frenchfries_list[frenchfries_size]
else:
    print("Okay. Totally alright.")

number_of_ketchup = input("How many ketchup packets do you want? ")
while number_of_ketchup.isnumeric() is False:
    count = 1
    count += 1
    if count == 11:
        print("You have entered the input wrong ten times.")
        exit()
    print("I'm afraid you have entered an invalid input. Please try again.")
    number_of_ketchup = input("How many ketchup packets do you want? ")
order_list.append(f"{number_of_ketchup} ketchup packets")
ketchup_price = int(number_of_ketchup)/4
subtotal += ketchup_price

if beverage_option == "yes" and frenchfries_option == "yes":
    subtotal -=1
    print(order_list)
    print(f"Your total is ${subtotal} because you get a $1 discount for ordering a burger, beverage, and fries.")
else:
    print(order_list)
    print(f"Your total is ${subtotal}")
print("Thanks for odering at The Habit Burger Grill. I hope you enjoy your food and have a wonderful day.")
