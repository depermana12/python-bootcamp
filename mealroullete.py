
import random

names = input("Please enter your name separated by comma: ")

namesSplit = names.split(", ")

#namesLength = len(namesSplit)
#pickRandom = random.randint(0, namesLength - 1)
#pickNames = namesSplit[pickRandom]


pickChoiceName = random.choice(namesSplit)

print(pickChoiceName + "will pay the bill today")

#print(f"{pickRandom} {pickNames} will pay the bill for the meal today")
