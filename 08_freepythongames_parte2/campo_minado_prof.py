"""
Campo Minado

Este jogo está parcialmente implementado.
Seu objetivo é compreender o funcionamento do código
e completar ou melhorar os trechos indicados com TODO,
para que fique funcionalmente semelhante ao jogo
presente no pacote freegames.

Depois, você deverá resolver os desafios propostos abaixo:

1. O que faz a chamada da função seed(0)?
2. Como alterar a quantidade de bombas no tabuleiro?
3. Como alterar o tamanho do tabuleiro?
4. Como exibir a imagem de uma bomba no lugar do X?
5. Como evitar sobreposição de bombas?
6. Como permitir que o jogador configure o número de bombas?

Leia o código com atenção antes de começar.
"""

from random import randrange, seed
from turtle import *

from freegames import floor, square


"""NOTA
Definição de variáveis globais para controle de estado do jogo

Conceitos envolvidos
- uso de dicionários como estruturas de dados
- Tupla como chave de dicionário (chave composta): (x, y)
- Representação de estado do jogo
- Reprodutibilidade (seed)

Importante: o tabuleiro não é uma matriz explícita (lista de lista),
mas um mapeamento de coordenadas -> valores
"""

# Define uma semente fixa para que a posição das bombas
# seja sempre a mesma a cada execução do programa
seed(0)

# Indica se existe uma bomba em cada posição (x, y)
bombas = {}

# Indica se a célula (x, y) já foi revelada
revelado = {}

# Armazena a quantidade de bombas vizinhas de cada célula
contagens = {}


"""NOTA
Inicialização do tabuleiro

Conceitos envolvidos:
- laços aninhados
- inicialização de estruturas paralelas
- coordenadas discretas
"""
def inicializar():
    """
    Inicializa as estruturas do jogo:
    - bombas
    - revelado
    - contagens
    """

    """NOTA
    O tabuleiro é uma grade de quadrados de 50x50
        - Cada posição (x, y) recebe:
        - nenhuma bomba (False)
        - não revelada (False)
        - contagem ainda indefinida (-1)
    """
    # Cria todas as células do tabuleiro
    for x in range(-250, 250, 50):
        for y in range(-250, 250, 50):
            bombas[x, y] = False
            revelado[x, y] = False
            contagens[x, y] = -1

    """NOTA
    Posicionamento das bombas:
    - São colocadas 8 bombas
    - Cada bomba recebe uma posição aleatória válida
    - O valor associada àquela posição passa a ser True
    - Não há verificação de duplicidade (tarefa pra os alunos fazerem)
    """
    # Posiciona as bombas aleatoriamente
    for _ in range(8):
        x = randrange(-200, 200, 50)
        y = randrange(-200, 200, 50)
        bombas[x, y] = True

    """NOTA
    Contagem de bombas vizinhas;
    Para cada célula do tabuleiro:
    - percorre todas as 8 vizinhas + ela mesma
    - soma os valores booleanos (True == 1, False == 0)
    - armazena o total em contagens

    Conceitos fundamentais:
    - vizinhança
    - acumulação
    - uso implícito de booleanos como inteiros
    - laços aninhados triplos
    """
    # Calcula a quantidade de bombas vizinhas
    for x in range(-200, 200, 50):
        for y in range(-200, 200, 50):
            total = 0

            # Verifica a célula atual e as vizinhas
            for i in (-50, 0, 50):
                for j in (-50, 0, 50):
                    total += bombas[x + i, y + j]

            contagens[x, y] = total


# -------------------------------------------------
# Funções de desenho
# -------------------------------------------------

"""NOTA
Abstra o desenho de uma célula
Separa lógica de visualização
"""
def carimbar(x, y, texto):
    """
    Desenha uma célula branca na posição (x, y)
    e escreve um texto dentro dela.
    """
    square(x, y, 50, 'white')
    color('black')
    write(texto, font=('Arial', 50, 'normal'))


"""NOTA
Percorre todo o tabuleiro
Desenha cada célula com um ?
Representa casas não-reveladas
"""
def desenhar_tabuleiro():
    """
    Desenha o tabuleiro inicial, com todas as
    células marcadas como desconhecidas.
    """
    for x in range(-200, 200, 50):
        for y in range(-200, 200, 50):
            carimbar(x, y, "?")

"""NOTA
Percorre todo o tabuleiro
Onde houver bomba, desenha um X
Representa o fim do jogo

Conceitos:
Varredura completa
Condição simples
Visualização de estado
"""
def fim_de_jogo():
    """
    Revela todas as bombas do tabuleiro,
    marcando-as com a letra 'X'.
    """
    for x in range(-200, 200, 50):
        for y in range(-200, 200, 50):
            if bombas[x, y]:
                carimbar(x, y, 'X')


# -------------------------------------------------
# Interação com o jogador
# -------------------------------------------------

def clique(x, y):
    """
    Responde ao clique do mouse nas coordenadas (x, y).
    """

    # Ajusta as coordenadas do clique para a grade
    x = floor(x, 50)
    y = floor(y, 50)

    # Se o jogador clicou em uma bomba, o jogo termina
    if bombas[x, y]:
        fim_de_jogo()
        return

    # Lista de células que ainda precisam ser processadas
    pilha = [(x, y)]

    while pilha:
        x, y = pilha.pop()

        # Revela a célula atual
        carimbar(x, y, contagens[x, y])
        revelado[x, y] = True

        # Se não houver bombas vizinhas,
        # revela automaticamente as células ao redor
        if contagens[x, y] == 0:
            for i in (-50, 0, 50):
                for j in (-50, 0, 50):
                    vizinho = x + i, y + j

                    if not revelado[vizinho]:
                        pilha.append(vizinho)


# -------------------------------------------------
# Configuração da janela e início do jogo
# -------------------------------------------------

setup(420, 420, 370, 0)
hideturtle()
tracer(False)

inicializar()
desenhar_tabuleiro()

onscreenclick(clique)
mainloop()
