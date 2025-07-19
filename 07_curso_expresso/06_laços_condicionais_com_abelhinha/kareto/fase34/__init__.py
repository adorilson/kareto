import random
import sys
import turtle
from .. import atores
from ..atores import Abelha, tem_mel_na_colmeia, tem_caminho

LINHAS = 8
COLUNAS = 8
DIMENSAO = 50


def importado():
    return sys.argv[0] != '-m'


def nectar_aleatorio():
    if importado():
        return random.randint(1, 9)
    return '?'

colmeias = [
    (37, nectar_aleatorio()),  # à frente da abelha
    (53, 1),                   # duas casas abaixo
    (50, nectar_aleatorio()),  # três casas à esquerda
    (18, 2),                   # subindo 4 casas
    (23, nectar_aleatorio()),  # última coluna, linha 2
    (63, 1),                   # última coluna, última linha
]

caminho_posicoes = [36, 37, 45, 53, 52, 51, 50, 42, 34, 26, 18, 19, 20, 21, 22, 23, 31, 39, 47, 55, 63]


def Abelha():
    return abelha


def configurar_janela():
    atores.configurar_janela()
    tela = turtle.Screen()
    tela.title("Abelhinha - Fase 34")


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
    abelha.posição = 36  # centro do mapa
    abelha.vire_para(atores.DIRECAO.LESTE)
    abelha.caminho_posicoes = caminho_posicoes
    abelha.atualize()
    abelha.apareça()
    return abelha


def tem_caminho():
    from ..atores import tem_caminho as tem_caminho_param
    return tem_caminho_param(caminho_posicoes)


configurar_janela()
desenhar_mundo()

for pos, nectar in colmeias:
    colmeia = atores.Colméia(pos, nectar)
    colmeia.atualize()
    colmeia.apareça()

abelha = configurar_abelha()
turtle.update()
