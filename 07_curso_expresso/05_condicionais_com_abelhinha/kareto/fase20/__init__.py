import random
import sys
import time
import turtle
from kareto import atores

LINHAS = 8
COLUNAS = 8
DIMENSAO = 50

def Abelha():
    return abelha

def quadrado(x, y):
    """Desenhe um quadrado na posição (x, y)."""
    tons_de_verde = "green", "darkgreen", "forestgreen", "seagreen"
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.pencolor("lightgreen")
    turtle.begin_fill()
    for _ in range(4):
        turtle.fillcolor(random.choice(tons_de_verde))
        turtle.forward(DIMENSAO)
        turtle.right(90)
    turtle.end_fill()


def configurar_janela():
    atores.configurar_janela()
    tela = turtle.Screen()
    tela.title("Abelhinha - Fase 20")


def desenhar_mundo():
    """Desenhe o mundo (tabuleiro) com todos os quadrados."""
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


def adicionar_girassois_abaixo_nuvens(posicoes_nuvens):
    girassois = []
    for posicao_nuvem in posicoes_nuvens:
        posicao_girassol = posicao_nuvem
        if posicao_girassol < LINHAS * COLUNAS and random.choice([True, False]):
            girassol = atores.Girassol(posicao_girassol, 1)
            girassol.atualize()
            girassol.apareça()
            girassois.append(girassol)
    return girassois


def configurar_abelha(posicao, direcao):
    abelha = atores.Abelha()
    abelha.posição = posicao
    abelha.vire_para(direcao)
    abelha.atualize()
    abelha.apareça()
    return abelha


configurar_janela()
desenhar_mundo()

# Posições das nuvens
posicoes_nuvens = [28+8, 28+16]

# Adiciona girassóis aleatoriamente abaixo das nuvens
girassois = adicionar_girassois_abaixo_nuvens(posicoes_nuvens)

# Adiciona nuvens
nuvens = adicionar_nuvens(posicoes_nuvens)

# Posição inicial da abelha
abelha = configurar_abelha(26, atores.DIRECAO.LESTE)

turtle.update()


def esconda_nuvens():
    import time
    time.sleep(1)

    for nuvem in nuvens:
        nuvem.esconda()

    turtle.update()


def importado():
    return sys.argv[0] != '-m'


if importado():
    esconda_nuvens()

laço_principal()
