import turtle
import random
from kareto import atores

LINHAS = 8
COLUNAS = 8
DIMENSAO = 50

# Posição inicial da abelha (exemplo: 27, virada para norte)
pos_inicial_abelha = 27

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
    tela.title("Abelhinha - Fase 23")

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

def adicionar_colmeias_ou_girassois_aleatorios(posicoes):
    elementos = []
    for posicao in posicoes:
        if random.choice([True, False]):
            colmeia = atores.Colméia(posicao, 1)
            colmeia.atualize()
            colmeia.apareça()
            elementos.append(colmeia)
        else:
            girassol = atores.Girassol(posicao, 1)
            girassol.atualize()
            girassol.apareça()
            elementos.append(girassol)
    return elementos

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

# Posição da nuvem e do elemento oculto
pos_nuvem = pos_inicial_abelha - 2 * COLUNAS

# Adiciona aleatoriamente uma colmeia ou um girassol sob a nuvem
if random.choice([True, False]):
    elemento = atores.Colméia(pos_nuvem, 1)
    elemento.atualize()
    elemento.apareça()
else:
    elemento = atores.Girassol(pos_nuvem, 1)
    elemento.atualize()
    elemento.apareça()

nuvens = adicionar_nuvens([pos_nuvem])

abelha = configurar_abelha(pos_inicial_abelha, atores.DIRECAO.NORTE)

turtle.update()

if importado():
    esconda_nuvens()

laço_principal()
