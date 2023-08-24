from turtle import Turtle, Screen
import random

my_screen = Screen()
turtles = []


my_screen.setup(width = 500, height= 400)
bet = my_screen.textinput(title = "Make your bet", prompt= "Which tutle will win the race? Pick a color: ")


def move_completely_left(turtle):
    turtle.setposition(-230, 0)


def make_into_turtle(turtle):
    turtle.shape("turtle")


def move_turtles():
    will_move = (0, 4)
    for turtle in turtles:
        step = will_move[random.randint(0, 1)]
        new_pos = turtle.xcor() + step
        turtle.setposition(new_pos, turtle.ycor())


def draw_track():
    timmy = Turtle()
    timmy.penup()
    track_line = 100
    timmy.speed(50)

    for _ in range(6):
        timmy.setposition(-230, track_line)
        timmy.pendown()
        timmy.setposition(timmy.position() + (435, 0))
        timmy.penup()

        track_line -= 40

    start = -230
    stop = 200

    timmy.setposition(start, 100)
    timmy.pendown()
    timmy.setposition(start, -100)
    timmy.penup()

    timmy.setposition(stop, 100)
    timmy.pendown()
    timmy.setposition(stop, -100)
    timmy.penup()

    timmy.setposition(stop + 5, 100)
    timmy.pendown()
    timmy.setposition(stop + 5, -100)
    timmy.penup()

    timmy.hideturtle()

draw_track()


for _ in range(5):
    turtles.append(Turtle())


turtles[0].color("purple")
turtles[1].color("blue")
turtles[2].color("green")
turtles[3].color("yellow")
turtles[4].color("red")


for each in turtles:
    each.penup()
    make_into_turtle(each)
    each.speed(50)


track = 80
for each in turtles:
    move_completely_left(each)
    each.sety(track)
    track -= 40


won = False
while not won:
    move_turtles()
    for each in turtles:
        if each.xcor() >= 200:
            won = True
            winner = each

if bet == winner:
    print(f"You Win! You bet on the right turtle. Winning turtle: {winner.color()}")
else:
    print(f"You Lose. You didn't bet on the right turtle. Winning turtle: {winner.color()}")

my_screen.exitonclick()
