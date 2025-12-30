"""
Paint – Desenho de formas

Este jogo está parcialmente implementado.
Seu objetivo é compreender o funcionamento do código
e completar ou melhorar os trechos indicados com TODO,
para que fique funcionalmente semelhante ao jogo
presente no pacote freegames.

Depois, você deverá resolver os desafios propostos abaixo:

Desafios:
1. Adicionar uma nova cor.
2. Completar o desenho do círculo.
3. Completar o desenho do retângulo.
4. Completar o desenho do triângulo.
5. Adicionar um parâmetro de largura do traço.
"""

import turtle
from freegames import vector


def linha(inicio, fim):
    """Desenha uma linha do ponto inicial ao final."""
    turtle.up()
    turtle.goto(inicio.x, inicio.y)
    turtle.down()
    turtle.goto(fim.x, fim.y)


def quadrado(inicio, fim):
    """Desenha um quadrado a partir de dois pontos."""
    turtle.up()
    turtle.goto(inicio.x, inicio.y)
    turtle.down()
    turtle.begin_fill()

    for _ in range(4):
        turtle.forward(fim.x - inicio.x)
        turtle.left(90)

    turtle.end_fill()


def circulo(inicio, fim):
    """Desenha um círculo."""
    pass  # TODO


def retangulo(inicio, fim):
    """Desenha um retângulo."""
    pass  # TODO


def triangulo(inicio, fim):
    """Desenha um triângulo."""
    pass  # TODO


def clique(x, y):
    """Armazena o ponto inicial ou desenha a forma."""
    inicio = estado['inicio']

    if inicio is None:
        estado['inicio'] = vector(x, y)
    else:
        forma = estado['forma']
        fim = vector(x, y)
        forma(inicio, fim)
        estado['inicio'] = None


def armazenar(chave, valor):
    """Armazena um valor no estado."""
    estado[chave] = valor


estado = {'inicio': None, 'forma': linha}

turtle.setup(420, 420, 370, 0)
turtle.onscreenclick(clique)
turtle.listen()

turtle.onkey(turtle.undo, 'u')
turtle.onkey(lambda: turtle.color('black'), 'K')
turtle.onkey(lambda: turtle.color('white'), 'W')
turtle.onkey(lambda: turtle.color('green'), 'G')
turtle.onkey(lambda: turtle.color('blue'), 'B')
turtle.onkey(lambda: turtle.color('red'), 'R')
turtle.onkey(lambda: armazenar('forma', linha), 'l')
turtle.onkey(lambda: armazenar('forma', quadrado), 's')
turtle.onkey(lambda: armazenar('forma', circulo), 'c')
turtle.onkey(lambda: armazenar('forma', retangulo), 'r')
turtle.onkey(lambda: armazenar('forma', triangulo), 't')

turtle.mainloop()
