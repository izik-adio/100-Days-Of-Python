"""
get the random modle for randomisation
"""
import random

rock_img = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper_img = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors_img = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

interested = True
while interested:
    # set the choices from which the computer is to choose
    options = ["rock", "paper", "scissors"]
    # help the compter choose randomly with th help of random.choice
    computer_choice = random.choice(options)
    # get the user choice
    user_choice = input(
        "Hey user what is your choice [rock, paper or scissors]? ").lower()
    if computer_choice == user_choice:
        print("That was a draw")
    else:
        if computer_choice == "rock":
            if user_choice == "scissors":
                print(
                    f"computer choose: {rock_img} \nyou choose: "
                    f"{scissors_img}!\nYou lose")
            elif user_choice == "paper":
                print(
                    f"computer choose: {rock_img} \nyou choose: "
                    f"{paper_img}!\nYou win")
        elif computer_choice == "paper":
            if user_choice == "rock":
                print(
                    f"computer choose: {paper_img} \nyou choose: "
                    f"{rock_img}!\nYou lose")
            elif user_choice == "scissors":
                print(
                    f"Computer choose: {paper_img} \nyou choose: "
                    f"{scissors_img}!\nYou win")
        else:
            if user_choice == "paper":
                print(
                    f"computer choose: {scissors_img} \nyou choose: "
                    f"{paper_img}!\nYou lose")
            elif user_choice == "rock":
                print(
                    f"computer choose: {scissors_img} \nyou choose: "
                    f"{rock_img}!\nYou win")

    option = input("Would you like to play again{yes/no}: ").lower()
    if option == "yes":
        interested = True
    else:
        interested = False

