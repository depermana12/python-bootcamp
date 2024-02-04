from operator import truediv
import random

word_list = ["advark", "baboon", "camel"]


chosen_world = random.choice(word_list)

print(chosen_world)

display =[]
endgame = False

for letter in chosen_world:
    display.append("_")

print(display)


while not endgame:
    guess = input("guess a letter ").lower()
    for position in range(len(chosen_world)):
        char = chosen_world[position]
        if char == guess:
            display[position] = char
    print(display)

    if "_" not in display:
        endgame = True
        print("you win")