from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        file = open("../snake-game-part-2-final/newfile.txt", mode="r")
        c = file.read()
        self.highscore=c
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score},high score{self.highscore}", align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def score_reset(self):


        if self.score > int(self.highscore):
            self.highscore = self.score
            file=open("../snake-game-part-2-final/newfile.txt",mode="w")
            c=file.write(f"{self.highscore}")

        self.score=0
        self.update_scoreboard()



    def increase_score(self):
        # self.highscore+=1
        self.score += 1
        self.clear()
        self.update_scoreboard()
