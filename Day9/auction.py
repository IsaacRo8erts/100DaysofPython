from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo

print(logo)
bidder = True
bids = {}

while bidder:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: "))
    bids[name] = bid
    other_bidder = input("Are there any other bidders?: Type 'yes' or 'no'.\n")

    if other_bidder == "yes":
        bidder = True
        clear()
    else:
        bidder = False
        # Could put this in a function
        for entry in bids:
            highest_bid = bids[entry]
            if bids[entry] > highest_bid:
                highest_bid = bids[entry]
        print(f"The winner is {entry} with a bid of £{bids[entry]}")