#step 5 is create a scorecoard
from turtle import Turtle
ALIGNMENT="center"
FONT=("Courier",16,"normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0,270)     
        self.write(f"score: {self.score} ", align= ALIGNMENT, font= FONT)
        self.hideturtle()

    def score_increase(self):
        self.score+=1
        self.clear()
        self.write(f"score: {self.score} ", align= ALIGNMENT, font= FONT)

    def game_over(self):
        self.goto(0,0)
        self.game=" GAME OVER"
        self.write(f"{self.game}",align= "center",font=FONT)
        