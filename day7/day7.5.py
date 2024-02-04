import random

word_list = ["advark", "baboon", "camel"]


chosen_world = random.choice(word_list)

print(chosen_world)

guess = input("guess a letter ").lower()

display =[]

for char in chosen_world:
    if char == guess:
        display.append(char)
    else:
        display.append("_")
    
print(display)

