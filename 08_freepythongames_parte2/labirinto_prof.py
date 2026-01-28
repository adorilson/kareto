"""Labirinto, mova de um lado ao outro.

Este jogo está parcialmente implementado.
Seu objetivo é compreender o funcionamento do código
e completar ou melhorar os trechos indicados com TODO,
para que fique funcionalmente semelhante ao jogo
presente no pacote freegames.

Depois, você deverá resolver os desafios propostos abaixo:

1. Manter pontuação contando os cliques (e tempo).
2. Gerar o mesmo labirinto duas vezes.
3. Permitir que o jogador desfaça o último movimento.
4. Fazer com que o caminho percorrido seja gradualmente.
5. Evitar que no primeiro clique seja feito um traço.
"""

import turtle
from random import random

from freegames import line


def desenhar():
    """Desenha o labirinto."""
    # Configuração visual inicial do labirinto
    turtle.color('black')
    turtle.width(5)

    # Estrutura de repetição dupla:
    # percorre uma "grade" 10x10 de células de 40x40 pixels
    for x in range(-200, 200, 40):
        for y in range(-200, 200, 40):

            # Decisão aleatória define a orientação da parede
            # Esse ponto é central para a geração procedural do labirinto
            if random() > 0.5:
                line(x, y, x + 40, y + 40)
            else:
                # TODO desenhar uma linha que vai do ponto (x, y + 40) ao ponto (x + 40, y)
                line(x, y + 40, x + 40, y)

    turtle.update()


primeiro = True

def toque(x, y):
    """Desenha o caminho do jogador ao clicar."""
    # Verificação de limites da tela:
    # se sair da área jogável, a caneta é levantada
    if abs(x) > 198 or abs(y) > 198:
        turtle.up()
    else:
        turtle.down()

    # Estilo do traço do jogador
    turtle.width(2)
    turtle.color('red')

    global primeiro

    if primeiro:
        turtle.up()
        turtle.goto(x, y)
        turtle.down()
        primeiro = False

    # Movimento direto para a posição clicada
    turtle.goto(x, y)

    # Ponto marca visualmente o trajeto percorrido
    turtle.dot(4)


# Configuração da janela
turtle.setup(420, 420, 370, 0)

# O cursor não faz parte da estética do jogo
turtle.hideturtle()

# Controle manual de atualização para melhor desempenho
turtle.tracer(False)

# TODO chamar função que desenha o labirinto
# Desenho inicial do labirinto
desenhar()

# TODO Associar função toque ao clique do mouse
# Associação de eventos de mouse
turtle.onscreenclick(toque)

turtle.mainloop()
