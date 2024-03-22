"""
Exercícios

1) Mude/defina a forma da tartaruga
2) Mude a ordem das cores
3) Mude a largura da linha
4) Faça a tartaruga desenhar dois quadrados
"""

import turtle

oogway = turtle.Turtle()
oogway.pensize(5)

for color in ['blue', 'black', 'red', 'pink']:
    oogway.color(color)
    oogway.forward(100)
    oogway.right(90)
