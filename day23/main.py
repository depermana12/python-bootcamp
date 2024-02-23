from turtle import Screen
from player import Player
from car import Car
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)

player = Player()
game = Scoreboard()
car = Car()

screen.listen()
screen.onkeypress(player.move, "Up")

game_running = True

while game_running:
    time.sleep(0.1)
    screen.update()

    car.generate()
    car.move()

    for gocar in car.factory:
        if gocar.distance(player) < 20:
            game_running = False
            game.is_over()

    if player.finish_line():
        player.start_pos()
        car.speed_up()
        game.level_up()

screen.exitonclick()
