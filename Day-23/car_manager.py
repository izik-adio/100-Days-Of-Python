"""It controls all of the randomly generated cars of the game"""
from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "white", "purple"]


class CarManager:
    """It controls all of the randomly generated cars of the game"""

    def __init__(self):
        self.allcars = []
        self.car_speed = 5

    def create_car(self):
        """Creates a car instance"""
        num = randint(1, 5)
        if num == 2:
            car = Turtle("square")
            car.shapesize(stretch_len=1, stretch_wid=0.5)
            car.color(choice(COLORS))
            car.setheading(180)
            y_pos = randint(-260, 260)
            car.penup()
            car.setpos(300, y_pos)
            self.allcars.append(car)

    def move(self):
        """The object that keeps the cars moving"""
        for cars in self.allcars:
            cars.forward(self.car_speed)
