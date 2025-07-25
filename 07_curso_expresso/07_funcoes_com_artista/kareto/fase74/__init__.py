import turtle
from functools import cache
from kareto import atores

atores.configurar_janela(titulo="Artista - Fase 74")


# Configurações iniciais
turtle.delay(0)
turtle.speed(0)
turtle.pensize(3)
turtle.pencolor("lightgray")

def desenha_quadrado(x, y, lado):
    turtle.penup()
    turtle.goto(x, y+50) # fiquei com preguiça fazer outras mudanças
    turtle.setheading(0)
    turtle.pendown()
    for _ in range(4):
        turtle.forward(lado)
        turtle.right(90)

# Tamanho e separação
lado = 50
espaco = 50

# Desenhar os três quadrados
for i in range(3):
    x = -150 + i * (lado + espaco)
    y = 0
    desenha_quadrado(x, y, lado)



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