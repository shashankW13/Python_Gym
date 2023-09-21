from art import logo
import os

print(logo)

bid_again = True
auction_data = []

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def winner_bidder(auction_record):
    max_bid = 0
    winner = ''
    for data in auction_record:
        for amount in data.values():
            if isinstance(amount, int):
                if amount > max_bid:
                    max_bid = amount
                    winner = data["name"]
    print(f"The winner is {winner} with a bid of ${max_bid}")

while bid_again:
    name = input("What is your name? : ")
    bid = int(input("What is your bid? : $"))

    auction_data.append({"name": name, "bid": bid})

    bidders = input("Are there any other bidders? Type 'yes' or 'no' : \n")
    if bidders == 'no':
        bid_again = False
        winner_bidder(auction_data)


    else:
        clear_screen()

print(auction_data)
