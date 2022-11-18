"""draw diffrent shapes from three sides to 10 sides with each shape having diffrent color"""
from random import random
from turtle import Turtle, Screen, done

tim = Turtle()
tim.pensize(2)
tim.speed(3)

my_screen = Screen()


for x in range(2):
    if x == 0:
        for i in range(3, 11):
            angle = int(360 / i)
            for _ in range(i):
                tim.forward(100)
                tim.left(angle)
            tim.color(random(), random(), random())
    elif x == 1:
        for i in range(3, 11):
            angle = int(360 / i)
            for _ in range(i):
                tim.forward(100)
                tim.right(angle)
            tim.color(random(), random(), random())

done()
