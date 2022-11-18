""" This code create an Hirst painting project clone """

import turtle
from random import choice

# import colorgram
# rgb_colors = []
# colors = colorgram.extract('C:/Users/isaac/Desktop/zik-tech/programming project/
# python projects/100-Days-Of-Python/Day-18/Hirst-Painting-Project/image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))


colors = [
    (149, 75, 50), (222, 201, 136), (53, 93, 123),
    (170, 154, 41), (138, 31, 20), (134, 163, 184),
    (197, 92, 73), (47, 121, 86), (73, 43, 35),
    (145, 178, 149), (14, 98, 70), (232, 176, 165),
    (160, 142, 158), (54, 45, 50), (101, 75, 77),
    (183, 205, 171), (36, 60, 74), (19, 86, 89),
    (82, 148, 129), (147, 17, 19), (27, 68, 102),
    (12, 70, 64), (107, 127, 153), (176, 192, 208),
    (168, 99, 102)
]


turtle.Screen().colormode(255)
t = turtle.Turtle()
t.speed(10)
t.penup()

for j in range(16):
    t.setposition(-250.00, (-300 + (j * 40)))

    for i in range(10):
        color = choice(colors)
        t.dot(20, color)
        t.fd(50)
turtle.Turtle().hideturtle()
turtle.done()
