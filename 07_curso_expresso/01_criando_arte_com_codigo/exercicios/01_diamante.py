import turtle

diamante = turtle.Turtle()
diamante.hideturtle()

# Seu código a partir daqui
angulo_menor = 60
angulo_maior = 120
lado = 150


diamante.left(angulo_menor)
diamante.forward(lado)

diamante.left(angulo_menor)
diamante.forward(lado)

diamante.left(angulo_maior)
diamante.forward(lado)

diamante.left(angulo_menor)
diamante.forward(lado)

# Instrução necessária para que a janela não se feche
turtle.mainloop()