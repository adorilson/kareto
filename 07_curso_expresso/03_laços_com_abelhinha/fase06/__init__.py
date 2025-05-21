import random
import turtle
import time

import atores

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


def configurar_janela(titulo):
    atores.configurar_janela()
    tela = turtle.Screen()
    tela.title(titulo)


def desenhar_mundo():
    """Desenhe o mundo (tabuleiro) com todos os quadrados."""
    celulas = [None] * (LINHAS * COLUNAS)

    for i, _ in enumerate(celulas):
        x, y = atores.xy(i)
        quadrado(x, y)

    turtle.update()


def verificar_flor():
    for girassol in girassois:
        if girassol.posicao == abelha.posicao:
            time.sleep(0.1)
            girassol.esconda()
            girassol.ativa = False


def laço_principal():
    turtle.update()
    verificar_flor()
    turtle.ontimer(laço_principal, 500)


# Atores desta fase
def adicionar_girassois(posições):
    girassóis = []
    for posição in posições:
        girassol = atores.Girassol()
        girassol.posicao = posição
        girassol.atualize()
        girassol.apareça()
        girassóis.append(girassol)
    return girassóis


def configurar_abelha(posição, direção):
    abelha = atores.Abelha()
    abelha.posicao = posição
    abelha.vire_para(direção)
    abelha.atualize()
    abelha.apareça()
    return abelha


configurar_janela("Abelhinha - Fase 6")
desenhar_mundo()

# É necessário que a abelha seja criada depois das flores, para ficar por cima
posições = 21, 22, 28, 35, 36, 42, 49, 50,
girassois = adicionar_girassois(posições)
abelha = configurar_abelha(posição=14, direção=atores.DIRECAO.SUL)


laço_principal()
time.sleep(0.3)
