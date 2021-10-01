import turtle
import random

s = turtle.Screen()

s.setup(width=500, height=400)
s.title("Turtle Race")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

user_bet = s.textinput(title="Make your bet", prompt='Which turtle will win the race? Enter a color\n(red, orange, yellow, green, blue, purple)')

y = -210
t = {}
for color in colors:
    t[color] = (turtle.Turtle(shape="turtle"))
    t[color].color(color)
    t[color].up()

    y += 60
    t[color].goto(-235, y)

race_finished = False
while not race_finished:
    for color in colors:
        t[color].forward(random.randint(0, 10))
        if t[color].position()[0] >= 225:
            race_finished = True
            winner = color
            break

if winner == user_bet:
    print('You win!')
else:
    print(f'You lost. The winner was {winner}')

s.exitonclick()