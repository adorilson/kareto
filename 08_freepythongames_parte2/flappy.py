"""
Flappy

Este jogo está parcialmente implementado.
Seu objetivo é compreender o funcionamento do código
e completar ou melhorar os trechos indicados com TODO,
para que fique funcionalmente semelhante ao jogo
presente no pacote freegames.

Depois, você deverá resolver os desafios propostos abaixo.

Desafios:

1. Manter a pontuação do jogador.
2. Variar a velocidade do jogo.
3. Variar o tamanho das bolas.
4. Permitir que o pássaro avance e recue.
"""

import turtle
from random import randrange
from freegames import vector

passaro = vector(0, 0)
bolas = []


def clique(x, y):
    """Move o pássaro para cima ao clicar."""
    subida = vector(0, 30)
    passaro.move(subida)


def dentro_da_tela(ponto):
    """Retorna True se o ponto estiver dentro da tela."""
    return -200 < ponto.x < 200 and -200 < ponto.y < 200


def desenhar(vivo):
    """Desenha os elementos do jogo."""
    turtle.clear()
    turtle.goto(passaro.x, passaro.y)

    # TODO: Alterar a cor do pássaro conforme o estado
    # O vivo deve ser verde e o morto vermelho
    if vivo:
        turtle.dot(10, 'black')
    else:
        turtle.dot(10, 'black')

    for bola in bolas:
        turtle.goto(bola.x, bola.y)
        turtle.dot(20, 'black')

    turtle.update()


def mover():
    """Atualiza o estado do jogo."""
    passaro.y -= 5

    for bola in bolas:
        bola.x -= 3

    if randrange(10) == 0:
        y = randrange(-199, 199)
        bolas.append(vector(199, y))

    while len(bolas)>0 and not dentro_da_tela(bolas[0]):
        # TODO: Remover a bola fora da tela (é a bola mais antiga na lista)
        # isso é o que causa o travamento do jogo quando a bola chega na borda
        pass

    if not dentro_da_tela(passaro):
        desenhar(False)
        return

    for bola in bolas:
        if abs(bola - passaro) < 15:
            desenhar(False)
            return

    desenhar(True)
    turtle.ontimer(mover, 50)


turtle.setup(420, 420, 370, 0)
turtle.hideturtle()
turtle.up()
turtle.tracer(False)
turtle.onscreenclick(clique)

mover()

turtle.mainloop()
