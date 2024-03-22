"""
Exercicios

1) Acrescente cores
2) Mude a largura da linha
3) Aumente a quantidade de linhas
"""

import turtle
import random

leonardo = turtle.Turtle()

cores = ['purple', 'blue', 'yellow', 'green', 'pink']
for _ in range (8):
    cor = random.choice(cores)
    leonardo.color(cor)
    leonardo.forward(100)
    leonardo.backward(100)
    leonardo.right(45)
