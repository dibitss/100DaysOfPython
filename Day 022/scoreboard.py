import turtle

class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.up()
        self.hideturtle()
        self.right_score = 0
        self.left_score = 0
        self.write_scores()
        
    def write_scores(self):
        self.clear()
        self.goto(-100, 180)
        self.write(self.left_score, align="center", font=("Courier", 80, "bold"))
        self.goto(100, 180)
        self.write(self.right_score, align="center", font=("Courier", 80, "bold"))

    def update_scores(self, player):
        if player == "right":
            self.right_score += 1
        else:
            self.left_score += 1
        self.write_scores()
