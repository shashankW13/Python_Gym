from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 24, 'bold')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.score = 0

    def update_score(self):
        self.clear()
        self.goto(0, 280)
        self.write(f'Score: {self.score}',
                   align=ALIGNMENT,
                   font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f'GAME OVER',
                   align=ALIGNMENT,
                   font=FONT)