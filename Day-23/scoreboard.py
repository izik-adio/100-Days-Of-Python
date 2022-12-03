"""This module keeps track of the players level"""

from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    """This module keeps track of the players level"""

    def __init__(self):
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.speed(0)
        self.color("white")
        self.penup()
        self.goto(x=-295, y=265)
        self.update()

    def update(self):
        """Prints the players score"""
        self.clear()
        self.level += 1
        self.write(arg=f"Level: {self.level}", align="left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER 😢😢😢", align="center", font=FONT)
