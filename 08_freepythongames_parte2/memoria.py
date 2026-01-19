"""Memória, jogo de quebra-cabeça de pares.

Este jogo está parcialmente implementado.
Seu objetivo é compreender o funcionamento do código
e completar ou melhorar os trechos indicados com TODO,
para que fique funcionalmente semelhante ao jogo
presente no pacote freegames.

Depois, você deverá resolver os desafios propostos abaixo.

Desafios:

1. Contar e imprimir quantos cliques ocorrem.
2. Reduzir o número de peças para um tabuleiro 4x4.
3. Detectar quando todas as peças forem reveladas.
4. Centralizar peças de um único dígito.
5. Usar letras em vez de números.
"""

import turtle
import random

from freegames import path

carro = path('car.gif')
pecas = list(range(32)) * 2
estado = {'marca': None}
escondido = [True] * 64


def quadrado(x, y):
    """Desenha um quadrado branco com contorno preto em (x, y)."""
    #TODO rescrever de forma que desenhe um quadrado a partir do ponto (x,y)
    # com 50 pixels de lado
    turtle.up()
    turtle.goto(-210, -210)
    turtle.down()
    turtle.color('black', 'white')
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(420)
        turtle.left(90)
    turtle.end_fill()


def indice(x, y):
    """Converte coordenadas (x, y) no índice da peça."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def coordenadas(contador):
    """Converte o índice da peça em coordenadas (x, y)."""
    return (contador % 8) * 50 - 200, (contador // 8) * 50 - 200


def toque(x, y):
    """Atualiza a marcação e as peças escondidas com base no clique."""
    posicao = indice(x, y)
    marca = estado['marca']

    if marca is None or marca == posicao or pecas[marca] != pecas[posicao]:
        estado['marca'] = posicao
    else:
        escondido[posicao] = False
        escondido[marca] = False
        estado['marca'] = None


def desenhar():
    """Desenha a imagem e as peças."""
    turtle.clear()
    turtle.goto(0, 0)
    turtle.shape(carro)
    turtle.stamp()

    for contador in range(64):
        if escondido[contador]:
            x, y = coordenadas(contador)
            quadrado(x, y)

    marca = estado['marca']

    if marca is not None and escondido[marca]:
        x, y = coordenadas(marca)
        turtle.up()
        turtle.goto(x + 2, y)
        turtle.color('black')
        turtle.write(pecas[marca], font=('Arial', 30, 'normal'))

    turtle.update()
    turtle.ontimer(desenhar, 100)


random.shuffle(pecas)

turtle.setup(420, 420, 370, 0)
turtle.addshape(carro)
turtle.hideturtle()
turtle.tracer(False)

# TODO associar o clique do mouse à função toque


desenhar()
turtle.mainloop()
