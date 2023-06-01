# TODO 1. Create a dictionary in this format:
# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dict = {y.letter : y.code for (x, y) in data.iterrows()}

word = input("Input a word: ").strip().upper()
nato = [data_dict[x] for x in word]
print(nato)
