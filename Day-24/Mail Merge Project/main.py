with open("./Input/Names/invited_names.txt", "rt") as names:
    names = names.readlines()

for name in names:
    with open("./Input/Letters/starting_letter.txt", "rt") as letter:
        d_letter = letter.read()
        d_letter = d_letter.replace("[name]", name.strip())

    with open(f"./Output/ReadyToSend/letter_for_{name.strip()}.txt", "x") as mail:
        mail.write(d_letter)