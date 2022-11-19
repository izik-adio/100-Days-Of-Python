"""A simple game where keywords are used to control a little turtle on the screen"""
import turtle

tim = turtle.Turtle()
tim.color("white")

# W = Forwards
# S = Backwards
# A = Counter-Clockwise
# D = Clockwise
# C = Clear drawing

def forwards():
    """Moves tim forwards when called"""
    tim.forward(10)

def backwards():
    """Moves tim backwards when called"""
    tim.backward(10)

def counter_clockwise():
    """Moves tim counter clockwise when caled"""
    tim.left(5)

def clockwise():
    """Moves tim clockwise when called"""
    tim.right(5)

def clear_screen():
    """clears the screen when calwled"""
    tim.clear()
    tim.home()

screen = turtle.Screen()
screen.bgcolor("black")

screen.listen()
screen.onkey(fun=forwards, key="w")
screen.onkey(fun=backwards, key="s")
screen.onkey(fun=counter_clockwise, key="a")
screen.onkey(fun=clockwise, key="d")
screen.onkey(fun=clear_screen, key="c")

screen.exitonclick()
