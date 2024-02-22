from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position, color):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.speed("fastest")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def paddle_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def paddle_down(self):
        self.goto(self.xcor(), self.ycor() - 20)
