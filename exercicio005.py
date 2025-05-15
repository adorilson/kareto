"""
Exercícios

1) Aumente o tamanho do envelope
2) Use formas diferentes da tartaruga enquanto faz a aba e enquanto faz o corpo
3) Deixe o envelope colorido
4) Reduza o aba do envelope
"""

import turtle

bowser = turtle.Turtle()
bowser.color("red")

for _ in [1, 2, 3]:
    bowser.forward(100)
    bowser.right(120)

for _ in [1, 2, 3, 4]:
    bowser.forward(100)
    bowser.right(90)

turtle.mainloop()
