from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Car:
    def __init__(self):
        self.factory = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def generate(self):
        """
        creating a random car position at each rolled dice equal to 1
        and append to factory list
        :return:
        """
        random_chance = randint(1, 5)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.color(choice(COLORS))
            random_y = randint(-250, 250)
            new_car.goto(300, random_y)
            self.factory.append(new_car)

    def move(self):
        """
        initial car speed
        :return:
        """
        for car in self.factory:
            car.backward(self.car_speed)

    def speed_up(self):
        """
        increase speed every level up
        :return:
        """
        self.car_speed += MOVE_INCREMENT
