import random
import turtle
import sys
from .. import atores
from ..atores import Abelha, tem_mel_na_colmeia

LINHAS = 8
COLUNAS = 8
DIMENSAO = 50

def Abelha():
    return abelha

def configurar_janela():
    atores.configurar_janela()
    tela = turtle.Screen()
    tela.title("Abelhinha - Fase 32")

def desenhar_mundo():
    tons_de_verde = ["green", "darkgreen", "forestgreen", "seagreen"]
    for i in range(LINHAS * COLUNAS):
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


def configurar_abelha():
    abelha = atores.Abelha()
    abelha.posição = 18  # linha 2, coluna 2 (mais acima)
    abelha.vire_para(atores.DIRECAO.LESTE)
    abelha.atualize()
    abelha.apareça()
    return abelha


def importado():
    return sys.argv[0] != '-m'


def nectar_aleatorio():
    if importado():
        return random.randint(1, 9)
    return '?'


configurar_janela()
desenhar_mundo()

# Posições das colmeias: alternando direita e baixo, terminando com o último abaixo do penúltimo
posicoes = [19, 27, 28, 36, 37, 45]
nectares = [2, 3, 1, 4, 2, nectar_aleatorio()]
for pos, nectar in zip(posicoes, nectares):
    colmeia = atores.Colméia(pos, nectar)
    colmeia.atualize()
    colmeia.apareça()

abelha = configurar_abelha()
turtle.update()
