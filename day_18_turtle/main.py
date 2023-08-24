import random
import turtle
from turtle import Turtle, Screen
# import colorgram
#
# colors = colorgram.extract("image.jpg", 30)
# rgb_tuples = []
#
# for i in range(len(colors)):
#     r = colors[i].rgb.r
#     g = colors[i].rgb.g
#     b = colors[i].rgb.b
#
#     new_color = (r, b, g)
#     rgb_tuples.append(new_color)
#
# print(rgb_tuples)

color_list = [(198, 32, 12), (250, 17, 237), (39, 189, 76), (38, 68, 217), (238, 5, 227), (229, 46, 159), (27, 157, 40), (215, 12, 74), (15, 16, 154), (199, 10, 14), (242, 252, 246), (243, 165, 33), (229, 121, 17), (73, 31, 9), (60, 8, 14), (224, 211, 141), (10, 61, 97), (221, 9, 160), (17, 43, 18), (46, 232, 214), (11, 239, 227), (81, 214, 73), (238, 220, 156), (74, 167, 213), (77, 202, 234), (52, 243, 234), (3, 40, 67)]

timmy = Turtle()
my_screen = Screen()
my_screen.colormode(255)
timmy.penup()

timmy.speed(100)
timmy.width(20)
space_between_dots = 50
num_of_dots = 10
timmy.setposition(- 200, -200)


timmy.hideturtle()

for y in range(10):
    for x in range(10):
        timmy.color(random.choice(color_list))
        timmy.circle(1)
        timmy.dot(20)
        timmy.setposition(timmy.position() + (space_between_dots, 0))
    timmy.setposition(-200, timmy.ycor() + space_between_dots)


my_screen.exitonclick()
