"""
Exercicios:

1) Mude a distancia entre as lentes dos óculos
2) Mude o tamanho das lentes
"""

import turtle

turtle = turtle.Turtle()
turtle.color('green')

for _ in range(4):
    turtle.left(90)
    turtle.backward(100)

turtle.backward(50)
turtle.backward(100)
turtle.right(90)

for _ in range(3):
  turtle.forward(100)
  turtle.left(90)

