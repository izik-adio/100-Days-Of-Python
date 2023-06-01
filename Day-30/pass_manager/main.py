import json
from json import *
from random import choice, randint, shuffle
from tkinter import *
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        new_data = {website: {"Email:": email, "Password:": password}}
        try:
            with open(file="data.json", mode="r") as first_data:
                read_data = json.load(first_data)
        except FileNotFoundError:
            with open(file="data.json", mode="w") as first_data:
                dump(new_data, first_data, indent=4)
        else:
            read_data.update(new_data)
            with open("data.json", "w") as data_file:
                dump(read_data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


def find_password():
    if len(website_entry.get()) > 0:
        try:
            with open(file="data.json", mode="r") as database:
                data = load(database)
        except FileNotFoundError:
            messagebox.showwarning(title="Error", message="No data file found")
        else:
            search = website_entry.get()
            try:
                email = data[search]["Email:"]
                password = data[search]["Password:"]
            except KeyError:
                messagebox.showerror(title="Error", message=f"No details for {search} exists")
            else:
                messagebox.showinfo(title=search.capitalize(), message=f"Email: {email}\n\nPassword: {password}")
    else:
        messagebox.showwarning(title="Empty Search", message="Make Sure to input a website to search for.")


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

website_entry = Entry(width=32)
website_entry.grid(row=1, column=1, columnspan=1)
website_entry.focus()

email_entry = Entry(width=47)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "example@gmail.com")

password_entry = Entry(width=32)
password_entry.grid(row=3, column=1)

search_button = Button(text="Search", bg="white", borderwidth=1, command=find_password)
search_button.config(font=("", 7, ""), width=14)
search_button.grid(row=1, column=2)

password_button = Button(text="Generate Password", bg="white", borderwidth=1, command=generate_password)
password_button.config(font=("", 7, ""))
password_button.grid(row=3, column=2)

label_4 = Label(text="", pady=15, bg="white")
label_4.grid(row=4, column=0)
add_button = Button(text="Add", width=40, bg="white", borderwidth=1, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
