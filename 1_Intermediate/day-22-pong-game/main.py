from distutils.fancy_getopt import longopt_pat
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()


scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    screen.update()
    ball.move_ball()
    time.sleep(0.05)

    if abs(ball.ycor()) > 280:
        ball.change_direction_y()

    #Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 and ball.direction_x > 0:
        ball.change_direction_x()
    elif  ball.distance(l_paddle) < 50 and ball.xcor() < -320 and ball.direction_x < 0:
        ball.change_direction_x()

    #Detect the ball behind the paddle
    if ball.xcor() > 400:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -400:
        ball.reset_position()
        scoreboard.r_point()


    #Increase speed of the ball
    if ball.xcor() < -100 and ball.direction_x > 0:
        ball.direction_x = 10
    elif ball.xcor() >= -100 and ball.direction_x > 0:
        ball.direction_x = 7

    if ball.xcor() > 100 and ball.direction_x < 0:
        ball.direction_x = -10
    elif ball.xcor() <= 100 and ball.direction_x < 0:
        ball.direction_x = -7



screen.exitonclick()

