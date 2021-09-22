import turtle as t
import random

tim = t.Turtle()
scree = t.Screen()
########### Challenge 3 - Draw Shapes ########

def random_color():
    colors_list = ["gold1", "red", "green", "blue", "DeepPink1", "CornFlowerBlue"]
    return random.choice(colors_list)

def draw_shape(sides):
    angle = 360 / sides
    tim.color(random_color())
    for _ in range(sides):
        tim.forward(100)
        tim.right(angle)


for sides in range(3, 20):
    draw_shape(sides)



scree.exitonclick()