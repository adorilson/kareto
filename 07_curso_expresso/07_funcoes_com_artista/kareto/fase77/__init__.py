import turtle
from functools import cache
from kareto import atores
import math

atores.configurar_janela(titulo="Artista - Fase 77")


# Configurações iniciais
turtle.delay(0)
turtle.speed(0)


turtle.pensize(3)
turtle.pencolor("lightgray")

# Começa do canto inferior esquerdo
turtle.penup()
turtle.goto(-150, 100)
turtle.pendown()

LADO = 50  # Tamanho do lado do triângulo equilátero

# Desenha um triângulo apontando para dentro
def triangulo():
    for _ in range(3):
        turtle.forward(LADO)
        turtle.right(120)

# Desenha uma linha com 4 triângulos
def linha_de_triangulos():
    for _ in range(4):
        triangulo()
        turtle.forward(LADO)


# Desenha os quatro lados do losango com triângulos alinhados
def padrao_losango():
    # Parte superior
    turtle.penup()
    turtle.setheading(0)
    turtle.pendown()
    linha_de_triangulos()

    # Lado direito
    turtle.penup()
    turtle.setheading(-60)
    turtle.pendown()
    linha_de_triangulos()

    # Parte inferior
    turtle.penup()
    turtle.setheading(180)
    turtle.pendown()
    linha_de_triangulos()

    # Lado esquerdo
    turtle.penup()
    turtle.setheading(120)
    turtle.pendown()
    linha_de_triangulos()

# Executar
padrao_losango()

turtle.hideturtle()



# cache para que o artista seja criado apenas uma vez (singleton)
@cache
def Artista():
    artista = atores.Artista()
    artista.hideturtle()
    artista.goto(-150, 100)
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