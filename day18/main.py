import turtle as t
from random import choice, randint

timmy = t.Turtle()
t.colormode(255)

timmy.shape("turtle")
timmy.color("purple", "aqua")

timmy.pensize(5)
timmy.speed(5)
direction = [0, 90, 180, 270]


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)

    selected_color = (r, g, b)
    return selected_color


for _ in range(200):
    timmy.color(random_color())
    timmy.forward(30)
    timmy.setheading(choice(direction))
