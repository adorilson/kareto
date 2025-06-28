import turtle
import random
from kareto import atores

LINHAS = 8
COLUNAS = 8
DIMENSAO = 50

# Linha central
linha = 4
colunas = list(range(COLUNAS))

# Funções utilitárias

def configurar_janela():
    atores.configurar_janela()
    tela = turtle.Screen()
    tela.title("Abelhinha - Fase 25")

def desenhar_mundo():
    celulas = [None] * (LINHAS * COLUNAS)
    for i, _ in enumerate(celulas):
        x, y = atores.xy(i)
        turtle.up()
        turtle.goto(x, y)
        turtle.down()
        turtle.pencolor("lightgreen")
        turtle.fillcolor(random.choice(["green", "darkgreen", "forestgreen", "seagreen"]))
        turtle.begin_fill()
        for _ in range(4):
            turtle.forward(DIMENSAO)
            turtle.right(90)
        turtle.end_fill()
    turtle.update()

def adicionar_nuvens(posicoes):
    nuvens = []
    for posicao in posicoes:
        nuvem = atores.Nuvem(posicao)
        nuvem.atualize()
        nuvem.apareça()
        nuvens.append(nuvem)
    return nuvens

def configurar_abelha(posicao, direcao):
    abelha = atores.Abelha()
    abelha.posição = posicao
    abelha.vire_para(direcao)
    abelha.atualize()
    abelha.apareça()
    return abelha

def Abelha():
    return abelha

def esconda_nuvens():
    import time
    time.sleep(1)
    for nuvem in nuvens:
        nuvem.esconda()
    turtle.update()

def importado():
    import sys
    return sys.argv[0] != '-m'

configurar_janela()
desenhar_mundo()

# Posições das nuvens: da segunda até a oitava casa da linha central
posicoes_nuvens = [linha * COLUNAS + c for c in colunas[1:]]

# Sob cada nuvem, aleatoriamente, uma colmeia ou um girassol
for pos in posicoes_nuvens:
    if random.choice([True, False]):
        elemento = atores.Colméia(pos, 1)
        elemento.atualize()
        elemento.apareça()
    else:
        elemento = atores.Girassol(pos, 1)
        elemento.atualize()
        elemento.apareça()

nuvens = adicionar_nuvens(posicoes_nuvens)

# Posição inicial da abelha na primeira casa da linha central
abelha = configurar_abelha(linha * COLUNAS + colunas[0], atores.DIRECAO.LESTE)

turtle.update()

#if importado():
#    esconda_nuvens()

def laço_principal():
    turtle.update()
    turtle.ontimer(laço_principal, 500)

laço_principal()
