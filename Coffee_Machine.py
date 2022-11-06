from data import MENU
from art import logo
from os import name, system

resorce = {"water":300, "milk":200, "coffee":100, "money":0}

# create report function that retrun what is at hand
def report():
    """It shows the current resource values"""
    print(f'Water: {resorce["water"]}ml\nMilk: {resorce["milk"]}ml\nCoffe: {resorce["coffee"]}g\nMoney: ${resorce["money"]}')

# create function that process coin
def process_coin():
    """Get the user coin and return the total"""
    total = 0
    print("Insert your coins.")
    try:
        total += float(input("How many quaters?: ")) * 0.25
        total += float(input("How many dimes?: ")) * 0.10
        total += float(input("How many nickles?: ")) * 0.05
        total += float(input("How many pennies?: ")) * 0.01
    except (ValueError, TypeError):
        print("Invalid input")
    return total

# check that the transaction is successful
def transaction_check(coffee_choice):
    """Check that the user has inserted enough money to purchase the drink they selected."""
    # define each of the coffe type price
    coffee_choice_price = {
        "espresso": MENU["espresso"]["cost"],
        "latte": MENU["latte"]["cost"],
        "cappuccino": MENU["cappuccino"]["cost"],     
        }
    pay = process_coin()
    def check(price):
        """It checks if the price is less, equal or over"""
        if pay < price:
            print("Sorry that's not enough money. Money refunded.")
        elif pay == price:
            resorce["money"] += pay
            return True
        else:
            change = pay - price
            resorce["money"] += price
            print(f"Here is ${change:.2f} in change")
            return True

    price = coffee_choice_price[coffee_choice]
    return check(price)

# create function that checks if resorce is enough for the order
def confirm_resource(coffee_choice):
    if (resorce["milk"] >= MENU[coffee_choice]["ingredients"]["milk"]) and (resorce["water"] >= MENU[coffee_choice]["ingredients"]["water"]) and (resorce["coffee"] >= MENU[coffee_choice]["ingredients"]["coffee"]):
        return True
    else:
        for value in MENU["espresso"]["ingredients"]:
            if resorce[value] < MENU[coffee_choice]["ingredients"][value]:
                print(f"Sorry there is not enough {value}")

# make the coffee by deducting what is needed from the store
def make_coffe(coffee_choice):
    resorce["milk"] -= MENU[coffee_choice]["ingredients"]["milk"]
    resorce["water"] -= MENU[coffee_choice]["ingredients"]["water"]
    resorce["coffee"] -= MENU[coffee_choice]["ingredients"]["coffee"]
    print(f"Here is your {coffee_choice}☕. Enjoy!")

# A function to clear the screen
def clear():
    if name == "nt":
        system("cls")
    else:
        system("clear")

on = True
off = False
print(logo)
while on:
    coffee_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if coffee_choice not in ("espresso", "latte", "cappuccino", "report", "off"):
        continue
    else:
        if coffee_choice == "report":
            report()
        elif coffee_choice == "off":
            clear()
            on = off
        else:
            clear()
            print(logo)
            if confirm_resource(coffee_choice):
                if transaction_check(coffee_choice):
                    make_coffe(coffee_choice)
