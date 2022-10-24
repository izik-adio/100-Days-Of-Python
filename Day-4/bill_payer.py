"""
The bill payer
"""
from random import randint

# recieve the names of all participant
names = input("names: ")

# filter through the name and pick a random name
names = names.split(" ")
index = randint(0, len(names) - 1)

# retrn the choosen name
print(f"Hey {names[index]} you have been choosen to pay the bill")
