from data import MENU
from art import logo
from os import name, system

resorce = {"water":300, "milk":200, "coffee":100, "money":0}

# create report function that retrun what is at hand
def report():
    """It shows the current resource values"""
    water = resorce["water"]
    milk = resorce["milk"]
    coffee = resorce["coffee"]
    money = resorce["money"]
    print(f"Water: {water}ml\nMilk: {milk}ml\nCoffe: {coffee}g\nMoney: ${money}")

# create function that process coin
def process_coin():
    """Get the user coin and return the total"""
    quarters = 0.25
    dimes = 0.10
    nickles = 0.05
    pennies = 0.01

    quarters_pay = 0
    dimes_pay = 0
    nickles_pay = 0
    pennies_pay = 0

    print("Insert your coins.")
    try:
        quarters_pay = float(input("How many quaters?: "))
        dimes_pay = float(input("How many dimes?: "))
        nickles_pay = float(input("How many nickles?: "))
        pennies_pay = float(input("How many pennies?: "))

    except (ValueError, TypeError):
        print("Invalid input")
    pay = (quarters * quarters_pay) + (dimes * dimes_pay) + (nickles * nickles_pay) + (pennies * pennies_pay)
    return pay

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
            on = off
        else:
            clear()
            print(logo)
            if confirm_resource(coffee_choice):
                if transaction_check(coffee_choice):
                    make_coffe(coffee_choice)
