import turtle

PADDLE_SPEED = 30

class Paddle(turtle.Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.up()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)
    
    def move_up(self):
        new_y = self.ycor() + PADDLE_SPEED
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - PADDLE_SPEED
        self.goto(self.xcor(), new_y)