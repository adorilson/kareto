"""
Snake, jogo clássico de arcade.

Desafios:

1. Como tornar a cobra mais rápida ou mais lenta?
2. Como fazer a cobra atravessar as bordas da tela?
3. Como fazer a comida se mover?
4. Alterar o jogo para que a cobra responda a cliques do mouse.
5. Exibir a pontuação na tela para o jogador, conforme a cobra come
as comidas

Leia o código com atenção antes de começar.
"""

from random import randrange
from turtle import *

from freegames import square, vector


# -------------------------
# Estado inicial do jogo
# -------------------------

comida = vector(0, 0)

cobra = [
    vector(10, 0),
]

direcao = vector(0, -10)


# -------------------------
# Funções auxiliares
# -------------------------

def mudar_direcao(x, y):
    """Altera a direção do movimento da cobra."""
    direcao.x = x
    direcao.y = y


def dentro_limites(cabeca):
    """Retorna True se a cabeça estiver dentro da área do jogo."""
    return -200 < cabeca.x < 190 and -200 < cabeca.y < 190


# -------------------------
# Lógica principal do jogo
# -------------------------

def mover():
    """Move a cobra um passo à frente."""
    cabeca = cobra[-1].copy()
    cabeca.move(direcao)

    #TODO: 
    # Extraia `cabeca in cobra` para uma função
    if not dentro_limites(cabeca) or cabeca in cobra:
        square(cabeca.x, cabeca.y, 9, 'red')
        update()
        return

    cobra.append(cabeca)

    if cabeca == comida:
        print('Tamanho da cobra:', len(cobra))

        # Nova posição aleatória para a comida
        comida.x = randrange(-15, 15) * 10
        comida.y = randrange(-15, 15) * 10
    else:
        # TODO:
        # Remova o primeiro segmento da cobra
        pass

    clear()

    # Desenho da cobra
    for segmento in cobra:
        square(segmento.x, segmento.y, 9, 'black')

    # Desenho da comida
    square(comida.x, comida.y, 9, 'green')

    update()

    # TODO:
    # Ajuste o tempo para controlar a velocidade do jogo
    ontimer(mover, 100)


# -------------------------
# Configuração da janela
# -------------------------

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()

onkey(lambda: mudar_direcao(10, 0), 'Right')
onkey(lambda: mudar_direcao(-10, 0), 'Left')
onkey(lambda: mudar_direcao(0, 10), 'Up')
onkey(lambda: mudar_direcao(0, -10), 'Down')

mover()
done()
