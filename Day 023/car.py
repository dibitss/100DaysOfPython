from turtle import Turtle
import random

# X_LOCATIONS = [330, -330]
X_LOCATIONS = [300, -300]
Y_LOCATIONS = [-240, -180, -120, -60, 0, 60, 120, 180, 240]
COLORS = ["DeepPink1", "green", "red", "blue", "brown"]
SPEED = 5
SPEED_INCREASE = 10

class CarManager():
    def __init__(self):
        self.cars = []
        self.speed = SPEED
        self.chance = 6

    def create_car(self):
        if random.randint(1, self.chance) == 1:
            car = Turtle(shape="square")
            car.color(random.choice(COLORS))
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.up()
            car.goto((random.choice(X_LOCATIONS),random.choice(Y_LOCATIONS)))
            if car.xcor() > 0:
                car.setheading(180)
            else:
                car.setheading(0)
            self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.forward(self.speed)

    def increase_speed(self):
        self.speed += SPEED_INCREASE
        if self.chance > 1:
            self.chance -= 1
    