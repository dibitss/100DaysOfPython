import random
from art import vs
from game_data import data

def clear():
    from subprocess import call
    import os

    from art import logo

    _ = call('clear' if os.name =='posix' else 'cls')
    print(logo)

def get_vs(last_b):
    if last_b == {}:
        a = random.choice(data)
        data.remove(a)
    else:
        a = last_b
    return a, random.choice(data)

def check_answer(a, b, guess):
    if a.get('follower_count') > b.get('follower_count'):
        return guess == 'a'
    else:
        return guess == 'b'

clear()

game_continues = True
last_b = {}
score = 0
while game_continues:
    option_a, option_b = get_vs(last_b)

    print(f'\nCompare A: {option_a.get("name")}, a {option_a.get("description")}, from {option_a.get("country")}.')
    print(vs)
    print(f'\nAgainst B: {option_b.get("name")}, a {option_b.get("description")}, from {option_b.get("country")}.')
    guess = input('Who has more followers? Type \'A\' or \'B\': ').lower()

    clear()

    is_correct = check_answer(option_a, option_b, guess)
    if is_correct:
        score += 1
        print(f'You are right! Current score: {score}')
    else:
        print(f'Sorry, that\'s wrong. Final score: {score}')
        break

    last_b = option_b


