from turtle import Turtle
FONT = ("Courier", 10, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.speed("fastest")
        self.color("white")
        self.penup()
        self.goto(0.00, 281)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"SCORE: {self.score}", move=False, align="center", font=FONT)

    def update(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()

