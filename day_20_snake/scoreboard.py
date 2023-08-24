from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        self.score = 0
        with open("C:/Users/celik/PycharmProjects/day_20_snake/data.txt") as file:
            self.high_score = int(file.read())
        self.speed("fastest")
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()

        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score:  {self.score}  High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("C:/Users/celik/PycharmProjects/day_20_snake/data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
