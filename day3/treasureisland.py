

print("Welcome to the One Piece island.")
print("Your objective is to find the missing one piece treasure")
print("You need to type the option you want")

firstMission = input("You are on the boat at the mistyc sea. Where do you want to paddle? 'left' or 'right' ")

if firstMission == "left":
    print("You choose the right direction, let's go...")
    secondmission = input("Your boat stuck in the reef, and just a couple paddle until it dock to the island. 'swim' or 'wait'? ")
    if secondmission == "wait":
        print("You're right, better be wait rather than loosing your boat")
        thirdmission = input("you have arrived. There is a gate with three door, which one you want to enter? 'red', 'green', or 'blue' ")
        if thirdmission == "green":
            print("congratulations. you have found the missing treasure")
        elif thirdmission == "red":
            print("Game over")
        else:
            print("Game over")
    else:
        print("oh no, there is a shark waiting for you. Game over!")
else:
    print("o oh, there is dragon hide behind the mist. Game over!")