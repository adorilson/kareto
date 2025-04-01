import time
import turtle

turtle.setup(620, 500, 1190, 1000)
time.sleep(1)

artista = turtle.Turtle()
artista.speed(1)

# Seu código a partir daqui

artista.shape('turtle') # comece tirando o # no início dessa linha
time.sleep(1)

artista.forward(100)
artista.left(120)
artista.forward(100)
artista.left(120)
artista.forward(100)
artista.left(120)


# Instrução necessária para que a janela não se feche
turtle.mainloop()
