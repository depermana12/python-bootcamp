from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

TOP_WALL = 280
BOTTOM_WALL = -280

paddle_l = Paddle((-350, 0), "white")
paddle_r = Paddle((350, 0), "green")
ball = Ball()
score = Scoreboard()

screen = Screen()
screen. bgcolor("black")
screen.setup(800, 600)
screen.title("Welcome to the ping pong game")
screen.tracer(0)

screen.listen()
screen.onkeypress(paddle_l.paddle_up, "w")
screen.onkeypress(paddle_l.paddle_down, "s")
screen.onkeypress(paddle_r.paddle_up, "Up")
screen.onkeypress(paddle_r.paddle_down, "Down")

while True:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > TOP_WALL or ball.ycor() < BOTTOM_WALL:
        ball.bounce_y()

    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_ball()
        score.point_l()

    if ball.xcor() < - 380:
        ball.reset_ball()
        score.point_r()
