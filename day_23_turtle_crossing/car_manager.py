from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CAR_WIDTH = 25


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.new_car = None
        self.cars = []
        self.hideturtle()

    def make_new_car(self):
        self.new_car = Turtle()
        random_color = random.choice(COLORS)
        x = 300
        y = random.randint(-270, 270)

        self.new_car.penup()
        self.new_car.setheading(90)
        self.new_car.goto(x, y)
        self.new_car.color(random_color)
        self.new_car.shape("square")
        self.new_car.width(CAR_WIDTH)
        self.new_car.shapesize(stretch_wid=2, stretch_len=1)
        self.cars.append(self.new_car)

    def move_cars(self, level):
        for car in self.cars:
            x = car.xcor() - (STARTING_MOVE_DISTANCE + level * MOVE_INCREMENT)
            y = car.ycor()
            car.goto(x, y)