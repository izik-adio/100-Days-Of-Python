"""Import of the turtle module so our new class can inherit from the Turtle class"""
from turtle import Turtle
from random import randint, random


class Food(Turtle):
    """Created the food class so as to get food for the snake"""

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.penup()
        self.speed(0)
        self.food_color()
        self.refresh()

    def food_color(self):
        """changes the food color"""
        self.color(random(), random(), random())

    def refresh(self):
        """Changes the food location"""
        random_x = randint(-280, 280)
        random_y = randint(-280, 280)
        self.goto(random_x, random_y)
