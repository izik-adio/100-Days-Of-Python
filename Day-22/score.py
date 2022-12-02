"""The part of the program that handles the score"""
from turtle import Turtle

class Score(Turtle):
    """The module for keeping the score"""
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.setpos(0, 235)
        self.score_update()

    def score_update(self):
        """Update the current score"""
        self.clear()
        self.write(arg=f"{self.l_score}     \
            {self.r_score}", align="center", font=("Arial", 45))

    # def score(self, side):
    #     """Increment score whem called"""
    #     if side == "l":
    #         self.l_score += 1
    #     elif side == "r":
    #         self.r_score += 1
