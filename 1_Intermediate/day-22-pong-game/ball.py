from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.up()
        self.direction_y = 7
        self.direction_x = 7

    def move_ball(self):
        position_y = self.ycor() + self.direction_y
        position_x = self.xcor() + self.direction_x
        self.goto(position_x,position_y)


    def change_direction_y(self):
        self.direction_y *= -1

    def change_direction_x(self):
        self.direction_x *= -1

    def reset_position(self):
        self.goto(0,0)
        self.change_direction_x()