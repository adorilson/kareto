"""
Exercícios

1) Aumente o tamanho do envelope
2) Use formas diferentes da tartaruga enquanto faz a aba e enquanto faz o corpo
3) Deixe o envelope colorido
4) Reduza o aba do envelope
"""

import turtle

turtle = turtle.Turtle()
turtle.color('red')

for _ in [1, 2, 3]:
    turtle.forward(100)
    turtle.right(120)

for _ in [1, 2, 3, 4]:
  turtle.forward(100)
  turtle.right(90)
