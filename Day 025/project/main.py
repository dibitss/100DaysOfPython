import turtle
import pandas

screen = turtle.Screen()
screen.title("50 US States")
image = "/home/dibits/Repos/100DaysOfPython/Day 025/project/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_data = pandas.read_csv("/home/dibits/Repos/100DaysOfPython/Day 025/project/50_states.csv")
all_states = states_data.state.to_list()

correct_answers = []
while len(correct_answers) < 50:
    answer = screen.textinput(f"{len(correct_answers)}/50 - Guess the state", "Enter a state name").title()
    if answer == "Exit":
        ## Original code
        # for state in correct_answers:
            # all_states.remove(state)
        
        ## Code with list comprehension (Day 26)
        _ = [all_states.remove(state) for state in all_states if state in correct_answers ]
        
        pandas.DataFrame(all_states).to_csv("/home/dibits/Repos/100DaysOfPython/Day 025/project/states_to_learn.csv")
        break
    if answer in all_states:
        correct_answers.append(answer)
        state = states_data[states_data.state == answer]
        x = int(state.x)
        y = int(state.y)
        
        sturtle = turtle.Turtle()
        sturtle.penup()
        sturtle.hideturtle()
        sturtle.goto(x, y)
        sturtle.write(answer, align="center", font=("courier", "10", "bold"))
