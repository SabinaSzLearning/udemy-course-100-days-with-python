from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self, speed):
        super().__init__()
        self.shape("square")
        self.shapesize(1,2,1)
        self.color(COLORS[random.randint(a = 0,b = len(COLORS)-1)])
        self.penup()
        self.goto(280, random.randint(-250,250))
        self.left(180)
        self.car_speed = speed

    def move_car(self):
        self.forward(self.car_speed)

