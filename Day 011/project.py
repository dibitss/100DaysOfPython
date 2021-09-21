import random

def clear():
    from subprocess import call
    import os

    from art import logo

    _ = call('clear' if os.name =='posix' else 'cls')
    print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    return random.choice(cards)

def calculate_score(cards):
    score = sum(cards)

    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and score > 21:
        score -= 10

    return score

def dealer_deal(cards):
    score = calculate_score(cards)
    while score < 17:
        cards.append(deal_card())
        score = calculate_score(cards)

    return cards, score
        

play = True
while play:
    clear()
    player = {"cards": [], "score": 0}
    dealer = {"cards": [], "score": 0}

    for _ in range(2):
        player["cards"].append(deal_card())
        dealer["cards"].append(deal_card())
    
    deal_another = True
    while deal_another and player["score"] < 21:
        player["score"] = calculate_score(player["cards"])
        if player["score"] == 0:
            print('You got Blackjack! You win!')
            deal_another = False
        else:
            print(f'\tYour cards: {player["cards"]}, current score: {player["score"]}')
            print(f'\tDealer\'s first card: {dealer["cards"][0]}')
            
            if input("Type 'y' to get another card. Type 'n' to pass: ") == 'n':
                deal_another = False
            else:
                player["cards"].append(deal_card())
                player["score"] = calculate_score(player["cards"])
    
    dealer["cards"], dealer["score"] = dealer_deal(dealer["cards"])

    print(f'\tYour final hand: {player["cards"]}, final score: {player["score"]}')
    print(f'\tDealer\'s final hand: {dealer["cards"]}, final score: {dealer["score"]}')

    if player["score"] > 21:
        print("You went over. You lose")
    elif dealer["score"] > 21:
        print("Dealer went over. You win")
    elif player["score"] > dealer["score"]:
        print("You win!")
    elif dealer["score"] > player["score"]:
        print("You lose!")
    else:
        print("It's a tie!")
    
    if input("Do you want to play another game of Blackjack? Type 'y' or 'n'") == 'n':
        play = False