"""The Ball module"""
from turtle import Turtle


class Ball(Turtle):
    """The Ball Class"""
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed_time = 0.1
        self.x_move = 10
        self.y_move = 10

    def move(self):
        """The ball move function"""
        x_co = self.xcor() + self.x_move
        y_co = self.ycor() + self.y_move
        self.goto(x_co, y_co)

    def bounce_y(self):
        """The ball bounce function"""
        self.y_move *= -1

    def bounce_x(self):
        """The ball bounce function"""
        self.x_move *= -1
        self.speed_time *= 0.9

    def init_pos(self):
        """Returns the ball to the initial position"""
        self.hideturtle()
        self.home()
        self.showturtle()
        self.speed_time = 0.1
        self.bounce_x()
