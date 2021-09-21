import random

def clear():
    from subprocess import call
    import os

    from art import logo

    _ = call('clear' if os.name =='posix' else 'cls')
    print(logo)

clear()
print('Welcome to the Number Guessing Game!')
print('I\'m thinking of a number between 1 and 100.')
difficulty = input('Choose a difficulty. Type \'easy\' or \'hard\': ')

if difficulty == 'easy':
    print('You have 10 attempts remaining to guess the number.')
    attempts = 10
else: 
    print('You have 5 attempts remaining to guess the number.')
    attempts = 5

number_to_guess = random.randint(1, 100)

game_over = False
while attempts > 0 and not game_over:
    user_guess = int(input('Make a guess: '))
    if number_to_guess == user_guess:
        print(f'You got it! The answer was {number_to_guess}')
        game_over = True
    else:
        if number_to_guess > user_guess:
            print(f'Your guess {user_guess} is too Low.')
        elif number_to_guess < user_guess:
            print(f'Your guess {user_guess} is too High.')
        
        attempts -= 1
        print('Guess again.')
        print(f'You have {attempts} attempts remaining to guess the number.')

if attempts == 0:
    print(f'You\'ve run out of guesses, you lose. The number was {number_to_guess}')