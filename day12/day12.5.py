import random

EASY_LEVEL = 10
HARD_LEVEL = 5


def difficulty():
    level = input("Choose difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL

def compare_answer(user_guess, computer_number, lives):
    if user_guess > computer_number:
        print("Too high")
        return lives - 1
    elif user_guess < computer_number:
        print("Too low")
        return lives - 1
    else:
        print(f"You guess the correct number {user_guess}. You win!")
        return

def start_game():

    print("Welcome to the number guessing game!")
    print("I'm thingking of a number between 1 and 100.")
    computer_number = random.randint(1, 100)
    print(f"your hint is {computer_number}")
    lives = difficulty()
    print(f"You have {lives} lives")

    user_guess = 0
    while user_guess != computer_number:
        print(f"You have {lives} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        lives = compare_answer(user_guess, computer_number, lives)
        if lives == 0:
            print("You lose")
            return



start_game()





