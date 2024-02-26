from turtle import Turtle, Screen
import pandas as pd

FONT = ("Arial", 15, "normal")
ALIGNMENT = "center"

turtle = Turtle()
screen = Screen()
screen.setup(877, 419)
screen.title("Tebak nama pulau di Indonesia")
image = "map.gif"
screen.addshape(image)
turtle.shape(image)

text = Turtle()
text.color("black")
text.hideturtle()
text.penup()

raw_data = pd.read_csv("islands.csv")
island = raw_data["island"]
island_list = island.to_list()

guessed_island = []

while len(guessed_island) < len(island_list):

    user_guess = screen.textinput(title=f"{len(guessed_island)}/5", prompt="What's another island name?").title()

    if user_guess == "Exit":
        # unanswered_island = []
        # for land in island_list:
        #     if land not in guessed_island:
        #         unanswered_island.append(land)

        unanswered_island = [land for land in island_list if land not in guessed_island]

        df = pd.DataFrame(unanswered_island, columns=["island"])
        df.to_csv("islands remaining.csv")

        break

    if user_guess in island_list:
        if user_guess in guessed_island:
            print("You're already guess that")
        else:
            guessed_island.append(user_guess)
            island_name = raw_data[raw_data.island == user_guess]
            island_x = island_name.x.values[0]
            island_y = island_name.y.values[0]
            text.goto(island_x, island_y)
            text.write(user_guess, align=ALIGNMENT, font=FONT)

screen.exitonclick()
