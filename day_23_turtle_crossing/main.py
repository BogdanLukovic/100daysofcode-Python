import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


def collision():
    for car in cars.cars:
        if player_turtle.distance(car) < 25:
            global game_is_on
            game_is_on = False
            game_over()


def game_over():
    score.write_game_over()


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle crossing")


player_turtle = Player()
cars = CarManager()
score = Scoreboard()

screen.listen()

i = 0
new_car_spawn_increment = 5
level = 0

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    score.write_score(level=level)

    screen.onkeypress(player_turtle.move, "Up")

    if i == new_car_spawn_increment:
        cars.make_new_car()
        i = 0
    i += 1
    cars.move_cars(level=level)

    if player_turtle.at_finish_line():
        level += 1
        player_turtle.hideturtle()
        player_turtle = Player()

    collision()
    screen.update()


screen.exitonclick()


