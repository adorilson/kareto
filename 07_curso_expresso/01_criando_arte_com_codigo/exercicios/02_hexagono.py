import turtle

hexagono = turtle.Turtle()
hexagono.hideturtle()

# Seu código a partir daqui
angulo = 60
lado = 100


hexagono.left(angulo)
hexagono.forward(lado)

hexagono.left(angulo)
hexagono.forward(lado)

hexagono.left(angulo)
hexagono.forward(lado)

hexagono.left(angulo)
hexagono.forward(lado)

hexagono.left(angulo)
hexagono.forward(lado)

hexagono.left(angulo)
hexagono.forward(lado)

# Instrução necessária para que a janela não se feche
turtle.mainloop()