"""
Exercicios:

1) Faça cada passo da tartaruga ter uma cor diferente
2) Aumente/diminua o diâmetro do círculo
"""

import turtle

turtle = turtle.Turtle()

for c in range(360):
    turtle.color('red')
    turtle.forward(1)
    turtle.right(1)
