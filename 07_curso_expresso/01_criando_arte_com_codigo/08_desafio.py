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
artista.right(angulo_menor)
artista.forward(curto)
artista.right(90)
artista.forward(curto)
artista.right(angulo_menor)
artista.forward(longo)
artista.right(angulo_menor)
artista.forward(curto)
artista.right(90)
artista.forward(curto)
artista.right(angulo_menor)

# Instrução necessária para que a janela não se feche
turtle.mainloop()
