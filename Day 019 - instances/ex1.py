from turtle import Turtle, Screen, clear

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)

def turn_right():
    tim.right(5)

def turn_left():
    tim.left(5)

def move_backwards():
    tim.backward(10)

def clear_screen():
    tim.clear()
    tim.up()
    tim.home()
    tim.down()

screen.listen()
screen.onkey(key="Up", fun=move_forwards)
screen.onkey(key="Right", fun=turn_right)
screen.onkey(key="Left", fun=turn_left)
screen.onkey(key="Down", fun=move_backwards)
screen.onkey(key="space", fun=clear_screen)
screen.exitonclick()
