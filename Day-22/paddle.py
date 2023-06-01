from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position: tuple = (0, 0)):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.speed(0)
        self.goto(position)

    def move_up(self):
        pos = self.ycor() + 20
        self.setpos(self.xcor(), pos)

    def move_down(self):
        pos = self.ycor() - 20
        self.setpos(self.xcor(), pos)
