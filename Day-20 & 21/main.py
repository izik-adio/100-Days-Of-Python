"""The Snake Game Program"""
from time import sleep
from turtle import Screen

from food import Food
from scoreboard import ScoreBoard
from snake import Control, Snake

screen = Screen()
screen.bgcolor("black")
screen.title("My Snake Game")
screen.setup(width=600, height=600)
screen.tracer(0)

food = Food()
snake = Snake()
snake_head = snake.segments[0]
control = Control(snake.segments[0])
score = ScoreBoard()

screen.listen()
screen.onkey(key="Up", fun=control.move_up)
screen.onkey(key="Down", fun=control.move_down)
screen.onkey(key="Left", fun=control.move_left)
screen.onkey(key="Right", fun=control.move_rigth)


def play_game():
    """The main function that controls the whole game"""
    score_count = 0
    game_is_on = True
    while game_is_on:
        food.food_color()
        screen.update()
        sleep(0.1)
        snake.move()
        score.score_output(score_count)

        if snake_head.distance(food) < 15:
            score_count += 1
            food.refresh()
            snake.add_new_segment()

        if (
            snake_head.xcor() > 285
            or snake_head.xcor() < -285
            or snake_head.ycor() > 285
            or snake_head.ycor() < -285
        ):
            game_is_on = False
            score.game_over()

        for seg in snake.segments[1:]:
            if snake_head.distance(seg) < 10:
                game_is_on = False
                score.game_over()


play_game()
play_again = screen.textinput(
    title="Play Again", prompt="Would you like to play again?\n['y' or 'n']: "
)
if (
    play_again == "y"
    or play_again == "yes"
    or play_again == "yeah"
    or play_again == "ye"
):
    play_game()

screen.exitonclick()
