"""
Exercícios

1) Acrescente mais cores à lista de cores possíveis
2) Faça o triângulo apontar para cima
3) Remova a cor vermelha da lista de cores possíveis
4) Mude a largura da linha
"""


import turtle
import random

turtle = turtle.Turtle()
colors = ['red', 'purple', 'blue']

for _ in [1, 2, 3]:
    color = random.choice(colors)
    turtle.color(color)
    turtle.forward(100)
    turtle.right(120)

