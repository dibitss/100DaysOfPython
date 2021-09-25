import turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snartle:
    def __init__(self):
        self.segments = []
        self.create_snartle()
        self.head = self.segments[0]
    
    def add_segment(self, position):
        snartle = turtle.Turtle(shape="square")
        snartle.color("white")
        snartle.up()
        snartle.goto(position)
        self.segments.append(snartle)
            
    def create_snartle(self):
        for x in range(0, -41, -20):
            position = (x, 0)
            self.add_segment(position)

    def move(self):
        for segment in range(len(self.segments) -1, 0, -1):
            self.segments[segment].goto(self.segments[segment - 1].pos())
        self.segments[0].forward(MOVE_DISTANCE)

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

    def grow(self):
        self.add_segment(self.segments[-1].pos())

    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.create_snartle()
        self.head = self.segments[0]