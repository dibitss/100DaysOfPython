import turtle

TEXT_X = 0
TEXT_Y = 270

ALIGNMENT = "center"
FONT = "courier"
FONTTYPE = "bold"
SIZE = 20

class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.up()
        self.goto(TEXT_X, TEXT_Y)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=(FONT, SIZE, FONTTYPE))

    def update_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
    
    def game_over(self):
        self.goto(0 ,0)
        self.write("GAME OVER.", move=False, align=ALIGNMENT, font=(FONT, SIZE, FONTTYPE))