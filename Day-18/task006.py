from turtle import Turtle, done

t = Turtle()
t.speed("fastest")

for i in range(360):
    t.color("red")
    for _ in range(4):
        t.forward(100)
        t.right(90)
    t.setheading(i)
    t.hideturtle()
done()