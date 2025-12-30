"""
Paint – Desenhe formas

Este jogo está parcialmente implementado.
Seu objetivo é compreender o funcionamento do código
e completar ou melhorar os trechos indicados com TODO,
para que fique funcionalmente semelhante ao jogo
presente no pacote freegames.

Depois, você deverá resolver os desafios propostos abaixo:

Desafios:
1. Adicionar uma nova cor.
2. Completar o desenho do círculo.
3. Completar o desenho do retângulo.
4. Completar o desenho do triângulo.
5. Adicionar um parâmetro de largura do traço.
"""

import turtle
from freegames import vector

# -------------------------------------------------
# Funções geométricas
# -------------------------------------------------
# Todas as funções de desenho seguem o MESMO CONTRATO:
# recebem dois pontos (inicio, fim).
# Isso permite trocar a forma dinamicamente usando o teclado.

def linha(inicio, fim):
    """Desenha uma linha do ponto inicial ao final."""
    turtle.up()
    turtle.goto(inicio.x, inicio.y)
    turtle.down()
    turtle.goto(fim.x, fim.y)
    # Ponto didático: a linha é a forma mais simples,
    # usada como referência para as demais.


def quadrado(inicio, fim):
    """Desenha um quadrado a partir de dois pontos."""
    turtle.up()
    turtle.goto(inicio.x, inicio.y)
    turtle.down()
    turtle.begin_fill()

    # Aqui o tamanho do lado é inferido apenas pelo eixo x.
    # Discussão pedagógica: limitações dessa escolha.
    for _ in range(4):
        turtle.forward(fim.x - inicio.x)
        turtle.left(90)

    turtle.end_fill()


def circulo(inicio, fim):
    """Desenha um círculo."""
    # TODO:
    # Identificar como calcular o raio a partir de dois pontos.
    # Ponto de intervenção: uso da função circle do turtle
    # ou cálculo manual.
    pass


def retangulo(inicio, fim):
    """Desenha um retângulo."""
    # TODO:
    # Diferenciar largura e altura.
    # Este exercício generaliza o quadrado.
    pass


def triangulo(inicio, fim):
    """Desenha um triângulo."""
    # TODO:
    # Planejar os vértices do triângulo.
    # Exige raciocínio geométrico explícito.
    pass


# -------------------------------------------------
# Interação com o mouse
# -------------------------------------------------
# O programa funciona com um protocolo de DOIS CLIQUES:
# 1º clique -> define o ponto inicial
# 2º clique -> desenha a forma escolhida

def clique(x, y):
    """Armazena o ponto inicial ou desenha a forma."""
    inicio = estado['inicio']

    if inicio is None:
        # Primeiro clique: apenas armazena o ponto
        estado['inicio'] = vector(x, y)
    else:
        # Segundo clique: executa a função da forma atual
        forma = estado['forma']
        fim = vector(x, y)
        forma(inicio, fim)
        estado['inicio'] = None


# -------------------------------------------------
# Estado global do programa
# -------------------------------------------------
# O dicionário estado centraliza:
# - o ponto inicial do desenho
# - a função que representa a forma atual
#
# Ponto-chave: funções são tratadas como DADOS.

def armazenar(chave, valor):
    """Armazena um valor no estado."""
    estado[chave] = valor


estado = {
    'inicio': None,
    'forma': linha
}


# -------------------------------------------------
# Configuração da janela e atalhos
# -------------------------------------------------

turtle.setup(420, 420, 370, 0)

turtle.onscreenclick(clique)
turtle.listen()

# Desfazer última ação
turtle.onkey(turtle.undo, 'u')

# Cores disponíveis
# Exercício: adicionar novas cores aqui
turtle.onkey(lambda: turtle.color('black'), 'K')
turtle.onkey(lambda: turtle.color('white'), 'W')
turtle.onkey(lambda: turtle.color('green'), 'G')
turtle.onkey(lambda: turtle.color('blue'), 'B')
turtle.onkey(lambda: turtle.color('red'), 'R')

# Seleção de formas
# Cada tecla altera qual função está armazenada em estado['forma']
turtle.onkey(lambda: armazenar('forma', linha), 'l')
turtle.onkey(lambda: armazenar('forma', quadrado), 's')
turtle.onkey(lambda: armazenar('forma', circulo), 'c')
turtle.onkey(lambda: armazenar('forma', retangulo), 'r')
turtle.onkey(lambda: armazenar('forma', triangulo), 't')

turtle.mainloop()
