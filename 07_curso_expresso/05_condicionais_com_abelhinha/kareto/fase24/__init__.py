import turtle
import random
from kareto import atores

LINHAS = 8
COLUNAS = 8
DIMENSAO = 50

# Posição inicial da abelha (exemplo: 12, virada para leste)
pos_inicial_abelha = 12

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
    tela.title("Abelhinha - Fase 24")

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

# Posições das nuvens formando um quadrado mais afastado
canto_superior_esquerdo = 12
canto_superior_direito = canto_superior_esquerdo + 3
canto_inferior_esquerdo = canto_superior_esquerdo + 3 * COLUNAS
canto_inferior_direito = canto_inferior_esquerdo + 3

posicoes_nuvens = [
    canto_superior_esquerdo,
    canto_superior_direito,
    canto_inferior_esquerdo,
    canto_inferior_direito
]

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

# Posição inicial da abelha em um dos cantos (exemplo: canto_superior_esquerdo)
abelha = configurar_abelha(canto_superior_esquerdo, atores.DIRECAO.LESTE)

turtle.update()

if importado():
    esconda_nuvens()

laço_principal()
