import random

# get the list of all alphabet in both lower and upercase
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o",
           "p","q","r","s","t","u","v","w","x","y","z","A","B","C","D",
           "E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S",
           "T","U","V","W","X","Y","Z"]

# Get all supported symbols
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

# Get all number from 1-9
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

# welcome the user
print("Welcome to the PyPassword Generator!")
use = input("What program(website, app, etc) are you generating a password for: ")
# get how many alphabet the user would like
no_letters = int(input("How many letters would you like in your password: "))
# get how many numbers the user would like
no_numbers = int(input("How many numbers would you like in your password: "))
# get how many symbols the user wold like
no_symbols = int(input("How many symbols would you like in your password: "))

# generate the amount of alphabet, num and symbols from the letters, numbers and symbols list

pass_list = []
while len(pass_list) < no_letters:
    pass_list.append(random.choice(letters))

while (len(pass_list) - no_letters) < no_symbols:
    pass_list.append(random.choice(symbols))

while len(pass_list) - (no_letters + no_symbols) < no_numbers:
    pass_list.append(random.choice(numbers))

random.shuffle(pass_list)

# concatenate the string that has been generated and output the result
password = ""
for items in pass_list:
    password += password.join(items)
pass_dict = {use:password}
print(f"Your newly generated password is: {password}")

f = open("password.txt","a")
f.write(f"\n{str(pass_dict)}")
f.close()