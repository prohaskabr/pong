from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.left_player_score = 0
        self.right_player_score = 0
        self.refresh()

    def refresh(self):
        self.clear()
        self.color("white")
        self.goto(0, 230)
        self.write(" - ", align="center", font=("ComicSansMs", 50, "normal"))
        self.color("yellow")
        self.goto(50, 230)
        self.write(self.right_player_score, align="center", font=("ComicSansMs", 50, "normal"))
        self.goto(-50, 230)
        self.write(self.left_player_score, align="center", font=("ComicSansMs", 50, "normal"))

    def score(self, player):
        if player == "L":
            self.left_player_score += 1
        elif player == "R":
            self.right_player_score += 1

        self.refresh()
