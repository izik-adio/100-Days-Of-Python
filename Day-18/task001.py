from turtle import Turtle, Screen, done

my_turtle = Turtle()
my_turtle.color("white")

my_screen = Screen()
my_screen.bgcolor("blue")
my_screen.exitonclick

# to make turtle draw a square
for _ in range(4):
    my_turtle.forward(100)
    my_turtle.right(90)
done()
