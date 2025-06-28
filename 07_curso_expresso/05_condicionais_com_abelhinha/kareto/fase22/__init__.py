import turtle
import random
from kareto import atores

LINHAS = 8
COLUNAS = 8
DIMENSAO = 50

# Posição inicial da abelha (exemplo: 10, virada para leste)
pos_inicial_abelha = 10

def quadrado(x, y):
    tons_de_verde = ["green", "darkgreen", "forestgreen", "seagreen"]
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

def configurar_janela():
    atores.configurar_janela()
    tela = turtle.Screen()
    tela.title("Abelhinha - Fase 22")

def desenhar_mundo():
    celulas = [None] * (LINHAS * COLUNAS)
    for i, _ in enumerate(celulas):
        x, y = atores.xy(i)
        quadrado(x, y)
    turtle.update()

def laço_principal():
    turtle.update()
    turtle.ontimer(laço_principal, 500)

def adicionar_nuvens(posicoes):
    nuvens = []
    for posicao in posicoes:
        nuvem = atores.Nuvem(posicao)
        nuvem.atualize()
        nuvem.apareça()
        nuvens.append(nuvem)
    return nuvens

def adicionar_colmeias_aleatorias(posicoes):
    colmeias = []
    for posicao in posicoes:
        if random.choice([True, False]):
            colmeia = atores.Colméia(posicao, 1)
            colmeia.atualize()
            colmeia.apareça()
            colmeias.append(colmeia)
    return colmeias

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

# Posições das nuvens e possíveis colmeias
primeira_nuvem = pos_inicial_abelha + 2
segunda_nuvem = primeira_nuvem + 2 * COLUNAS
posicoes_nuvens = [primeira_nuvem, segunda_nuvem]

colmeias = adicionar_colmeias_aleatorias(posicoes_nuvens)
nuvens = adicionar_nuvens(posicoes_nuvens)

abelha = configurar_abelha(pos_inicial_abelha, atores.DIRECAO.LESTE)

turtle.update()

if importado():
    esconda_nuvens()

laço_principal()
