from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.up()
        self.level = 1
        self.print_scoreboard()

    def print_scoreboard(self):
        self.clear()
        self.goto(-190, 240)
        self.write(f"Level: {self.level}", align="center", font=("Courier", 30, "bold"))

    def level_up(self):
        self.level += 1
        self.print_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over.", align="center", font=("Courier", 30, "bold"))