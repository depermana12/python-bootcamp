from turtle import Turtle

FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-250, 250)
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def is_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

    def level_up(self):
        self.level += 1
        self.update_score()
