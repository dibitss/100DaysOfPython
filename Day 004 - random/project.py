import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [rock, paper, scissors]
computer_hand = random.choice(options)
user_choice = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors: "))
if user_choice < 0 or user_choice > 2:
    print("You don't know how to play, you lose!")
else:
    user_hand = options[user_choice]

    print("You chose:" + user_hand)

    print("\nComputer chose:" + computer_hand)

    if user_hand == computer_hand:
        print("It's a tie")
    elif user_hand == rock and computer_hand == scissors:
        print("You won")
    elif user_hand == paper and computer_hand == rock:
        print("You won")
    elif user_hand == scissors and computer_hand == paper:
        print("You won")
    else:
        print("Computer won")