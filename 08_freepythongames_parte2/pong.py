"""
Pong

Este jogo está parcialmente implementado.
Seu objetivo é compreender o funcionamento do código
e completar ou melhorar os trechos indicados com TODO,
para que fique funcionalmente semelhante ao jogo
presente no pacote freegames.

Depois, você deverá resolver os desafios propostos abaixo:

1. Alterar as cores do jogo.
2. Qual é a taxa de atualização (frame rate)? Deixe mais rápida ou mais lenta.
3. Alterar a velocidade da bola.
4. Alterar o tamanho das raquetes.
5. Modificar como a bola rebate nas paredes.
6. Como adicionar um jogador controlado pelo computador?
7. Adicionar uma segunda bola.

"""

from random import choice, random
import turtle
from freegames import vector


def valor():
    """Gera um valor aleatório entre (-5, -3) ou (3, 5)."""
    return (3 + random() * 2) * choice([1, -1])


# Estado global do jogo
bola = vector(0, 0)                 # posição da bola
direcao = vector(valor(), valor())  # velocidade da bola
raquetes = {1: 0, 2: 0}             # posição vertical das raquetes


def mover(jogador, deslocamento):
    raquetes[jogador] += deslocamento


def raquete(x, y, largura, altura):
    turtle.penup()
    turtle.goto(x, y)
    turtle.down()
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(largura)
        turtle.left(90)
        turtle.forward(altura)
        turtle.left(90)
    turtle.end_fill()


def desenhar():
    turtle.clear()

    raquete(-200, raquetes[1], 10, 50)
    # TODO Criar a segunda raquete

    bola.move(direcao)

    turtle.up()
    turtle.goto(bola.x, bola.y)
    turtle.dot(10)
    turtle.update()

    if bola.y < -200 or bola.y > 200:
        direcao.y = -direcao.y

    if bola.x < -185:
        if raquetes[1] <= bola.y <= raquetes[1] + 50:
            direcao.x = -direcao.x
        else:
            return

    if bola.x > 185:
        if raquetes[2] <= bola.y <= raquetes[2] + 50:
            direcao.x = -direcao.x
        else:
            return

    turtle.ontimer(desenhar, 50)


turtle.setup(420, 420, 370, 0)
turtle.hideturtle()
turtle.tracer(False)

turtle.listen()
turtle.onkey(lambda: mover(1, 20), 'w')
turtle.onkey(lambda: mover(1, -20), 's')
turtle.onkey(lambda: mover(2, 20), 'i')
turtle.onkey(lambda: mover(2, -20), 'k')

desenhar()

turtle.mainloop()
