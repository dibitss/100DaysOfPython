import turtle
import random

# import colorgram

# extracted_colors = colorgram.extract('/home/dibits/Repos/100DaysOfPython/Day 018/image.jpg', 30)
# colors = []

# for color in extracted_colors:
#     colors.append((color.rgb.r, color.rgb.g, color.rgb.b)) 

# print(colors)

colors = [(195, 167, 125), (154, 144, 48), (144, 110, 32), (236, 241, 236), (201, 200, 110), (95, 38, 21), (84, 124, 122), (81, 111, 143), (12, 38, 68), (88, 69, 77), (201, 144, 147), (179, 90, 89), (225, 226, 229), (34, 87, 84), (33, 85, 87), (228, 224, 226), (178, 91, 94), (90, 48, 41), (144, 166, 161), (146, 159, 172), (107, 137, 132), (81, 42, 43), (85, 46, 47), (212, 182, 179), (178, 200, 194), (112, 128, 148), (212, 180, 181), (52, 62, 77), (180, 192, 205)]

turtle.colormode(255)
t = turtle.Turtle()
t.speed("fastest")
t.up()
t.hideturtle()
t.goto(-250, -280)

for _ in range(10):
    t.goto(-250, t.pos()[1] + 50)
    for _ in range(10):
        t.dot(20, random.choice(colors))
        t.up()
        t.forward(50)



s = turtle.Screen()
s.exitonclick()

