""" The turtle racing game """
from turtle import Turtle, Screen, done
from random import randint

screen = Screen()
screen.setup(width=600, height=350)
colors = ["red", "orange", "green", "purple", "yellow", "blue"]
GAME_ON = False


def instance(my_turtle: str, color: str, width: int, height: int):
    """Create an instance of a turtle, gives it a color and a position"""
    my_turtle.penup()
    my_turtle.color(color)
    my_turtle.setposition(width, height)


turtle_list = (
    Turtle(shape="turtle"),
    Turtle(shape="turtle"),
    Turtle(shape="turtle"),
    Turtle(shape="turtle"),
    Turtle(shape="turtle"),
    Turtle(shape="turtle"),
)


def play_game(play):
    """This is the main game function"""
    user_bet = ""
    while user_bet not in colors:
        user_bet = screen.textinput(
        title="Place Your Bet",
        prompt=f"Which turtle would win?{colors}\nInput the color: ",
        )
    pos = 0
    x_cor = -280
    y_cor = -120

    for turtles in turtle_list:
        instance(turtles, color=colors[pos], width=x_cor, height=y_cor)
        pos += 1
        y_cor += 50

    if user_bet:
        play = True

    while play:
        for i in range(6):
            move = randint(1, 10)
            turtle_list[i].forward(move)
            if turtle_list[i].xcor() > 270:
                if i == colors.index(user_bet):
                    user_choice = screen.textinput(
                        title="RESULT",
                        prompt="You won.\nyour guess is the winner"
                        "\nWould you like to play again ('y' or 'n')",
                    )
                    if user_choice == "y" or user_choice == "yes":
                        play = True
                        play_game(play)
                    else:
                        play = False

                else:
                    user_choice = screen.textinput(
                        title="RESULT",
                        prompt="You lose.\nwould you like to play again ('y' or 'n')",
                    ).lower()
                    if user_choice == "y" or user_choice == "yes":
                        play = True
                        play_game(play)
                    else:
                        play = False
    done()

play_game(GAME_ON)
