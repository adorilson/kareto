import turtle
from kareto import atores
import random

LINHAS = 8
COLUNAS = 8
DIMENSAO = 50

def quadrado(x, y):
    """Desenhe um quadrado na posição (x, y)."""
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
    tela.title("Abelhinha - Fase 21")

def desenhar_mundo():
    celulas = [None] * (LINHAS * COLUNAS)
    for i, _ in enumerate(celulas):
        x, y = atores.xy(i)
        quadrado(x, y)
    turtle.update()

def laço_principal():
    turtle.update()
    turtle.ontimer(laço_principal, 500)

def adicionar_girassois(posicoes):
    girassois = []
    for posicao in posicoes:
        girassol = atores.Girassol(posicao, 1)
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

def Abelha():
    return abelha

configurar_janela()
desenhar_mundo()

# Posições dos girassóis
posicoes_girassois = [25, 28, 30, 31]
girassois = adicionar_girassois(posicoes_girassois)

# Posição inicial da abelha
abelha = configurar_abelha(24, atores.DIRECAO.LESTE)

laço_principal()
