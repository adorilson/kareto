import random
import time
import turtle

from .. import atores

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
    tela.title("Abelhinha - Fase 30")


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
def configurar_abelha(posição_inicial, direção_inicial):
    abelha = atores.Abelha()
    abelha.posição = posição_inicial
    abelha.vire_para(direção_inicial)
    abelha.atualize()
    abelha.apareça()
    return abelha


configurar_janela()
desenhar_mundo()

# Adiciona colmeias e girassóis em posições aleatórias, sem nuvens
qtd_colmeias = random.randint(1, 5)
qtd_girassois = random.randint(1, 5)

posicoes_disponiveis = list(range(1, LINHAS*COLUNAS+1))
posicoes_colmeias = random.sample(posicoes_disponiveis, k=min(qtd_colmeias, len(posicoes_disponiveis)))
posicoes_restantes = [p for p in posicoes_disponiveis if p not in posicoes_colmeias]
posicoes_girassois = random.sample(posicoes_restantes, k=min(qtd_girassois, len(posicoes_restantes)))

for pos in posicoes_colmeias:
    colmeia = atores.Colméia(pos, '?')
    colmeia.atualize()
    colmeia.apareça()

for pos in posicoes_girassois:
    girassol = atores.Girassol(pos, '?')
    girassol.atualize()
    girassol.apareça()

# Posição inicial da abelha aleatória
direcao_inicial_abelha = random.choice(tuple(atores.DIRECAO))
posicao_inicial_abelha = random.randint(1, LINHAS*COLUNAS)
abelha = configurar_abelha(posicao_inicial_abelha, direcao_inicial_abelha)

laço_principal()
time.sleep(0.3)
