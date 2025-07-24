import turtle
from functools import cache
from kareto import atores

atores.configurar_janela(titulo="Artista - Fase 71")

turtle.delay(0)

def desenha_lente(x, y):
    """Desenha uma lente quadrada com lado 100, a partir do canto inferior esquerdo (x, y)"""
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(0)
    turtle.pendown()
    for _ in range(4):
        turtle.forward(100)
        turtle.left(90)

def desenha_ponte():
    """Liga o topo das duas lentes"""
    turtle.penup()
    turtle.goto(-137.5, 100)  # topo da lente esquerda
    turtle.setheading(0)
    turtle.pendown()
    turtle.forward(100 + 75)  # até o topo da lente direita

def desenha_perna_3d(x, y):
    """Desenha uma haste na direção de 45°, simulando profundidade"""
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(45)
    turtle.pendown()
    turtle.forward(60)
    turtle.right(90)
    turtle.forward(30)

# Configuração inicial
turtle.speed(2)
turtle.pensize(3)

# Lentes com 75 pixels de distância entre elas
x_lente_esquerda = -137.5
x_lente_direita = 37.5

turtle.pencolor("lightgray")
desenha_lente(x_lente_esquerda, 0)
desenha_lente(x_lente_direita, 0)

# Ponte
desenha_ponte()

# Hastes
turtle.pencolor("black")
desenha_perna_3d(x_lente_esquerda, 100)
desenha_perna_3d(x_lente_direita + 100, 100)

# Finalização
#turtle.teleport(-75, 50)  # move para baixo
#turtle.setheading(0)  # orienta para a direita


# cache para que o artista seja criado apenas uma vez (singleton)
@cache
def Artista():
    artista = atores.Artista()
    artista.hideturtle()
    artista.pensize(3)
    artista.penup()
    artista.pencolor("black")
    artista.goto(x_lente_esquerda, 100)
    artista.pendown()
    artista.shapesize(2)
    artista.showturtle()
    return artista

#E com isso o artista aparece tanto na excução do módulo, quanto quando é importado
artista = Artista()

turtle.delay(20)
turtle.tracer(True)