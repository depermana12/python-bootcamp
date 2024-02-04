
print("Welcome to the secret auction progam.")
other_participant = True
participants = {}


while other_participant:
    names = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    participants[names] = bid
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    if other_bidders == "no":
        other_participant = False


def highest_bidder(bidding_record):
    highest_price = 0
    for client in bidding_record:
        if bidding_record[client] > highest_price:
            highest_price = bidding_record[client]
            winner = client
    print(f"The winner is {winner} with ${highest_price} bid")


highest_bidder(participants)
