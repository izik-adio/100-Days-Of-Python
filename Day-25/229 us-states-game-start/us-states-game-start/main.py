import turtle
import pandas

screen = turtle.Screen()
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data_f = pandas.read_csv("./50_states.csv")
guess_list = list(data_f.state)
score = 0
while len(guess_list) != 0:
    answer = screen.textinput(title=f"{score}/50 States Correct", prompt="Whats another states name?").title()
    if answer == "Exit":
        break
    for data in guess_list:
        if answer == data:
            state_data = data_f[data_f.state == answer]
            state_turtle = turtle.Turtle()
            state_turtle.hideturtle()
            state_turtle.penup()
            state_turtle.goto(int(state_data.x), int(state_data.y))
            state_turtle.write(answer)
            guess_list.remove(answer)
            score += 1
missing_states = {
    "Missing states": guess_list
}
missing_states = pandas.DataFrame(missing_states)
missing_states.to_csv("Missing-states.csv")

