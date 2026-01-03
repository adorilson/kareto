"""
Jogo da Velha

Este jogo está parcialmente implementado.
Seu objetivo é compreender o funcionamento do código
e completar ou melhorar os trechos indicados com TODO,
para que fique funcionalmente semelhante ao jogo
presente no pacote freegames.

Depois, você deverá resolver os desafios propostos abaixo.

Exercícios

1. Dar cores e espessuras diferentes para X e O.
2. Tratar o clique em uma casa já ocupada.
3. Detectar quando um jogador venceu.
4. Criar um jogador computador.
"""

import turtle
from freegames import line


def desenhar_grade():
    """Desenha a grade do jogo."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def desenhar_x(x, y):
    """Desenha o símbolo X."""
    line(x, y, x + 133, y + 133)
    line(x, y + 133, x + 133, y)


def desenhar_o(x, y):
    """Desenha o símbolo O."""
    turtle.up()
    turtle.goto(x + 67, y + 5)
    turtle.down()
    turtle.circle(62)


def ajustar_para_celula(valor):
    """Ajusta o valor para a célula da grade."""
    return ((valor + 200) // 133) * 133 - 200


estado = {'jogador': 0}
jogadores = [desenhar_x, desenhar_o]


def ao_clicar(x, y):
    """Desenha X ou O na célula clicada."""
    x = ajustar_para_celula(x)
    y = ajustar_para_celula(y)

    jogador = estado['jogador']
    desenhar = jogadores[jogador]

    desenhar(x, y)
    turtle.update()

    # TODO
    # Finalizar o controle de estado definir o próximo jogador



turtle.setup(420, 420, 370, 0)
turtle.hideturtle()
turtle.tracer(False)

desenhar_grade()
turtle.update()

turtle.onscreenclick(ao_clicar)
turtle.mainloop()
