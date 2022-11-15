from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from time import sleep
from os import system, name


money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()


class main:

    def clear(self):
        if name == "nt":
            system("cls")
        else:
            system("clear")

    def report(self):
        """ Return Resource Balance """
        money_machine.report()
        coffee_maker.report()

    def checker(self, user_drink):
        """ Check Resources Sufficient"""
        check = Menu().find_drink(user_drink)
        return coffee_maker.is_resource_sufficient(check)

    def coin(self, user_drink):
        """ Process coins and Check transaction successful """
        cost = Menu().find_drink(user_drink).cost
        check_pay = money_machine.make_payment(cost)
        return check_pay

    def make_coffee(self, user_drink):
        """ Make Coffee """
        drink_request = Menu().find_drink(user_drink)
        coffee_maker.make_coffee(drink_request)

    def admin(self):
        admin_name = input("Whats your name: ").lower()
        password = input("Input admin password: ").lower()
        if admin_name == "owner" and password == "owner-password":
            while True:
                admin_choice = input("What would you like to do (Off/Refill/Report/Quit): ").lower()
                if admin_choice == "off":
                    print("Would switch off in 2 seconds")
                    return False
                elif admin_choice == "refill":
                    coffee_maker.resources = {
                        "water": 300,
                        "milk": 200,
                        "coffee": 100,
                    }
                    print("Refilled")
                    continue
                elif admin_choice == "report":
                    self.report()
                    sleep(5)
                    self.clear()
                    continue
                elif admin_choice == "quit":
                    self.clear()
                    break
                else:
                    print("Invalid Input")
                    continue
        else:
            print("Invalid Credentials")
            return True
