import turtle as t
from random import choice, randint

timmy = t.Turtle()
t.colormode(255)

timmy.shape("turtle")
timmy.color("purple", "aqua")

timmy.pensize(2)
timmy.speed("fastest")

# direction = [0, 90, 180, 270]


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)

    selected_color = (r, g, b)
    return selected_color

def full_circle(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)
        # timmy.setheading(choice(direction))

full_circle(5)