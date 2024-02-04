# from turtle import Turtle, Screen
#
# jimmy = Turtle()
# jimmy.shape("turtle")
# jimmy.color("brown", "blue")
# jimmy.forward(50)
#
#
# my_screen = Screen()
# my_screen.exitonclick()

from prettytable import PrettyTable 



table = PrettyTable()
table.add_column("Pokemon name", ["Pikchu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)