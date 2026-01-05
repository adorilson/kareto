"""
Spinner

Este jogo está parcialmente implementado.
Seu objetivo é compreender o funcionamento do código
e completar ou melhorar os trechos indicados com TODO,
para que fique funcionalmente semelhante ao jogo
presente no pacote freegames.

Depois, você deverá resolver os desafios propostos abaixo.

Desafios:

1. Alterar o padrão visual do spinner.
2. Fazer o spinner responder a cliques do mouse.
3. Alterar a aceleração do movimento.
4. Permitir que o spinner gire para frente e para trás.
"""

import turtle

estado = {'giro': 0}


def desenhar_spinner():
    """Desenha o spinner."""
    turtle.clear()

    angulo = estado['giro'] / 10
    turtle.right(angulo)

    turtle.forward(100)
    turtle.dot(120, 'red')
    turtle.backward(100)

    turtle.right(120)
    turtle.forward(100)
    turtle.dot(120, 'green')
    turtle.backward(100)

    # TODO: complete o terceiro braço

    turtle.right(120)
    turtle.update()


def animar():
    """Controla a animação."""
    if estado['giro'] > 0:
        estado['giro'] -= 1

    desenhar_spinner()
    turtle.ontimer(animar, 20)


def impulsionar():
    """Aplica impulso ao spinner."""
    estado['giro'] += 10 


turtle.setup(420, 420, 370, 0)
turtle.hideturtle()
turtle.tracer(False)
turtle.width(20)
turtle.listen()

turtle.onkey(impulsionar, 'space')

animar()
turtle.mainloop()
