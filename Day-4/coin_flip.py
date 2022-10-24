"""
This program is a cool game built out of random module in python
"""
import random

print(
    "Hello user you are welcome to the coin flip game\n"
    "you are to guess the side of the coin flip output\n"
    "N.B:You are competing with the computer!!!"
)

PLAY = True
while PLAY:
    coin = random.choice(["head", "tail"])
    user_guess = input("What side are you chooseing{Head or Tail}: ").lower()
    if coin == user_guess:
        print("Huray!!!.\nYou guessed right.")
    else:
        print("Sorry that was wrong!")
    opt = input("\nWould you like to PLAY again{yes/no}: ").lower()
    if opt == "yes":
        PLAY = True
    else:
        PLAY = False
