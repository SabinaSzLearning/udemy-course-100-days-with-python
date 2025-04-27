import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(500,400)
user_bet = screen.textinput("Make your bet","Which turtle will win? enter a color")

number_of_turtle = 6
colors = ["red", "blue", "green", "yellow", "purple", "orange"]
turtles = []
is_race_on = True

for i in range(number_of_turtle):
    turtles.append(Turtle(shape="turtle"))
    turtles[i].color(colors[i])

for i in range(number_of_turtle):
    turtles[i].up()
    turtles[i].goto(-200,i/number_of_turtle*200-80)

while is_race_on:
    for i in range(number_of_turtle):
        turtles[i].forward(random.randint(1,15))
        if turtles[i].xcor() > 200:
            is_race_on = False
            print(f"The winner is {colors[i]}")
            if colors[i].lower() == user_bet.lower():
                print("You win!")
            else:
                print("You lose!")
            break


screen.exitonclick()