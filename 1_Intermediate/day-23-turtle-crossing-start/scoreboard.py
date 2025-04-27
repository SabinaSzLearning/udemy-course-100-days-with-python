# from socket import send_fds
from turtle import Turtle

FONT = ("Courier", 15, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("Black")
        self.goto(-200,240)
        self.score = 1
        self.update()

    def update(self):
        self.clear()
        self.write(f"Level: {self.score}", align="center", font=FONT)

    def add_point(self):
        self.score += 1
        self.update()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align="center", font=FONT)

