import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare_winner(user_score, computer_score):
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


user_cards = []
computer_cards = []
game_over = False

for digit in range(2):
    user_cards.append(deal_card())
    computer_cards.append((deal_card()))


while not game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f"user card {user_cards} = {user_score} \ncomputer card {computer_cards[0]}")

    if user_score > 21:
        game_over = True
    else:
        reshufle = input("Type 'y' t get another card, type 'n' to pass: ")
        if reshufle == "y":
            user_cards.append(deal_card())
        else:
            game_over = True


while len(computer_cards) == 2 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)


print(f"user cards {user_cards} = {user_score}\ncomputer cards {computer_cards} = {computer_score}")
print(compare_winner(user_score, computer_score))



