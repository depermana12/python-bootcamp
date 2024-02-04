import math

wallheight = int(input("enter the height of the wall: "))
wallwidth = int(input("enter the width of the wall: "))
paintcoverage = 5


def paintcalculator(height, width, coverage):
    area = height * width
    numcan = math.ceil(area / coverage)
    print(f"You need {numcan} cans of paint")


paintcalculator(wallheight, wallwidth, paintcoverage)
