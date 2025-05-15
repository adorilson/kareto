"""
Exercicios

1) Era para ser um envelope. Mas saiu errado. Corrija.
"""

import turtle

donatello = turtle.Turtle()
donatello.color("green")

for _ in [1, 2, 3]:
    donatello.forward(100)
    donatello.right(120)

for _ in [1, 2, 3, 4]:
    donatello.left(90)
    donatello.forward(100)
