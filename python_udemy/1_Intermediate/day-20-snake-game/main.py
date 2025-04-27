from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.15)
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.add_point()

    #Detect collision with wall
    if abs(snake.head.xcor()) > 280 or abs(snake.head.ycor()) > 280:
        # game_is_on = False
        scoreboard.reset()
        snake.reset()

    #Detect collision with tail
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            # game_is_on = False
            scoreboard.reset()
            snake.reset()


screen.exitonclick()