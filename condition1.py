
print("Welcome to the rollercoaster!")

heigth = int(input("please enter your height in cm "))

if heigth >= 150:
    print("You're allowed to enter")
    age = int(input("please enter your age "))
    if age <= 10:
        print("please pay $5 ticket")
    elif age <= 17:
        print("please pay $7 ticket")
    else:
        print("please pay $10 ticket")
else:
    print("Sorry, you're not allowed to enter")