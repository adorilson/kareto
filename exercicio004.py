"""
Exercícios

1) Acrescente ao menos mais duas cores à lista de cores possíveis
Veja os nomes de cores válidos em: https://pt.wikipedia.org/wiki/Lista_de_cores
(coluna Nome Web)
2) Faça o triângulo apontar para cima
3) Remova a cor vermelha da lista de cores possíveis
4) Mude a largura da linha
"""

import turtle
import random

kame = turtle.Turtle()
cores = ['red', 'purple', 'blue']

for _ in [1, 2, 3]:
    cor = random.choice(cores)
    kame.color(cor)
    kame.forward(100)
    kame.right(120)
