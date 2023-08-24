from turtle import Turtle

COORDINATE1 = -380
COORDINATE2 = 380
PADDLE_SIZE = 4


class Paddle:
    def __init__(self):
        self.segments = []
        self.make_paddle()

    def make_paddle(self):
        for _ in range(PADDLE_SIZE):
            self.segments.append(Turtle())
        for segment in self.segments:
            segment.width(20)
            segment.shape("square")
            segment.color("white")
            segment.penup()
            segment.speed("fastest")

        for i in range(PADDLE_SIZE):
            self.segments[i].goto(COORDINATE1, i * 20)

    def move_paddle_up(self):
        if not self.segments[0].ycor() > 300:
            for segment in self.segments:
                segment.goto(segment.xcor(), segment.ycor() + 20)

    def move_paddle_down(self):
        if not self.segments[3].ycor() < -300:
            for segment in self.segments:
                segment.goto(segment.xcor(), segment.ycor() - 20)
