"""Creating the snake body"""
from turtle import Turtle

MOVE_CONSTANT = 20


class Snake:
    """The snake class"""

    def __init__(self):
        self.segments = []
        self.x_position = 0
        self.y_position = 0
        self.body()

    def body(self):
        """The snake main body method"""
        for _ in range(3):
            self.add_new_segment()

    def add_new_segment(self):
        """To make the snake grow longer"""
        segment = Turtle("square")
        segment.penup()
        segment.color("white")
        segment.goto(self.x_position, self.y_position)
        self.segments.append(segment)
        self.x_position -= 20

    def move(self):
        """The method to make the snake segments move"""
        for i in range(len(self.segments) - 1, 0, -1):
            x_position = self.segments[i - 1].xcor()
            y_position = self.segments[i - 1].ycor()
            self.segments[i].goto(x_position, y_position)
        self.segments[0].forward(MOVE_CONSTANT)


class Control:
    """To control the movement of the snake"""

    def __init__(self, segment):
        self.segment = segment

    def move_up(self):
        """The method to make the snake move in the upward direction"""
        if self.segment.heading() != 270:
            self.segment.setheading(90)

    def move_down(self):
        """The method to make the snake move in the downward direction"""
        if self.segment.heading() != 90:
            self.segment.setheading(270)

    def move_left(self):
        """The method to make the snake move in the leftward direction"""
        if self.segment.heading() != 0:
            self.segment.setheading(180)

    def move_rigth(self):
        """The method to make the snake move in the leftward direction"""
        if self.segment.heading() != 180:
            self.segment.setheading(0)
