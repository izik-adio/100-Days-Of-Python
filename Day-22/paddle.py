"""The part of the program that controls the paddle"""
from turtle import Turtle


class Paddle(Turtle):
    """The paddle class"""
    def __init__(self, position: tuple = (0, 0)):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.speed(0)
        self.goto(position)

    def move_up(self):
        """The part of the program that makes the paddle move up"""
        pos = self.ycor() + 20
        self.setpos(self.xcor(), pos)

    def move_down(self):
        """The part of the program that makes the paddle move down"""
        pos = self.ycor() - 20
        self.setpos(self.xcor(), pos)
