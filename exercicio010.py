"""
Exercícios

1) Faça cada quadrado ter uma cor
2) Faça cada quadrado com um formato diferente da tartaruga
3) Faça os quadrados não se tocarem
4) Desenhe um quadrado maior ao redor dos demais quadrados
"""

import turtle

touché = turtle.Turtle()

for _ in range(4):
    touché.forward(100)
    touché.right(90)

for _ in range(4):
   touché.left(90)
   touché.forward(100)

for _ in range(4):
   touché.forward(100)
   touché.left(90)

for _ in range(4):
   touché.right(90)
   touché.forward(100)
