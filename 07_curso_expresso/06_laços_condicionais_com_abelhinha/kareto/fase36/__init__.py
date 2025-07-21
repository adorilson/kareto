import random
import sys
import turtle
from .. import atores
from ..atores import Abelha, tem_nectar_no_girassol, tem_caminho

LINHAS = 8
COLUNAS = 8
DIMENSAO = 50

# Abelha: última linha, segunda coluna (posição 57), direcionada para cima
pos_abelha = 57

# Colmeia 1: 4 casas acima (posição 25), 3 néctares
pos_colmeia1 = 25
# Girassol: 4 casas à direita da colmeia (posição 29), 3 néctares
pos_girassol = 29
# Colmeia 2: 2 casas abaixo do girassol (posição 45), 2 néctares
pos_colmeia2 = 45

# Caminho: abelha sobe até colmeia1, vai para direita até girassol, desce até colmeia2
# Preenche também a região entre eles
caminho_posicoes = [
    57, 49, 41, 33, 25, # sobe até colmeia1
    26, 27, 28, 29,     # vai para direita até girassol
    37, 45              # desce até colmeia2
]

# Adiciona casas intermediárias para preencher a região entre os atores
caminho_posicoes += [34, 35, 36, 44, 53, 61] # exemplo de preenchimento lateral/vertical

atores_lista = [
    ("colmeia", pos_colmeia1, 3),
    ("girassol", pos_girassol, 3),
    ("colmeia", pos_colmeia2, 2)
]

def configurar_janela():
    atores.configurar_janela()
    tela = turtle.Screen()
    tela.title("Abelhinha - Fase 36")

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
    abelha.vire_para(atores.DIRECAO.NORTE)
    abelha.caminho_posicoes = caminho_posicoes
    abelha.atualize()
    abelha.apareça()
    return abelha

configurar_janela()
desenhar_mundo()

for tipo, pos, nectar in atores_lista:
    if tipo == "colmeia":
        ator = atores.Colméia(pos, nectar)
    else:
        ator = atores.Girassol(pos, nectar)
    ator.atualize()
    ator.apareça()

abelha = configurar_abelha()
turtle.update()

def Abelha():
    return abelha

def tem_caminho():
    from ..atores import tem_caminho as tem_caminho_param
    return tem_caminho_param(caminho_posicoes)

def tem_nectar_no_girassol():
    from ..atores import tem_nectar_no_girassol as tng
    return tng()

def tem_nectar_na_colmeia():
    from ..atores import tem_mel_na_colmeia as tnc
    return tnc()
