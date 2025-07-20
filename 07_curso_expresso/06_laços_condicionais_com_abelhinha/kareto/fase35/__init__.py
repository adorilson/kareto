import random
import sys
import turtle
from .. import atores
from ..atores import Abelha, tem_nectar_no_girassol, tem_caminho

LINHAS = 8
COLUNAS = 8
DIMENSAO = 50

def importado():
    return sys.argv[0] != '-m'


def nectar_aleatorio():
    if importado():
        return random.randint(1, 9)
    return '?'

# Posições dos girassóis e néctar
# Abelha: última linha, primeira coluna => posição 56
# Girassol 1: duas casas à frente => posição 58 (1 néctar)
# Girassol 2: sobe duas casas, depois duas à direita => posição 44 (aleatório)
# Girassol 3: última coluna, linha 4 => posição 31
# Caminho ajustado: termina em 31 (girassol3), 23 (uma casa acima)

pos_abelha = 56
pos_girassol1 = 58
pos_girassol2 = 44
pos_girassol3 = 31

# Caminho: dois L invertidos, cada lado com 3 casas
# Primeiro L: 56 (abelha), 57, 58 (girassol1), 50, 42, 43, 44 (girassol2)
# Após o segundo girassol (44), o caminho segue para cima: 36, 28
# E ao lado dele: 29 (à direita de 28)
# Depois segue para a esquerda do terceiro girassol: 30
# Depois para o terceiro girassol: 31 (girassol3)
# Casa final acima: 23
caminho_posicoes = [56, 57, 58, 50, 42, 43, 44, 36, 28, 29, 30, 31, 23]


girassois = [
    (pos_girassol1, 1),
    (pos_girassol2, nectar_aleatorio()),
    (pos_girassol3, 3),
]

def Abelha():
    return abelha

def configurar_janela():
    atores.configurar_janela()
    tela = turtle.Screen()
    tela.title("Abelhinha - Fase 35")

def desenhar_mundo():
    tons_de_verde = ["green", "darkgreen", "forestgreen", "seagreen"]
    for i in range(LINHAS * COLUNAS):
        x, y = atores.xy(i)
        turtle.up()
        turtle.goto(x, y)
        turtle.down()
        if i in caminho_posicoes:
            turtle.pencolor("#1E90FF")  # azul forte
            turtle.fillcolor("#87CEFA") # azul claro
        else:
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
    abelha.posição = pos_abelha
    abelha.vire_para(atores.DIRECAO.LESTE)
    abelha.caminho_posicoes = caminho_posicoes
    abelha.atualize()
    abelha.apareça()
    return abelha

configurar_janela()
desenhar_mundo()

for pos, nectar in girassois:
    girassol = atores.Girassol(pos, nectar)
    girassol.atualize()
    girassol.apareça()

abelha = configurar_abelha()
turtle.update()

def tem_caminho():
    from ..atores import tem_caminho as tem_caminho_param
    return tem_caminho_param(caminho_posicoes)
