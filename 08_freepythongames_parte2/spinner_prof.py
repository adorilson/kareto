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

"""
Leitura orientada:
- O estado do programa está concentrado no dicionário `estado`
- O movimento é controlado por decremento gradual (simulação de atrito)
- A animação depende de ontimer → laço temporal explícito
- O ângulo é função direta do estado (estado → visual)
"""

import turtle

# Estado global do sistema (variável mutável central)
estado = {'giro': 0}


def desenhar_spinner():
    """
    Responsável apenas pelo desenho.
    Observe a separação entre lógica (estado)
    e representação visual (turtle).
    """
    turtle.clear()

    # Conversão do estado em rotação
    angulo = estado['giro'] / 10
    turtle.right(angulo)

    # Cada braço é desenhado explicitamente
    turtle.forward(100)
    turtle.dot(120, 'red')
    turtle.backward(100)

    turtle.right(120)
    turtle.forward(100)
    turtle.dot(120, 'green')
    turtle.backward(100)

    # TODO: completar o terceiro braço
    turtle.right(120)
    turtle.forward(100)
    turtle.dot(120, 'blue')
    turtle.backward(100)

    turtle.right(120)
    turtle.update()


def animar():
    """
    Laço de animação:
    - Atualiza o estado
    - Redesenha
    - Agenda próxima execução
    """
    if estado['giro'] > 0:
        estado['giro'] -= 1  # simula desaceleração

    desenhar_spinner()
    turtle.ontimer(animar, 20)


def impulsionar():
    """
    Evento de entrada:
    altera o estado, não o desenho diretamente.
    """
    estado['giro'] += 10


# Configuração gráfica
turtle.setup(420, 420, 370, 0)
turtle.hideturtle()
turtle.tracer(False)
turtle.width(20)

# Eventos
turtle.listen()
turtle.onkey(impulsionar, 'space')

animar()
turtle.mainloop()
