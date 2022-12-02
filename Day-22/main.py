"""The main page of the game"""
from time import sleep
from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score

main_screen = Screen()
main_screen.setup(width=800, height=600)
main_screen.title("Pong")
main_screen.bgcolor("black")
main_screen.tracer(1)

r_paddle = Paddle((375, 0))
l_paddle = Paddle((-380, 0))

ball = Ball()
score = Score()

main_screen.listen()
main_screen.onkey(key="Up", fun=l_paddle.move_up)
main_screen.onkey(key="Down", fun=l_paddle.move_down)
main_screen.onkey(key="w", fun=r_paddle.move_up)
main_screen.onkey(key="s", fun=r_paddle.move_down)

def goal():
    """To check if any paddle wins"""
    if ball.xcor() <= -385:
        score.r_score += 1
        ball.init_pos()
        return True
    if ball.xcor() >= 385:
        score.l_score += 1
        ball.init_pos()
        return True

GAME_IS_ON = True
while GAME_IS_ON:
    sleep(ball.speed_time)
    main_screen.update()
    ball.move()
    if ball.ycor() > 278 or ball.ycor() < -278:
        ball.bounce_y()
    if ball.distance(r_paddle) < 50 and ball.xcor() >= 360 or \
        ball.distance(l_paddle) < 50 and ball.xcor() <= -360:
        ball.bounce_x()
    if goal():
        score.score_update()
