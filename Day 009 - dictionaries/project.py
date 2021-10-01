#from replit import clear
#HINT: You can call clear() to clear the output in the console.

def clear():
    from subprocess import call
    import os

    from art import logo

    _ = call('clear' if os.name =='posix' else 'cls')
    print(logo)

def get_winner(bidders_record):
    bid_winner = {"name": "", "bid": 0}

    for name in bidders_record:
        if bidders_record[name] > bid_winner["bid"]:
            bid_winner["name"] = name
            bid_winner["bid"] = bidders_record[name]

    clear()
    print(f'The auction was won by {bid_winner["name"]} with a bid of ${bid_winner["bid"]}')

print("Welcome to secret auctions")

bidders = {}

another_one = True
while another_one:
    clear()
    name = input("What's your name? ")
    bid = input("What's your bid? $")

    bidders[name] = int(bid)

    if input("Is there another bidder? Type 'yes' or 'no' ") == 'no':
        another_one = False

get_winner(bidders)