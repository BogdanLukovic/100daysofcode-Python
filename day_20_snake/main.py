from scoreboard import Scoreboard
from snake import Snake
from turtle import Turtle, Screen
from food import Food
import time

my_screen = Screen()
my_screen.setup(600, 600)
my_screen.bgcolor("black")
my_screen.tracer(0)


snake = Snake()

game_is_on = True

food = Food()

scoreboard = Scoreboard()

my_screen.onkeypress(snake.look_up, "w")
my_screen.onkeypress(snake.look_left, "a")
my_screen.onkeypress(snake.look_down, "s")
my_screen.onkeypress(snake.look_right, "d")
my_screen.listen()

while game_is_on:
    my_screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 17:
        food.refresh()
        scoreboard.increase_score()
        snake.add_segment()

    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()

    body = snake.snake[1:]
    for segment in body:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

my_screen.exitonclick()
