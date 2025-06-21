import random
import turtle
import time

import atores

LINHAS = 8
COLUNAS = 8
DIMENSAO = 50
TITULO_JANELA = "Abelhinha - Fase 18"


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
    tela.title(TITULO_JANELA)


def desenhar_mundo():
    """Desenhe o mundo (tabuleiro) com todos os quadrados."""
    celulas = [None] * (LINHAS * COLUNAS)

    for i, _ in enumerate(celulas):
        x, y = atores.xy(i)
        quadrado(x, y)

    turtle.update()

def laço_principal():
    turtle.update()
    turtle.ontimer(laço_principal, 500)


# Atores desta fase
def adicionar_girassois(posições):
    girassóis = []
    for posição, nectar in posições:
        girassol = atores.Girassol(posição=posição, nectar=nectar)
        girassol.atualize()
        girassol.apareça()
        girassóis.append(girassol)
    return girassóis


def adicionar_colméias(posições):
    colméias = []
    for posição, nectar in posições:
        colméia = atores.Colméia(posição=posição, nectar=nectar)
        colméia.atualize()
        colméia.apareça()
        colméias.append(colméia)
    return colméias


def configurar_abelha(posição_inicial, direção_inicial):
    abelha = atores.Abelha()
    abelha.posição = posição_inicial
    abelha.vire_para(direção_inicial)
    abelha.atualize()
    abelha.apareça()
    return abelha


configurar_janela()
desenhar_mundo()



posicao_inicial_abelha = 7
direcao_inicial_abelha = atores.DIRECAO.OESTE

nectar = 1
# as somas estão à mostra porque fiquei com preguiça de contar
posicoes_colmeias = [(5, nectar), (6, nectar),
                     (13, nectar), 
                     (19, nectar), (20, nectar), (21, nectar), 
                     (19+8, nectar),
                     (19+14, nectar), (19+15, nectar), (19+16, nectar),
                     (17+24, nectar),
                     (17+32, nectar),
                     ]

# É necessário que a abelha seja criada depois das flores, para ficar por cima
colmeias = adicionar_colméias(posicoes_colmeias)
abelha = configurar_abelha(posicao_inicial_abelha, direcao_inicial_abelha)

laço_principal()
time.sleep(0.3) 