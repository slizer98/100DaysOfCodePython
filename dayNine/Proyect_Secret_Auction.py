from clear import clear
from art import logo

bids = {}

def get_participants():
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bids[name] = bid

def highes_bidder():
    winner = ''
    max_bid = 0
    for name in bids:
        bid_amount = bids[name]
        if bid_amount > max_bid:
            max_bid = bid_amount
            winner = name
    print(f"The winner is {winner} with a bid of ${max_bid}")

print(logo)
print("Welcome to the secret auction program.")

get_participants()

more_bids = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

while more_bids != "no":
    clear()
    get_participants()
    more_bids = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

highes_bidder()