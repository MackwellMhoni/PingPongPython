from turtle import Turtle

class score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.scoreboard()

    def scoreboard (self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Arial", 24, "bold"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Arial", 24, "bold"))

    def leftPoint(self):
        self.l_score += 1
        self.scoreboard()

    def rightPoint(self):
        self.r_score += 1
        self.scoreboard()