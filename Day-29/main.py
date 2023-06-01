from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def pass_generator():
    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) > 0 and len(password) > 0:
        save_response = messagebox.askokcancel(title=website, message=f"These are the details entered: "
                                                                      f"\nEmail: {email}\nPassword: {password}\n"
                                                                      f"Is it okay to save?")
        if save_response:
            with open(file="data.txt", mode="a") as data:
                data.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)
    else:
        messagebox.showwarning(title="Oops", message="Please don't leave any field empty!")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(pady=40, padx=40, bg="white")

lock_pics = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
canvas.create_image(100, 100, image=lock_pics)
canvas.grid(row=0, column=1)

label_1 = Label(text="Website:", bg="white")
label_1.grid(row=1, column=0)

label_2 = Label(text="Email/Username:", bg="white")
label_2.grid(row=2, column=0)

label_3 = Label(text="Password:", bg="white")
label_3.grid(row=3, column=0)

website_entry = Entry(width=47)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=47)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "example@gmail.com")

password_entry = Entry(width=32)
password_entry.grid(row=3, column=1)

password_button = Button(text="Generate Password", bg="white", borderwidth=1, command=pass_generator)
password_button.config(font=("", 7, ""))
password_button.grid(row=3, column=2)

label_4 = Label(text="", pady=15, bg="white")
label_4.grid(row=4, column=0)
add_button = Button(text="Add", width=40, bg="white", borderwidth=1, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
