from game_data import data
import random

def format_data(account):
    name = account.get("name")
    job = account.get("description")
    country = account.get("country")
    followers = account.get("follower_count")
    return(f"{name}, a {job} from {country}")

def compare(guess, data1_follower, data2_follower):
    if data1_follower > data2_follower:
        return guess == "A"
    else:
        return guess == "B"

try_again = True
score = 0
random_data2 = random.choice(data)

while try_again:
    random_data1 = random_data2
    random_data2 = random.choice(data)
    while random_data1 == random_data2:
        random_data2 = random.choice(data)

    print(f"Compare A:{format_data(random_data1)}")
    print("Versus")
    print(f"Compare B:{format_data(random_data2)}")

    guess = input("Who has more followers? Type 'A' or 'B': ")

    data1_follower = random_data1.get("follower_count")
    data2_follower = random_data2.get("follower_count")
    answer = compare(guess, data1_follower, data2_follower)


    if answer:
        print("You're right")
        score += 1
        print(f"You got {score} score")
    else:
        print("You're wrong")
        score -= 1
        try_again = False