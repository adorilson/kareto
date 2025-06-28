import turtle
from kareto import atores
import random

LINHAS = 8
COLUNAS = 8
DIMENSAO = 50

linha = 4
colunas = list(range(COLUNAS))

def configurar_janela():
    atores.configurar_janela()
    tela = turtle.Screen()
    tela.title("Abelhinha - Fase 26")

def desenhar_mundo():
    celulas = [None] * (LINHAS * COLUNAS)
    tons_de_verde = ["green", "darkgreen", "forestgreen", "seagreen"]
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

# Posições dos elementos: toda a linha central, exceto a posição inicial da abelha
posicoes = [linha * COLUNAS + c for c in colunas[1:]]

# Distribuição fixa: alterna girassol e colmeia, mas troca o segundo girassol por colmeia
for i, pos in enumerate(posicoes):
    if i == 2:
        elemento = atores.Colméia(pos, 1)
        elemento.atualize()
        elemento.apareça()
    elif i % 2 == 0:
        elemento = atores.Girassol(pos, 1)
        elemento.atualize()
        elemento.apareça()
    else:
        elemento = atores.Colméia(pos, 1)
        elemento.atualize()
        elemento.apareça()

# Posição inicial da abelha na primeira casa da linha central
abelha = configurar_abelha(linha * COLUNAS + colunas[0], atores.DIRECAO.LESTE)

turtle.update()
