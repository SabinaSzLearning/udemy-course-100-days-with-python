from turtle import Turtle, Screen
import random
timmy = Turtle()
timmy.shape("circle")

# for i in range(3,8):
#     for j in range(i):
#         timmy.forward(50)
#         timmy.right(360/i)

# --------------------------------------
def change_color():
    R = random.random()
    B = random.random()
    G = random.random()

    timmy.color(R, G, B)
#
#
# timmy.speed(10)
# timmy.pensize(10)
# for _ in range(100):
#     timmy.forward(30)
#     angle = int(random.randint(0,3) * 90)
#     timmy.right(angle)
#     change_color()

# --------------------------------------

timmy.speed(15)
for i in range(100):
    timmy.circle(130)
    timmy.right(360/100)
    change_color()












screen = Screen()
screen.exitonclick()