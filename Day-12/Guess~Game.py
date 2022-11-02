from random import randint
from art import logo

def hint(guess, user_guess):
    if user_guess > guess:
        return "Too High\nGuess Again"
    elif user_guess < guess:
        return "Too low\nGuess Again"
    
def play(possible_attempts):
    while possible_attempts >= 0:
        user_guess = int(input(f"Remaing guess chance = {possible_attempts}.\nGuess a number between 1-100: "))
        if user_guess != guess:
            if possible_attempts == 0:
                print(f"Youve run out of guesses. You lose.The number is {guess}")
                break
            print(hint(guess,user_guess))
        else:
            print("You win")
            break
        possible_attempts -= 1

while input("Would you like to play a number guess game? Reply with 'y' or 'n': ").lower() == 'y':
    print(logo)
    print("Welcome to This Guess Game")
    Interested = True
    while Interested:
        guess = randint(1,100)
        user_choice = input("Choose Difficulty level. Reply with 'Easy' or 'Hard' or 'No': ").lower()
        if user_choice == 'easy':
            possible_attempts = 10
            play(possible_attempts)
        elif user_choice == 'hard':
            possible_attempts = 5
            play(possible_attempts)
        elif user_choice == 'no':
            break
        else:
            pass
