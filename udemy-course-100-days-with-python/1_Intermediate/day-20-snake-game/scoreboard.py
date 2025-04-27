from turtle import Turtle

ALIGN = "center"
FRONT = ("Courier", 20, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        with open("best_score.txt", mode  = "r") as file:
            self.highest_score = int(file.read())
        self.points = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0,270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.points} Highest score: {self.highest_score}", False, ALIGN, FRONT)

    def add_point(self):
        self.points += 1
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", False, ALIGN, FRONT)

    def reset(self):
        if self.points > self.highest_score:
            self.highest_score = self.points
            with open("best_score.txt", mode='w') as file:
                file.write(f"{self.highest_score}")
        self.points = 0
        self.update_scoreboard()