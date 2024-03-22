"""
Exercicios:

1) Faça cada passo da tartaruga ter uma cor diferente
2) Aumente/diminua o diâmetro do círculo
"""

import turtle

raphael = turtle.Turtle()

for _ in range(360):
    raphael.color('red')
    raphael.forward(1)
    raphael.right(1)
