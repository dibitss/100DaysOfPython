import turtle
from time import sleep
from snartle import Snartle
from food import Food
from scoreboard import Scoreboard

screen = turtle.Screen()
screen.title("Snartle")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

scoreboard = Scoreboard()
snartle = Snartle()
food = Food()

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

    if snartle.head.distance(food) < 15:
        food.relocate()
        snartle.grow()
        scoreboard.update_score()

    if snartle.head.xcor() > 280 or snartle.head.xcor() < -280 or snartle.head.ycor() > 280 or snartle.head.ycor() < -280:
        scoreboard.reset()
        snartle.reset()

    for segment in snartle.segments[1:]:
        if snartle.head.distance(segment) < 10:
            scoreboard.reset()
            snartle.reset()

screen.exitonclick()