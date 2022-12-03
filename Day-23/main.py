"""The main game module"""
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
player = Player()
car_manager = CarManager()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()
screen.onkey(fun=player.move_up, key="Up")
screen.onkey(fun=player.move_down, key="Down")

scoreboard = Scoreboard()

GAME_IS_ON = True
while GAME_IS_ON:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move()
    for x_car in car_manager.allcars:
        if player.distance(x_car) < 15:
            scoreboard.game_over()
            GAME_IS_ON = False
    if player.ycor() < -280:
        player.goto(0, -280)
    if player.ycor() >= 280:
        player.goto(0, -280)
        car_manager.car_speed += 5
        scoreboard.update()

screen.exitonclick()
