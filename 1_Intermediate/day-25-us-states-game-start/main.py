import turtle
from turtle import Turtle

import pandas

screen = turtle.Screen()
screen.title(" U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
x_val = data.x.to_list()
y_val = data.y.to_list()

correct_answers = []
answer_state = screen.textinput(title=f"{len(correct_answers)}/50 States Correct", prompt="What's another state's name?")

while len(correct_answers) < 50:

    answer_state = answer_state.title()
    if answer_state == "Exit":
        states_to_learn = [item for item in states if item not in correct_answers]
        df = pandas.DataFrame(states_to_learn, columns=['To learn'])
        df.to_csv("states.csv")
        break

    if answer_state in states and answer_state not in correct_answers:
        id = data[data.state == answer_state].index[0]

        text = Turtle()
        text.penup()
        text.hideturtle()
        text.goto(x_val[id] , y_val[id])
        text.write(data.state[id],move=False, align="left", font=("Arial", 8, "normal"))
        correct_answers.append(answer_state)
        answer_state = screen.textinput(title=f"{len(correct_answers)}/50 States Correct", prompt="Correct. What's another state's name?")
    elif answer_state in correct_answers:
        answer_state = screen.textinput(title=f"{len(correct_answers)}/50 States Correct", prompt="Present. What's another state's name?")
    else:
        answer_state = screen.textinput(title=f"{len(correct_answers)}/50 States Correct", prompt="Wrong. What's another state's name?")

