
print("Welcome to the love calculator")
yourName = input("Whats is your name? ")
yourCrushName = input("What is your crush name? ")

ourName = yourName.lower() + yourCrushName.lower()

concatT = ourName.count("t")
concatR = ourName.count("r")
concatU = ourName.count("u")
concatE = ourName.count("e")

concatL = ourName.count("l")
concatO = ourName.count("o")
concatV = ourName.count("v")
concatVE = ourName.count("e")

trueCount = concatT + concatR + concatU + concatE
loveCount = concatL +concatO + concatV + concatVE

totalTrueLove = int(str(trueCount) + str(loveCount))


if totalTrueLove < 10 or totalTrueLove > 90:
    print(" you go together like mentos")
elif totalTrueLove >= 40 and totalTrueLove <= 50:
    print("you are alright together")
else:
    print("your score is z")

print(f"true count is {trueCount}. love count is {loveCount}. love calculator result is {totalTrueLove}%")
print(type(totalTrueLove))