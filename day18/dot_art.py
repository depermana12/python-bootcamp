import turtle as t
from random import choice

screen = t.Screen()
timmy = t.Turtle()
timmy.hideturtle()
timmy.speed("fastest")
t.colormode(255)


colors = [(248, 245, 246), (213, 154, 96), (52, 107, 132), (179, 77, 31), (202, 142, 31),
          (115, 155, 171), (124, 79, 99), (122, 175, 156), (229, 236, 239), (226, 198, 131), (242, 247, 244),
          (192, 87, 108), (11, 50, 64), (55, 38, 19), (45, 168, 126), (47, 127, 123), (200, 121, 143), (168, 21, 29),
          (228, 92, 77), (244, 162, 160), (38, 32, 35), (2, 25, 24), (78, 147, 171), (170, 23, 18), (19, 79, 90),
          (101, 126, 158), (235, 166, 171), (177, 204, 185), (49, 62, 84), (164, 203, 208), (183, 190, 204),
          (83, 70, 40), (11, 112, 106)]


timmy.penup()
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)


for dot_count in range(1, 101):
    timmy.color(choice(colors))
    timmy.dot(30, choice(colors))
    timmy.forward(50)
    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)


screen.exitonclick()
