"""Simon Diz

Exercícios

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


# -------------------------------------------------
# Estado do jogo
# -------------------------------------------------
# padrao: sequência correta de azulejos
# palpites: sequência inserida pelo jogador
padrao = []
palpites = []


# -------------------------------------------------
# Representação do tabuleiro
# -------------------------------------------------
# Cada azulejo é identificado por uma posição (vector)
# e associado a uma cor clara e uma escura.
# PONTO DE INTERVENÇÃO:
# - adicionar novos azulejos
# - alterar layout do tabuleiro
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
    # Cada posição do dicionário define um azulejo
    for pos, (_, escuro) in azulejos.items():
        square(pos.x, pos.y, 200, escuro)
    update()


def piscar(pos):
    """
    Pisca um azulejo:
    1. desenha a cor clara
    2. espera um tempo
    3. volta para a cor escura
    """
    claro, escuro = azulejos[pos]

    square(pos.x, pos.y, 200, claro)
    update()
    sleep(0.5)   # PONTO DE INTERVENÇÃO: velocidade do jogo

    square(pos.x, pos.y, 200, escuro)
    update()
    sleep(0.5)


# -------------------------------------------------
# Lógica do jogo
# -------------------------------------------------
def aumentar_sequencia():
    """
    Aumenta o padrão em uma posição aleatória
    e mostra toda a sequência ao jogador.
    """
    pos = choice(list(azulejos))
    padrao.append(pos)

    for pos in padrao:
        piscar(pos)

    # Limpa os palpites para a nova rodada
    palpites.clear()
    print('Tamanho do padrão:', len(padrao))


def clique(x, y):
    """
    Trata o clique do jogador.
    Cada clique deve corresponder ao próximo
    azulejo do padrão.
    """
    onscreenclick(None)

    x = floor(x, 200)
    y = floor(y, 200)
    pos = vector(x, y)

    indice = len(palpites)

    # Condição de erro: clique incorreto
    if pos != padrao[indice]:
        # PONTO DE INTERVENÇÃO:
        # - mostrar mensagem de erro
        # - reiniciar o jogo
        bye()

    palpites.append(pos)
    piscar(pos)

    # Se o jogador completou a sequência,
    # o padrão cresce
    if len(palpites) == len(padrao):
        aumentar_sequencia()

    onscreenclick(clique)


def iniciar(x, y):
    """Inicia o jogo."""
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
