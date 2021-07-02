from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(-50, 250)
        self.pencolor("white")
        self.hideturtle()
        self.clear()
        self.write(f"Score: {self.score} ", font=("Arial", 14, "normal"))

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score} ", font=("Arial", 14, "normal"))

    def game_over(self):
        self.goto(-50, 0)
        self.write("Game Over", font=("Arial", 14, "normal"))
