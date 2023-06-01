from tkinter import *

window = Tk()
window.title("Miles to Kilometers Converter")
window.minsize(width=350, height=300)
window.configure(padx=20, pady=30)

text = Label(text="Convert Miles to Kilometers")
text.grid(row=0, column=2)
text.configure(pady=10, font=("Arial", 10, "bold"))

label = Label(text="Miles")
label.grid(row=1, column=1)
label.configure(font=("Arial", 10, "bold"))

input = Entry()
input.focus()
input.grid(column=2, row=1)

Kilometer = Label(text="0 Kilometers", font=("Arial", 15, "bold"))
Kilometer.grid(row=3, column=2)


def convert():
    km = float(input.get()) * 1.609
    Kilometer.configure(text=f"{km} Kilometers")


button = Button(text="Convert", command=convert)
button.grid(row=2, column=2, padx=10, pady=10)

window.mainloop()
