from turtle import Turtle, Screen

screen = Screen()
tim = Turtle()

def move_forward():
    tim.forward(10)

def move_back():
    tim.back(10)

def left():
    tim.left(10)

def right():
    tim.right(10)

def clear():
    tim.clear()
    tim.up()
    tim.home()
    tim.down()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="d", fun=right)
screen.onkey(key="a", fun=left)
screen.onkey(key="c", fun=clear)
screen.exitonclick()