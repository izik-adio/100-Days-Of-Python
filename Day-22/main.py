from turtle import Screen
from paddle import Paddle
from ball import Ball
from time import sleep

main_screen = Screen()
main_screen.setup(width=800, height=600)
main_screen.title("Pong")
main_screen.bgcolor("black")
main_screen.tracer(1)

r_paddle = Paddle((375, 0))
l_paddle = Paddle((-380, 0))

ball = Ball()

main_screen.listen()
main_screen.onkey(key="Up", fun=l_paddle.move_up)
main_screen.onkey(key="Down", fun=l_paddle.move_down)
main_screen.onkey(key="w", fun=r_paddle.move_up)
main_screen.onkey(key="s", fun=r_paddle.move_down)

game_is_on = True
pos = (10, 10)
while game_is_on:
    sleep(0.1)
    main_screen.update()
    ball.move()
    if ball.ycor() > 275 or ball.ycor() < -275:
        ball.bounce()