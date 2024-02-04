import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]

userInput = int(input("choose your weapon. enter 0 for rock, 1 for paper, and 2 for scissors: "))

rpcChoices = len(game_images) - 1
computerInput = random.randint(0, rpcChoices - 1)


if userInput < 0 or userInput >= 3:
    print("you type invalid number. you lose")
else:
    print("you choose")
    print(game_images[userInput])
    print("computer choose")
    print(game_images[computerInput])
    if userInput == 0 and computerInput == 2:
        print("you win")
    elif userInput == 2 and computerInput == 0:
        print("you lose")
    elif computerInput > userInput:
        print("you lose")
    elif userInput > computerInput:
        print("you win")
    elif userInput == computerInput:
        print("draw")