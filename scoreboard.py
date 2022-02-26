from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 24, 'normal')
COLOR = "white"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color(COLOR)
        self.penup()
        self.goto(x=0, y=260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over.", align=ALIGNMENT, font=FONT)


    def update_scores(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

