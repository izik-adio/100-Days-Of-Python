"""The player or moving turtle module"""
from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10


class Player(Turtle):
    """The player or moving turtle module"""

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("blue")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)

    def move_up(self):
        """the method that would allow the movement of the turtle"""
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        """the method that would allow the movement of the turtle"""
        self.backward(MOVE_DISTANCE)
