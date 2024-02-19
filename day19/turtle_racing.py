from turtle import Turtle, Screen
from random import randint

start_race = False

screen = Screen()
screen.setup(500, 400)

colors = ["red", "green", "blue", "brown", "black"]
y_pos = [-100, -50, 0, 50, 100]

all_turtles = []

for turtle in range(0, 5):
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle])
    new_turtle.goto(-230, y_pos[turtle])
    all_turtles.append(new_turtle)

user_guess = screen.textinput("Make your guess", "Which turtle color will win the race?")

if user_guess:
    start_race = True

while start_race:
    for team_turtle in all_turtles:

        if team_turtle.xcor() > 230:
            start_race = False
            turtle_color = team_turtle.pencolor()
            if user_guess == turtle_color:
                print(f"You've won. The winner is {turtle_color} turtle")
            else:
                print(f"You've lost. The winner is {turtle_color} turtle")

        speed = randint(1, 10)
        team_turtle.forward(speed)

screen.exitonclick()
