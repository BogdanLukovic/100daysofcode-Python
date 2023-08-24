from turtle import Screen, Turtle


class MyScreen:
    def __init__(self):
        self.net = Turtle()
        self.score1 = Turtle()
        self.score2 = Turtle()

        self.draw_net()
        # self.draw_score(0, 0)

    def draw_net(self):
        # prepares turtle to draw net
        self.net.color("white")
        self.net.hideturtle()
        self.net.penup()
        self.net.width(5)
        self.net.shape("square")
        self.net.goto(0, -380)
        self.net.speed("fastest")
        self.net.setheading(90)

        # writes net
        for y in range(16):
            self.net.pendown()
            self.net.forward(20)
            self.net.penup()
            self.net.forward(30)

    def draw_score(self, score_player, score_computer):

        self.score1.speed("fastest")
        self.score2.speed("fastest")

        self.score1.color("white")
        self.score2.color("white")

        self.score1.hideturtle()
        self.score2.hideturtle()

        self.score1.penup()
        self.score2.penup()

        self.score1.goto(-90, 320)
        self.score2.goto(90, 320)

        self.score1.write(f"{score_player}", align="center", font=("Arial", 40, "bold"))
        self.score2.write(f"{score_computer}", align="center", font=("Arial", 40, "bold"))

    def blackout_score(self, score_player, score_computer):
        self.score1.speed("fastest")
        self.score2.speed("fastest")

        self.score1.color("black")
        self.score2.color("black")

        self.score1.hideturtle()
        self.score2.hideturtle()

        self.score1.penup()
        self.score2.penup()

        self.score1.goto(-90, 320)
        self.score2.goto(90, 320)

        self.score1.begin_fill()
        self.score2.begin_fill()

        self.score1.circle(80)
        self.score2.circle(80)

        self.score1.end_fill()
        self.score2.end_fill()
