

print("Welcome to the tip calculator.")

price = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give?"))
people = int(input ("How many people to split?"))

totalTip = price * tip/100
totalBill = totalTip + price
totalSplit = totalBill / people

totalSplitRound = round(totalSplit, 2)
totalBillRound = round(totalBill, 2)
totalTipRound = round(totalTip, 2)

print(f"price befor tip are ${price}, the tip of {tip} is ${totalTipRound}, total bill is {totalBillRound}, the split bill of {people} people is {totalSplitRound}")

