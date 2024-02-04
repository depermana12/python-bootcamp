

row1 = ["📁", "📁", "📁"]
row2 = ["📁", "📁", "📁"]
row3 = ["📁", "📁", "📁"]

treasureChest = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

direction = input("please enter row horizontal and col vertical direction: ")


horizontal = int(direction[0])
vertical = int(direction[1])


#pointedDirection = treasureChest[vertical - 1]
#pointedDirection[horizontal-1] = "x"

treasureChest[vertical - 1] [horizontal -1] = "x"


print(f"{row1}\n{row2}\n{row3}")

