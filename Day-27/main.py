import tkinter

screen = tkinter.Tk()
screen.minsize(500,500)
screen.title("First GUI with tkinter in Python")

text = tkinter.Label(text="This is a test text", font=("Arial", 25, "bold"))
text.pack(expand=1)
#
# screen.mainloop()

def add(*args):
    return sum(args)

print(add(1,2,3,4,5,6,7,8,9,10))