from turtle import Turtle
import random
TAMANHO = 0.7

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=TAMANHO, stretch_wid=TAMANHO)
        self.color("blue")
        self.speed("fastest")
        self.local()

    def local(self):
        rand_x = 20 * random.randint(-14, 14)
        rand_y = 20 * random.randint(-14, 14)
        self.goto(rand_x, rand_y)
