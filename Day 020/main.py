import turtle
import random
from time import sleep
from snartle import Snartle

# def turn_right():
#     for index in range(len(snartles)):
#         snartles[index].setheading(snartles[index].heading() + 90)
        
screen = turtle.Screen()
screen.title("Snartle")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

snartle = Snartle()

screen.listen()
screen.onkey(key="Up", fun=snartle.up)
screen.onkey(key="Down", fun=snartle.down)
screen.onkey(key="Left", fun=snartle.left)
screen.onkey(key="Right", fun=snartle.right)

dead = False
while not dead:
    screen.update()
    sleep(0.1)
    
    snartle.move()

screen.exitonclick()