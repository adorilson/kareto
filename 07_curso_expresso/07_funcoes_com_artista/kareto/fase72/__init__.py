import turtle
from functools import cache
from kareto import atores

atores.configurar_janela(titulo="Artista - Fase 72")

turtle.delay(0)

def desenha_estrela():
    """Desenha uma estrela"""
    for _ in range(360//45):
        turtle.forward(25)
        turtle.backward(25)
        turtle.right(45)
    
# Configuração inicial
turtle.speed(2)
turtle.pensize(3)


turtle.pencolor("lightgray")
desenha_estrela()


turtle.pencolor("black")


# cache para que o artista seja criado apenas uma vez (singleton)
@cache
def Artista():
    artista = atores.Artista()
    artista.hideturtle()
    artista.pensize(3)
    artista.penup()
    artista.pencolor("black")
    artista.pendown()
    artista.showturtle()
    return artista

#E com isso o artista aparece tanto na excução do módulo, quanto quando é importado
artista = Artista()

turtle.delay(20)
turtle.tracer(True)