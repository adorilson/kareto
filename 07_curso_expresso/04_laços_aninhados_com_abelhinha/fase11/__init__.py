import random
import time
import turtle

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


def configurar_janela():
    atores.configurar_janela()
    tela = turtle.Screen()
    tela.title("Abelhinha - Fase 11")


def desenhar_mundo():
    """Desenhe o mundo (tabuleiro) com todos os quadrados."""
    celulas = [None] * (LINHAS * COLUNAS)

    for i, _ in enumerate(celulas):
        x, y = atores.xy(i)
        quadrado(x, y)

    turtle.update()


def verificar_flor():
    for girassol in girassois:
        if girassol.posição == abelha.posicao:
            time.sleep(0.1)
            girassol.esconda()
            girassol.ativa = False


def laço_principal():
    turtle.update()
    turtle.ontimer(laço_principal, 500)


# Atores desta fase
def adicionar_girassois(posições):
    girassóis = []
    for posição_atual, néctar in posições:
        girassol = atores.Girassol(posição_atual, néctar)
        girassol.atualize()
        girassol.apareça()
        girassóis.append(girassol)
    return girassóis


def configurar_abelha(posição_inicial, direção_inicial):
    abelha = atores.Abelha()
    abelha.posição = posição_inicial
    abelha.vire_para(direção_inicial)
    abelha.atualize()
    abelha.apareça()
    return abelha


configurar_janela()
desenhar_mundo()

qtd = random.randint(1, 10)
posicoes_girassois = random.choices(range(1, LINHAS*COLUNAS), k=qtd)
posicao_inicial_abelha = random.randint(1, LINHAS*COLUNAS)
direcao_inicial_abelha = random.choice(tuple(atores.DIRECAO))

# É necessário que a abelha seja criada depois das flores, para ficar por cima
girassois = adicionar_girassois([(posição, random.randint(1, 9)) for posição in posicoes_girassois])
abelha = configurar_abelha(posicao_inicial_abelha, direcao_inicial_abelha)

laço_principal()
time.sleep(0.3)
