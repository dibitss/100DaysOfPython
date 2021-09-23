import turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snartle:
    def __init__(self):
        self.snartles = []
        self.create_snartle()
        self.head = self.snartles[0]
    
    def create_snartle(self):
        x = 0
        for _ in range(3):
            snartle = turtle.Turtle(shape="square")
            snartle.color("white")
            snartle.up()
            snartle.setx(x)
            x = snartle.xcor() - 20
            self.snartles.append(snartle)

    def move(self):
        for segment in range(len(self.snartles) -1, 0, -1):
            self.snartles[segment].goto(self.snartles[segment - 1].pos())
        self.snartles[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)