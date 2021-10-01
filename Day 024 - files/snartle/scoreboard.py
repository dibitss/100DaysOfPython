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
        with open("/home/dibits/Repos/100DaysOfPython/Day 024/snartle/data.txt") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.hideturtle()
        self.up()
        self.goto(TEXT_X, TEXT_Y)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", move=False, align=ALIGNMENT, font=(FONT, SIZE, FONTTYPE))

    def update_score(self):
        self.score += 1
        self.update_scoreboard()
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("/home/dibits/Repos/100DaysOfPython/Day 024/snartle/data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0 ,0)
    #     self.write("GAME OVER.", move=False, align=ALIGNMENT, font=(FONT, SIZE, FONTTYPE))