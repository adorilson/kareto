import random
import turtle
import sys
from .. import atores

LINHAS = 8
COLUNAS = 8
DIMENSAO = 50

tem_nectar_no_girassol = atores.tem_nectar_no_girassol

def Abelha():
    return abelha

def configurar_janela():
    atores.configurar_janela()
    tela = turtle.Screen()
    tela.title("Abelhinha - Fase 31")

def desenhar_mundo():
    tons_de_verde = ["green", "darkgreen", "forestgreen", "seagreen"]
    for i in range(LINHAS * COLUNAS):
        x, y = atores.xy(i)
        turtle.up()
        turtle.goto(x, y)
        turtle.down()
        turtle.pencolor("lightgreen")
        turtle.fillcolor(random.choice(tons_de_verde))
        turtle.begin_fill()
        for _ in range(4):
            turtle.forward(DIMENSAO)
            turtle.right(90)
        turtle.end_fill()
    turtle.update()

def configurar_abelha():
    abelha = atores.Abelha()
    abelha.posição = 40
    abelha.vire_para(atores.DIRECAO.LESTE)
    abelha.atualize()
    abelha.apareça()
    return abelha

configurar_janela()
desenhar_mundo()


def importado():
    return sys.argv[0] != '-m'


def nectares():
    if importado():
        return random.randint(1, 9)

    return '?'


# Girassóis nas posições 43 a 47
for i in range(41, 46):
    nectar = nectares()
    girassol = atores.Girassol(i, nectar)
    girassol.atualize()
    girassol.apareça()

# Abelha na posição 40
abelha = configurar_abelha()

turtle.update()
