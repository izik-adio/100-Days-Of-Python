from menu import Menu
from func import main
from time import sleep


is_on = True
while is_on:
    option = Menu().get_items()
    user_choice = input(f"What would you like? {option}: ").lower()
    option = option.split("/")
    option.pop(-1)
    if user_choice in option:
        if main().checker(user_choice):
            if main().coin(user_choice):
                main().make_coffee(user_choice)
                sleep(3)
                main().clear()
    elif user_choice == "admin":
        main().admin()
    else:
        print("Invalid Input")
        continue
