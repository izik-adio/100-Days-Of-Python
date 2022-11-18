""" draw multicolor small square at rando direction """
from turtle import Turtle, Screen, done
from random import random, randint, choice

my_tim = Turtle()
my_tim.speed(1000000)
my_tim.pensize(6)

my_screen = Screen()
my_screen.bgcolor("black")

randint(50, 500)
for _ in range(1000000):
    my_tim.color(random(), random(), random())
    my_tim.fd(50)
    angle = choice([0, 90, 180, 270])
    my_tim.setheading(angle)
done()
