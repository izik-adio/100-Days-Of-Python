from turtle import Turtle


class ScoreBoard(Turtle):
    """To keep track of score"""

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.setposition(0, 270)
        self.hideturtle()

    def score_output(self, score_count):
        """to display the score"""
        self.clear()
        self.write(
            arg=f"Score: {score_count}", align="center", font=("Courier", 20, "normal")
        )

    def game_over(self):
        """Prompt the user that the game is over"""
        self.penup()
        self.setpos(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 30, "normal"))

        self.setpos(0, 0)
