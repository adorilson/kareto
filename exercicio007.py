"""
Exercicios:

1) Mude a distancia entre as lentes dos óculos
2) Mude o tamanho das lentes
"""

import turtle

michelangelo = turtle.Turtle()
michelangelo.color("green")

for _ in range(4):
    michelangelo.left(90)
    michelangelo.backward(100)

michelangelo.backward(50)
michelangelo.backward(100)
michelangelo.right(90)

for _ in range(3):
    michelangelo.forward(100)
    michelangelo.left(90)
