import turtle
from functools import cache
from kareto import atores

atores.configurar_janela(titulo="Artista - Fase 73")

turtle.delay(0)

import turtle

# Configurações iniciais
turtle.speed(0)

def desenha_retangulo(x, y, largura, altura, cor='black', espessura=1):
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(0)
    turtle.pendown()
    turtle.pensize(espessura)
    turtle.pencolor(cor)
    for _ in range(2):
        turtle.forward(largura)
        turtle.left(90)
        turtle.forward(altura)
        turtle.left(90)

def desenha_janela(x, y, tamanho=25):
    """Desenha uma janela com 4 quadrados colados"""
    for linha in range(2):
        for coluna in range(2):
            xi = x + coluna * tamanho
            yi = y - linha * tamanho
            desenha_retangulo(xi, yi, tamanho, tamanho, cor='lightgray', espessura=3)

# Desenha o corpo da casa
desenha_retangulo(-150, -150, 300, 300, cor='black', espessura=3)

# Desenha a porta
desenha_retangulo(-40, -150, 80, 100, cor='black', espessura=3)

# Posição inicial da janela superior esquerda
x_inicial = -110
y_superior = 80
distancia_horizontal = 100
distancia_vertical = 150

# Desenha janelas superiores
for i in range(3):
    x = x_inicial + i * distancia_horizontal
    desenha_janela(x, y_superior)

# Desenha janelas inferiores (150 pixels abaixo)
for i in [0, 2]:  # Apenas a primeira e a terceira janela
    x = x_inicial + i * distancia_horizontal
    desenha_janela(x, y_superior - distancia_vertical)



# cache para que o artista seja criado apenas uma vez (singleton)
@cache
def Artista():
    artista = atores.Artista()
    artista.hideturtle()
    artista.goto(x_inicial+25, y_superior)
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