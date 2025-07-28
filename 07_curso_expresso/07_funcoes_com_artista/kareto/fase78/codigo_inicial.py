import turtle
from kareto.fase78 import Artista

def hexagono():
    for _ in range(6):
        artista.forward(25)
        artista.right(60)

def linha_de_hexagonos():
    for _ in range(8):
        hexagono()
        artista.pule_para_frente(25)

def quadrado():
    for _ in range(4):
        artista.forward(50)
        artista.left(90)

def linha_de_quadrados():
    for _ in range(3):
        quadrado()
        artista.pule_para_frente(100)

def quadrado_deslocados():
    for _ in range(2):
        linha_de_hexagonos()
        artista.right(180)

artista = Artista()



turtle.mainloop()