import time
import turtle

turtle.setup(500, 500, 1000, 1000)
time.sleep(1)

artista = turtle.Turtle()
artista.speed(1)

# Seu código a partir daqui

artista.shape('turtle')
time.sleep(1)

longo = 150
curto = 75
angulo_menor = 45
angulo_maior = 75

artista.forward(longo)
artista.left(120)
artista.forward(longo)
artista.left(120)
artista.forward(longo)
artista.left(120)


# Instrução necessária para que a janela não se feche
turtle.mainloop()
