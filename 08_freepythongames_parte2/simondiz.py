"""
Simon Diz

Este jogo está parcialmente implementado.
Seu objetivo é compreender o funcionamento do código
e completar ou melhorar os trechos indicados com TODO,
para que fique funcionalmente semelhante ao jogo
presente no pacote freegames.

Depois, você deverá resolver os desafios propostos:

1. Acelerar a taxa de piscada dos azulejos.
2. Adicionar mais azulejos.
3. Quando o usuário errar, mostrar uma mensagem de "Game Over" e reiniciar o jogo.
4. Por que na função clique há duas chamadas para onscreenclick?
O que aconteceria se a primeira fosse removida?
"""

from random import choice
from time import sleep
from turtle import *

from freegames import floor, square, vector


padrao = []
palpites = []

azulejos = {
    vector(0, 0): ('red', 'dark red'),
    vector(0, -200): ('blue', 'dark blue'),
    vector(-200, 0): ('green', 'dark green'),
    vector(-200, -200): ('yellow', 'khaki'),
}


# -------------------------------------------------
# Desenho da interface
# -------------------------------------------------
def grade():
    """Desenha o tabuleiro inicial."""
    # TODO:
    # Percorra o dicionário azulejos
    # e desenhe cada azulejo usando sua cor escura
    pass


def piscar(pos):
    """Pisca um azulejo."""
    claro, escuro = azulejos[pos]

    # TODO:
    # 1. desenhe o azulejo com a cor clara
    # 2. espere um tempo
    # 3. desenhe o azulejo com a cor escura
    pass


# -------------------------------------------------
# Lógica do jogo
# -------------------------------------------------
def aumentar_sequencia():
    """Adiciona um azulejo ao padrão."""
    pos = choice(list(azulejos))
    padrao.append(pos)

    for pos in padrao:
        piscar(pos)

    palpites.clear()


def clique(x, y):
    """Responde ao clique do jogador."""
    onscreenclick(None)

    x = floor(x, 200)
    y = floor(y, 200)
    pos = vector(x, y)

    indice = len(palpites)

    # Condição de erro: clique incorreto
    if pos != padrao[indice]:
        bye()

    palpites.append(pos)
    piscar(pos)

    # Se o jogador completou a sequência,
    # o padrão cresce
    if len(palpites) == len(padrao):
        aumentar_sequencia()

    onscreenclick(clique)


def iniciar(x, y):
    aumentar_sequencia()
    onscreenclick(clique)


# -------------------------------------------------
# Configuração da janela
# -------------------------------------------------
setup(420, 420, 370, 0)
hideturtle()
tracer(False)

grade()
onscreenclick(iniciar)
mainloop()
