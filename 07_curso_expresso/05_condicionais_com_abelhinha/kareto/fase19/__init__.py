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
    tela.title("Abelhinha - Fase 19")


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
def adicionar_nuvens(posicoes):
    nuvens = []
    for posicao in posicoes:
        nuvem = atores.Nuvem(posicao)
        nuvem.atualize()
        nuvem.apareça()
        nuvens.append(nuvem)
    return nuvens


def configurar_abelha(posição_inicial, direção_inicial):
    abelha = atores.Abelha()
    abelha.posição = posição_inicial
    abelha.vire_para(direção_inicial)
    abelha.atualize()
    abelha.apareça()
    return abelha


configurar_janela()
desenhar_mundo()

# Adiciona uma colmeia e uma nuvem na mesma posição
posicao_sobreposta_colmeia = random.randint(1, LINHAS*COLUNAS)

sobreposta_colmeia = atores.Colméia(posicao_sobreposta_colmeia, random.randint(1, 9))
sobreposta_colmeia.atualize()
sobreposta_colmeia.apareça()

sobreposta_nuvem_colmeia = atores.Nuvem(posicao_sobreposta_colmeia)
sobreposta_nuvem_colmeia.atualize()
sobreposta_nuvem_colmeia.apareça()

# Adiciona um girassol e uma nuvem em outra posição
while True:
    posicao_sobreposta_girassol = random.randint(1, LINHAS*COLUNAS)
    if posicao_sobreposta_girassol != posicao_sobreposta_colmeia:
        break

sobreposto_girassol = atores.Girassol(posicao_sobreposta_girassol, random.randint(1, 9))
sobreposto_girassol.atualize()
sobreposto_girassol.apareça()

sobreposta_nuvem_girassol = atores.Nuvem(posicao_sobreposta_girassol)
sobreposta_nuvem_girassol.atualize()
sobreposta_nuvem_girassol.apareça()

# Gera as demais nuvens normalmente, evitando as duas posições sobrepostas
demais_nuvens = [i for i in range(1, LINHAS*COLUNAS) if i not in (posicao_sobreposta_colmeia, posicao_sobreposta_girassol)]
qtd_nuvens = random.randint(1, 10)
posicoes_nuvens = random.sample(demais_nuvens, k=min(qtd_nuvens, len(demais_nuvens)))
nuvens = adicionar_nuvens(posicoes_nuvens)

posicao_inicial_abelha = random.randint(1, LINHAS*COLUNAS)
direcao_inicial_abelha = random.choice(tuple(atores.DIRECAO))

abelha = configurar_abelha(posicao_inicial_abelha, direcao_inicial_abelha)

laço_principal()
time.sleep(0.3)
