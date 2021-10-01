import turtle as t

tim = t.Turtle()

########### Challenge 2 - Draw a Dashed Line ########

tim.shape("turtle")
tim.color("DeepPink1")

for _ in range(10):
    tim.forward(10)
    tim.up()
    tim.forward(10)
    tim.down()
