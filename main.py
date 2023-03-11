from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

LARGURA = 600
ALTURA = 600
screen = Screen()
screen.setup(LARGURA, ALTURA)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
comida = Food()
placar = Scoreboard()
screen.update()

# Faz com que a cobra possa mudar de direção
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.09)
    snake.mover()

    # Detectando colisão com a comida
    if snake.cabeca.distance(comida) < 10:
        comida.local()
        placar.atualizar_pontuacao()
        snake.extender()

    # Detectando se a cobra saiu da tela
    if snake.cabeca.xcor() > 290 or snake.cabeca.xcor() < -290 or snake.cabeca.ycor() > 290 or snake.cabeca.ycor() < -290:
        game_is_on = False
        placar.game_over()

    # Dectando se a cabeça colidiu com o corpo
    for seguimento in snake.segmentos[1:]:
        if snake.cabeca.distance(seguimento) < 10:
            game_is_on = False
            placar.game_over()
screen.exitonclick()
