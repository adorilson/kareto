import turtle
from functools import cache
from kareto import atores

atores.configurar_janela(titulo="Artista - Fase 75")


# Configurações iniciais
turtle.delay(0)
turtle.speed(0)


t = turtle.Turtle()
t.pensize(3)
t.pencolor("lightgray")

# Começa do canto inferior esquerdo
t.penup()
t.goto(-150, 0)
t.pendown()

# Desenha um quadrado voltado para cima ou para baixo
def quadrado_para_cima():
    for _ in range(4):
        t.forward(50)
        t.left(90)

def quadrado_para_baixo():
    for _ in range(4):
        t.forward(50)
        t.right(90)

# Alterna: cima, baixo, cima, ...
for i in range(6):
    if i % 2 == 0:
        quadrado_para_cima()
    else:
        quadrado_para_baixo()

    # Move para o próximo quadrado (sem levantar caneta)
    t.forward(50)

t.hideturtle()



# cache para que o artista seja criado apenas uma vez (singleton)
@cache
def Artista():
    artista = atores.Artista()
    artista.hideturtle()
    artista.goto(-150, 0)
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