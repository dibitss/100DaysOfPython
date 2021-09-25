from turtle import Screen
from scoreboard import Scoreboard
from frortler import Frortler
from time import sleep
from car import CarManager
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Frortler")

scoreboard = Scoreboard()
player = Frortler()
car_manager = CarManager()

screen.listen()
screen.onkey(key="Up", fun=player.go_up)

squashed = False
while not squashed:
    sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move()
    
    for car in car_manager.cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            squashed = True
            screen.update()

    if player.ycor() > 280:
        player.go_to_start()
        scoreboard.level_up()
        car_manager.increase_speed()
    
screen.exitonclick()