from turtle import Turtle, done
from random import random

t = Turtle()
t.speed(0)

for i in range(360 // 5):
    t.color(random(), random(), random())
    t.circle(100)
    t.setheading(t.heading() + 5)
done()
