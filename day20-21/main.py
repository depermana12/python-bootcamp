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

snek_running = True
screen.listen()

screen.onkey(snek.up, "Up")
screen.onkey(snek.down, "Down")
screen.onkey(snek.left, "Left")
screen.onkey(snek.right, "Right")


while snek_running:
    screen.update()
    time.sleep(0.1)
    snek.move()
    snek_head = snek.snek_body_seg[0]

    # Detect collisions against food
    if snek.snek_body_seg[0].distance(food) < 15:
        food.random_food()
        snek.extend_body_seg()
        scoreboard.scores()

    # Detect walls
    if snek_head.xcor() > RIGHT_WALL or snek_head.xcor() < LEFT_WALL or snek_head.ycor() > TOP_WALL or snek_head.ycor() < BOTTOM_WALL:
        snek_running = False
        scoreboard.game_over()

    # Detect collisions against the tail
    for seg in snek.snek_body_seg[1:]:
        if snek.snek_body_seg[0].distance(seg) < 10:
            snek_running = False
            scoreboard.game_over()

screen.exitonclick()
