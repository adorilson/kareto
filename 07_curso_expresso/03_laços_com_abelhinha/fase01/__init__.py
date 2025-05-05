import random
import turtle
import time

from atores import atores

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
    tela.title("Abelhinha - Fase 1")


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
def adicionar_girassois():
    girassol1 = atores.Girassol()
    girassol1.posicao = 35

    girassol2 = atores.Girassol()
    girassol2.posicao = 37
    
    girassol3 = atores.Girassol()
    girassol3.posicao = 38

    girassois = girassol1, girassol2, girassol3

    for girassol in girassois:
        girassol.atualize()
        girassol.apareça()

    return girassois


def configurar_abelha():
    abelha = atores.Abelha()
    abelha.posicao = 33
    abelha.atualize()
    abelha.apareça()
    return abelha


configurar_janela()
desenhar_mundo()

# É necessário que a abelha seja criada depois das flores, para ficar por cima
girassois = adicionar_girassois()
abelha = configurar_abelha()

laço_principal()
time.sleep(0.3)
