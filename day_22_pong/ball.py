from turtle import Turtle

EDGE = 400


class Ball:

    def __init__(self):
        self.ball = Turtle()
        self.ball.penup()
        self.ball.shape("circle")
        self.ball.color("white")
        self.ball.setheading(110)

    def hit_opponent_paddle(self):
        current_heading = self.ball.heading()
        new_heading = 0

        if self.ball.heading() >= 0:
            new_heading = (90 + (90 - current_heading)) % 360
            self.ball.setheading(new_heading)
        else:
            new_heading = (270 - (current_heading - 270)) % 360
            self.ball.setheading(new_heading)

    def hit_player_paddle(self):
        current_heading = self.ball.heading()
        new_heading = 0

        if self.ball.heading() >= 180:
            new_heading = (270 + (270 - current_heading)) % 360
            self.ball.setheading(new_heading)
        else:
            new_heading = (90 - (current_heading + 90)) % 360
            self.ball.setheading(new_heading)

    def hit_wall(self):
        current_heading = self.ball.heading()
        new_heading = 0

        # TOP EDGE
        if self.ball.ycor() > EDGE:
            if self.ball.heading() <= 90:
                new_heading = (270 + (90 - current_heading)) % 360
                self.ball.setheading(new_heading)
            else:
                new_heading = (270 - (current_heading - 90)) % 360
                self.ball.setheading(new_heading)
        # BOTTOM EDGE
        elif self.ball.ycor() < -1 * EDGE:
            if self.ball.heading() >= 270:
                new_heading = (90 - (current_heading - 270)) % 360
                self.ball.setheading(new_heading)
            else:
                new_heading = (90 + (270 - current_heading)) % 360
                self.ball.setheading(new_heading)

        current_heading = new_heading

    def goal(self):
        if self.ball.xcor() > EDGE:
            return "win"
        elif self.ball.xcor() < -1 * EDGE:
            return "lose"
