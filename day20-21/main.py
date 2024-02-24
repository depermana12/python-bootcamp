from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

TOP_WALL = 280
BOTTOM_WALL = -280
RIGHT_WALL = 280
LEFT_WALL = -280

snek = Snake()
food = Food()
scoreboard = Scoreboard()
screen = Screen()

screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

screen.listen()
screen.onkey(snek.up, "Up")
screen.onkey(snek.down, "Down")
screen.onkey(snek.left, "Left")
screen.onkey(snek.right, "Right")

while True:
    screen.update()
    time.sleep(0.1)
    snek.move()

    # Detect collisions against food
    if snek.head.distance(food) < 15:
        food.generate()
        snek.extend_body_seg()
        scoreboard.scores()

    # Detect walls
    if snek.head.xcor() > RIGHT_WALL or snek.head.xcor() < LEFT_WALL or \
            snek.head.ycor() > TOP_WALL or snek.head.ycor() < BOTTOM_WALL:
        scoreboard.update_high_score()
        snek.update_body_seg()

    # Detect collisions against the tail
    for seg in snek.snek_body_seg[1:]:
        if snek.head.distance(seg) < 10:
            scoreboard.update_high_score()
            snek.update_body_seg()
