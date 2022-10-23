name = input("input the first name: ")
name_2 = input("input the second name: ")
name = name.lower()
name_2 = name_2.lower()
added = name + name_2

true = 0
love = 0

for letter in "true":
    true += added.count(letter)
for letter in "love":
    love += added.count(letter)

lovescore = int(str(true) + str(love))
if lovescore < 10 or lovescore > 90:
    print(f"Your score is {lovescore}, you match like coke and fanta")
elif lovescore >= 40 and lovescore <= 50:
    print(f"Your score is {lovescore}, you are alright together.")
else:
    print(f"Your score is {lovescore}")
