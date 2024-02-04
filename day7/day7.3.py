import random

word_list = ["advark", "baboon", "camel"]


chosen_world = random.choice(word_list)

guess = input("guess a letter ").lower()

for char in chosen_world:
    if char == guess:
        print("True")
    else:
        print("Wrong")

