from screen import MyScreen
from turtle import Turtle, Screen
import time
from paddle import Paddle
from ball import Ball


def point_scored(player_outcome):
    global pong_ball

    if player_outcome == "win":
        print("WIN")
        pong_ball.ball.hideturtle()
        pong_ball = Ball()

        return "player"
    elif player_outcome == "lose":
        print("LOSE")
        pong_ball.ball.hideturtle()
        pong_ball = Ball()
        return "lose"


my_screen = Screen()
my_screen.title("Pong")
my_screen.tracer(False)
my_screen.screensize(800, 800)
my_screen.bgcolor("black")
board = MyScreen()

# Makes paddles
player_A = Paddle()
player_B = Paddle()
pong_ball = Ball()


# Moves computer paddle to the right side
for segment in player_B.segments:
    segment.goto(380, segment.ycor())

# Moves player paddle
direction = "up"
my_screen.listen()

# Sets scores to 0
score_player = 0
score_computer = 0

while True:

    time.sleep(0.002)

    should_score = point_scored(pong_ball.goal())

    # Checks if a goal has been made
    if should_score == "player":
        board.blackout_score(score_player, score_computer)
        score_player += 1
    if should_score == "lose":
        board.blackout_score(score_player, score_computer)
        score_computer += 1



    # Moves paddles
    my_screen.onkeypress(player_A.move_paddle_up, "w")
    my_screen.onkeypress(player_A.move_paddle_down, "s")

    # Checks if ball hit paddles
    for segment in player_A.segments:
        if pong_ball.ball.distance(segment) < 15:
            pong_ball.hit_player_paddle()
            pass
    for segment in player_B.segments:
        if pong_ball.ball.distance(segment) < 15:
            pong_ball.hit_opponent_paddle()
            pass

    # Moves ball
    pong_ball.hit_wall()
    pong_ball.ball.forward(6)

    # Moves computer paddle and reverses direction if it hits a wall
    if direction.lower() == "up":
        if player_B.segments[3].ycor() >= 350:
            direction = "down"
        player_B.move_paddle_up()
    elif direction.lower() == "down":
        if player_B.segments[0].ycor() <= -350:
            direction = "up"
        player_B.move_paddle_down()

    board.draw_score(score_player, score_computer)
    my_screen.update()


my_screen.exitonclick()


