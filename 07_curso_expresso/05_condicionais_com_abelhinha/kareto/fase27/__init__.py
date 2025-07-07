import turtle
import kareto
from kareto import atores

LINHAS = 8
COLUNAS = 8
DIMENSAO = 50

kareto.atores.SPEED = 100

def configurar_janela():
    atores.configurar_janela()
    tela = turtle.Screen()
    tela.title("Abelhinha - Fase 27")

def desenhar_mundo():
    celulas = [None] * (LINHAS * COLUNAS)
    tons_de_verde = ["green", "darkgreen", "forestgreen", "seagreen"]
    import random
    for i, _ in enumerate(celulas):
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

def configurar_abelha(posicao, direcao):
    abelha = atores.Abelha()
    abelha.posição = posicao
    abelha.vire_para(direcao)
    abelha.atualize()
    abelha.apareça()
    return abelha

def Abelha():
    return abelha

def importado():
    import sys
    return sys.argv[0] != '-m'

configurar_janela()
desenhar_mundo()

# Preenche o jardim: girassóis e colmeias
for linha in range(LINHAS):
    for coluna in range(COLUNAS):
        pos = linha * COLUNAS + coluna
        if coluna < 7:
            flor = atores.Girassol(pos, 1)
            flor.atualize()
            flor.apareça()
        else:
            colmeia = atores.Colméia(pos, 7)
            colmeia.atualize()
            colmeia.apareça()

# Posição inicial da abelha: primeira linha, primeira coluna
abelha = configurar_abelha(0, atores.DIRECAO.LESTE)

turtle.update()
