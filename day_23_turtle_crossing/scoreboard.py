from turtle import Turtle
FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        self.penup()
        self.hideturtle()
        self.goto(-290, 260)

    def write_score(self, level):
        self.clear()
        self.write(f"Level: {level}", font=FONT)

    def write_game_over(self):
        self.speed("fastest")
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)