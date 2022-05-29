from art import logo
import os

print(logo)
bids = {}
bidding = True
while bidding == True:
    name = input('What is your name?')
    bid = int(input('What is your bid?'))
    bids[name] = bid
    stop_bidding = input('Are there others that want to bid?')
    if stop_bidding == 'No':
        max = 0
        for key in bids:
            if bids[key] > max:
                highest_bidder = key
                max = bids[key]
        print(f"The highest_bidder is {highest_bidder}")
        bidding = False
    else:
        os.system('clear')
