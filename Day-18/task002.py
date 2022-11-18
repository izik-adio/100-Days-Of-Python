"""drawing dashed lines"""
from turtle import Turtle, Screen, done

tim = Turtle()
tim.speed(3)
tim.pensize(3)

for i in range(1, 10):
    for _ in range(16):
        tim.forward(10)
        tim.pendown()
        tim.forward(10)
        tim.penup()
    if i == 3 or i == 5 or i == 7:
        continue
    tim.right(90)
done()
my_screen = Screen()
