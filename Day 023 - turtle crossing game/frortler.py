from turtle import Turtle

PACE = 20

class Frortler(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.up()
        self.setheading(90)
        self.go_to_start()
        

    def go_to_start(self):
        self.goto(0, -280)

    def go_up(self):
        self.goto(self.xcor(), self.ycor() + PACE)