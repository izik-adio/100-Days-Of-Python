"""A python program for circular structure and benzen structre"""

import turtle
import colorsys

# for a benzen structre
colors = ["red", "purple", "blue", "green", "orange", "yellow"]
tim = turtle.Pen()
tim.speed(0)
turtle.Screen().bgcolor("black")
for x in range(200):
    tim.pencolor(colors[x % 6])
    tim.width(x / 100 + 1)
    tim.forward(x)
    tim.left(59)
turtle.Screen().clear()

# for the circular structure
turtle.Screen().bgcolor("black")
t = turtle.Turtle()
n = 36
h = 0
t.speed(0)
for i in range(460):
    c = colorsys.hsv_to_rgb(h, 1, 0.9)
    h += 1/n
    t.color(c)
    t.left(145)
    for i in range(5):
        t.fd(300)
        t.left(150)
t.clear()
turtle.done()
