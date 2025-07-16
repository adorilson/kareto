import random
import turtle
from .. import atores
from ..atores import Abelha, tem_mel_na_colmeia, tem_caminho

LINHAS = 8
COLUNAS = 8
DIMENSAO = 50

def Abelha():
    return abelha

def configurar_janela():
    atores.configurar_janela()
    tela = turtle.Screen()
    tela.title("Abelhinha - Fase 33")

def desenhar_mundo():
    tons_de_verde = ["green", "darkgreen", "forestgreen", "seagreen"]
    caminho = [48, 49, 50, 51, 52, 53, 54, 55, 47, 39, 31, 23, 15, 14, 13, 12, 11, 10, 9, 17, 25]
    for i in range(LINHAS * COLUNAS):
        x, y = atores.xy(i)
        turtle.up()
        turtle.goto(x, y)
        turtle.down()
        if i in caminho:
            turtle.pencolor("#1E90FF")  # azul forte para contraste
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
    abelha.posição = 48  # antepenúltima linha, primeira coluna (linha 6, coluna 0)
    abelha.vire_para(atores.DIRECAO.LESTE)
    abelha.atualize()
    abelha.apareça()
    return abelha

def tem_caminho():
    caminho_posicoes = [48, 49, 50, 51, 52, 53, 54, 55, 47, 39, 31, 23, 15, 14, 13, 12, 11, 10, 9, 17, 25]
    from ..atores import tem_caminho as tem_caminho_param
    return tem_caminho_param(caminho_posicoes)

configurar_janela()
desenhar_mundo()

# Colmeias conforme descrição do usuário
colmeias = [
    (55, 1),  # mesma linha da abelha, última coluna (linha 6, coluna 7)
    (15, 1),  # mesma coluna da colmeia anterior, segunda linha (linha 1, coluna 7)
    (9, 1),   # mesma linha da anterior, segunda coluna (linha 1, coluna 1)
    (25, 1),  # mesma coluna da anterior, duas linhas abaixo (linha 3, coluna 1)
]
for pos, nectar in colmeias:
    colmeia = atores.Colméia(pos, nectar)
    colmeia.atualize()
    colmeia.apareça()

abelha = configurar_abelha()
abelha.caminho_posicoes = [48, 49, 50, 51, 52, 53, 54, 55, 47, 39, 31, 23, 15, 14, 13, 12, 11, 10, 9, 17, 25]
turtle.update()
