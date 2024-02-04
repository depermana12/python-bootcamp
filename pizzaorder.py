
print("Welcome to the pizza deliveries")
size = input("what size pizza do you want? S, M, or L ")
addpepperoni = input("do you want pepperoni? Y or N ")
extracheese = input("do you want extra cheese? Y or N ")

price = 0

if size == "S":
    print("the price for small pizza is $15")
    price += 15
elif size == "M":
    print("price for medium pizza is $20")
    price += 20
else:
    print("price for large pizza is $25")
    price += 25

if addpepperoni == "Y":
    if size == "S":
        print("extra charge for pepperoni is $2")
        price += 2
    else:
        print("extra charge for pepperoni is $3")
        price += 3
else:
    print("okay no pepperoni")

if extracheese == "Y":
    print("extra charge for cheese is $1")
    price += 1
else:
    print("okay no cheese")

tax = 10 / 100 * price

totalprice = tax + price

print(f"Your order price is ${price} with 10% tax is ${tax}. The total bill is ${totalprice}")
