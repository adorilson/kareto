"""
Snake, jogo clássico de arcade.

Este jogo está parcialmente implementado.
Seu objetivo é compreender o funcionamento do código
e completar ou melhorar os trechos indicados com TODO,
para que fique funcionalmente semelhante ao jogo
presente no pacote freegames.

Depois, você deverá resolver os desafios propostos abaixo:

1. Como tornar a cobra mais rápida ou mais lenta?
2. Como fazer a cobra atravessar as bordas da tela?
3. Como fazer a comida se mover?
4. Alterar o jogo para que a cobra responda a cliques do mouse.
5. Exibir a pontuação na tela para o jogador, conforme a cobra come
as comidas.

Leia o código com atenção antes de começar.
"""

from random import randrange
from turtle import *

from freegames import square, vector


"""
Definição de variáveis globais para controle de estado do jogo

Conceitos envolvidos
- Variáveis globais
- Listas
- Representação de estado do jogo
- Vetores como abstração de posição
"""

# Posição inicial da comida
comida = vector(0, 0)

# A cobra é uma lista de segmentos (cada segmento é um vetor)
cobra = [vector(10, 0)]

# Direção atual do movimento
direcao = vector(0, -10)


"""NOTA
Função de mudança de direção

Conceitos
- Funções
- Parâmetros
- Modificação de estado global
- Relação entre entrada do usuário e comportamento do programa
"""

def mudar_direcao(x, y):
    """Altera a direção do movimento da cobra."""
    direcao.x = x
    direcao.y = y


"""NOTA
Função para verificação de limites da tela

Conceitos
- Expressões booleanas
- Operadores relacionais
- Retorno de função (True / False)
"""

def dentro_limites(cabeca):
    """Retorna True se a cabeça estiver dentro da área do jogo."""
    return -200 < cabeca.x < 190 and -200 < cabeca.y < 190

"""
Função principal de movimento
"""

def mover():
    """Move a cobra um segmento à frente."""

    # Aqui aparece uma ideia-chave:
    # a nova cabeça é criada a partir da última posição da cobra
    cabeca = cobra[-1].copy()
    cabeca.move(direcao)

    # Detecção de colisões
    """NOTA
    Conceitos:
    - Condicional composta
    - Operador lógico or
    - Teste de pertencimento (in)
    - Encerramento antecipado da função (return)
    """
    if not dentro_limites(cabeca) or cabeca in cobra:
        square(cabeca.x, cabeca.y, 9, 'red')
        update()
        return

    # Crescimento da cobra e lógica da comida
    """NOTA
    Conceitos
    - Estrutura if / else
    - Manipulação de listas (append / pop)
    - Aleatoriedade
    - Crescimento condicionado a eventos
    """
    cobra.append(cabeca)

    if cabeca == comida:
        print('Tamanho da cobra:', len(cobra))
        comida.x = randrange(-15, 15) * 10
        comida.y = randrange(-15, 15) * 10
    else:
        cobra.pop(0)

    #Desenho do jogo
    """NOTA
    Conceitos
    Laço for
    Atualização gráfica
    Programação orientada a eventos temporais (ontimer)
    """
    clear()

    for segmento in cobra:
        square(segmento.x, segmento.y, 9, 'black')

    square(comida.x, comida.y, 9, 'green')
    update()
    ontimer(mover, 100)

# Configuração da tela e eventos
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: mudar_direcao(10, 0), 'Right')
onkey(lambda: mudar_direcao(-10, 0), 'Left')
onkey(lambda: mudar_direcao(0, 10), 'Up')
onkey(lambda: mudar_direcao(0, -10), 'Down')

# Chamada inicial de mover
mover()

mainloop()
