from turtle import Turtle
DISTANCIA = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake():
    def __init__(self):
        self.segmentos = []
        self.create_snake()
        self.cabeca = self.segmentos[0]
        self.cabeca.color("green")

    def create_snake(self):
        self.x = 0
        for _ in range(3):
            posicao = (self.x, 0)
            self.adicionar_segmento(posicao)
            self.x -= 20

    def adicionar_segmento(self, posicao):
        self.parte = Turtle("square")
        self.parte.color("white")
        self.parte.penup()
        self.parte.goto(posicao)
        self.segmentos.append(self.parte)

    def extender(self):
        self.adicionar_segmento(self.segmentos[-1].position())

    def mover(self):
        # Posição 3 vai para posição 2 e assim por diante.
        for num_segmento in range(len(self.segmentos) - 1, 0, -1):
            novo_x = self.segmentos[num_segmento - 1].xcor()
            novo_y = self.segmentos[num_segmento - 1].ycor()
            self.segmentos[num_segmento].goto(novo_x, novo_y)
        self.cabeca.forward(DISTANCIA)

    def up(self):
        if self.cabeca.heading() != DOWN:
            self.cabeca.setheading(UP)

    def down(self):
        if self.cabeca.heading() != UP:
            self.cabeca.setheading(DOWN)

    def right(self):
        if self.cabeca.heading() != LEFT:
            self.cabeca.setheading(RIGHT)

    def left(self):
        if self.cabeca.heading() != RIGHT:
            self.cabeca.setheading(LEFT)
