import random
from word_list import word_list

# choose a random word from the above list
chosen_word = random.choice(word_list)

# the user in-game lives
lives = ["❤", "❤", "❤", "❤", "❤", "❤"]

# what to show to the user
display = []
for _ in chosen_word:
    display.append("_")

# rule of the game
print("Hello user welcome to this game you are to guess the hidden word by "
      "guessing each of its characters\nNB:You have ❤❤❤❤❤❤ lives\n"
      "For each incorrect guess you make you lose a live\n")
left = len(lives)
print(chosen_word)
while "_" in display:
    # show the user the remaining live
    print(f"\nLives left is {lives[:left]}")

    # get the user guess
    guess = input("\nGuess a letter from the hidden word: ").lower()

    # check if the user already guessed the same letter before
    if guess in display:
        print("\nYou already guessed this before")

    for position in range(len(chosen_word)):
        if guess == chosen_word[position]:
            display[position] = guess

    if guess not in chosen_word:
        left -= 1
        if left == 0:
            print("\nYou lose.Try again later")
            print(display)
            break
    print(display)
    
if list(chosen_word) == display:
    print("\nYou win👏👏👏")
