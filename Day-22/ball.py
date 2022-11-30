from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        x_co = self.xcor() + self.x_move
        y_co = self.ycor() + self.y_move
        self.goto(x_co, y_co)

    def bounce(self):
        self.y_move *= -1
