from turtle import Turtle, Screen
import time


class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    snake = []
    DIRECTION = 0

    def add_segment(self):

        self.snake.append(Turtle())
        tip = - 1
        self.snake[tip].penup()
        self.snake[tip].speed("fastest")
        self.snake[tip].width(10)
        self.snake[tip].shape("square")
        self.snake[tip].color("white")

        # Adds the first 3 segments to starting position and then adds one at a time to the end
        if len(self.snake) > 2:
            self.add_segment_to_end()
        else:
            self.snake[tip].setposition(-20 * tip, 0)

    def add_segment_to_end(self):
        tip = len(self.snake) - 1
        last_segment = self.snake[len(self.snake) - 2]
        second_to_last = self.snake[len(self.snake) - 3]

        # Adds tip of snakes' tail to end of snake
        x = last_segment.xcor() - (second_to_last.xcor() - last_segment.xcor())
        y = last_segment.ycor() - (second_to_last.ycor() - last_segment.ycor())
        self.snake[tip].setposition(x, y)

    def move(self):
        for i in range(len(self.snake) - 1, 0, -1):
            self.snake[i].setposition(self.snake[i - 1].pos())
        self.snake[0].forward(20)

    def look_up(self):
        if not self.DIRECTION == 270:
            self.DIRECTION = 90
        self.snake[0].setheading(self.DIRECTION)

        time.sleep(0.2)

    def look_left(self):

        if not self.DIRECTION == 0:
            self.DIRECTION = 180
        self.snake[0].setheading(self.DIRECTION)
        time.sleep(0.2)

    def look_right(self):
        if not self.DIRECTION == 180:
            self.DIRECTION = 0
        self.snake[0].setheading(self.DIRECTION)
        time.sleep(0.2)

    def look_down(self):
        if not self.DIRECTION == 90:
            self.DIRECTION = 270
        self.snake[0].setheading(self.DIRECTION)
        time.sleep(0.2)

    def create_snake(self):
        self.add_segment()
        self.add_segment()
        self.add_segment()

    def reset(self):
        for segment in self.snake:
            segment.goto(1000, 1000)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]