from turtle import Screen
from snake import Snake
import time

snek = Snake()
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snek_running = True
screen.listen()

while snek_running:
    screen.update()
    time.sleep(0.1)
    snek.move()

    screen.onkey(snek.up,"Up")
    screen.onkey(snek.down, "Down")
    screen.onkey(snek.left,"Left")
    screen.onkey(snek.right, "Right")

screen.exitonclick()
