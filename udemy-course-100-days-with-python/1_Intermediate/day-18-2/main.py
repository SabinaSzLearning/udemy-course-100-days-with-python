# import colorgram
# list = []
# # Extract 6 colors from an image.
# colors = colorgram.extract('image.jpg', 30)
# for item in range(len(colors)):
#     list.append((colors[item].rgb.r,colors[item].rgb.g,colors[item].rgb.b))
# print(list)

import random
import turtle
from turtle import Turtle, Screen

tim = Turtle()

colors_new = [(253, 253, 252), (242, 244, 247), (241, 247, 243), (144, 76, 50), (188, 165, 117), (248, 244, 246), (166, 153, 36), (14, 46, 85), (139, 185, 176), (146, 56, 81), (42, 110, 136), (59, 120, 99), (145, 170, 177), (87, 35, 30), (64, 152, 169), (220, 209, 93), (110, 37, 31), (100, 145, 111), (165, 99, 131), (91, 122, 172), (158, 138, 158), (177, 104, 82), (55, 52, 85), (206, 182, 195), (68, 48, 63), (73, 51, 71), (173, 201, 194), (175, 198, 201), (213, 182, 176), (37, 47, 45)]

turtle.colormode(255)
tim.hideturtle()
tim.up()
tim.speed(20)
for i in range(10):
    for j in range(10):
        tim.setposition(j*50-200,i*50-200)
        tim.dot(20, colors_new[random.randint(0,len(colors_new)-1)])

screen = Screen()
screen.exitonclick()