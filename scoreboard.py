from turtle import Turtle
ALINHAMENTO = "center"
FONTE = ("Courier", 22, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.pontuacao = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.atualizar_placar()

    def atualizar_placar(self):
        self.write(f"Placar = {self.pontuacao}", align=ALINHAMENTO, font=FONTE)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALINHAMENTO, font=FONTE)

    def atualizar_pontuacao(self):
        self.pontuacao += 1
        self.clear()
        self.atualizar_placar()
