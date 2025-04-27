import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

STARTING_MOVE_DISTANCE = 5

speed = STARTING_MOVE_DISTANCE
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()

cars = []

screen.listen()
screen.onkey(player.move,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if player.check_line():
        scoreboard.add_point()
        player.start_position()
        speed += 4

    if random.randint(1,6) == 6:
        cars.append(CarManager(speed))

    for car in cars:
        car.move_car()
        #Detect collision
        if player.distance(car) < 20 and (car.xcor()-10) > player.xcor():
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()