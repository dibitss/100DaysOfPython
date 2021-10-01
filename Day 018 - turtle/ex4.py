import turtle as t
import random

tim = t.Turtle()

########### Challenge 4 - Random Walk ########
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

tim.pensize(10)
tim.speed(10)
t.colormode(255)

while True:
    tim.color(random_color())
    move = random.randint(1, 4)
    if move == 1:
        tim.forward(20)
    elif move == 2:
        tim.right(90)
    elif move == 3:
        tim.backward(20)
    elif move == 4:
        tim.left(90)