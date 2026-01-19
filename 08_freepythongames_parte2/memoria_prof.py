"""Memória, jogo de quebra-cabeça de pares.

VERSÃO DO PROFESSOR

Este jogo trabalha fortemente:
- listas e indexação
- dicionários como estrutura de estado
- mapeamento entre coordenadas gráficas e dados
- eventos (cliques do mouse)
- laço de atualização com ontimer
"""

import turtle
from random import shuffle


from freegames import path

# Caminho para a imagem de fundo
carro = path('car.gif')

# Lista de peças: números de 0 a 31 duplicados (pares)
# O shuffle garante a aleatoriedade do tabuleiro
pecas = list(range(32)) * 2

# Dicionário usado para manter o estado do jogo
# 'marca' guarda a posição da primeira peça clicada
estado = {'marca': None}

# Lista de booleanos que indica se cada peça está escondida
# True  -> peça escondida
# False -> peça revelada
escondido = [True] * 64


"""
Cada quadrado representa uma peça ainda não revelada.
O tamanho fixo (50x50) define implicitamente o grid do jogo.
"""
def quadrado(x, y):
    """Desenha um quadrado branco com contorno preto em (x, y)."""
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.color('black', 'white')
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(50)
        turtle.left(90)
    turtle.end_fill()


"""
Esta função é crucial: ela faz o mapeamento entre
o espaço gráfico (clique do mouse) e a estrutura de dados (lista).
"""
def indice(x, y):
    """Converte coordenadas (x, y) no índice da peça."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


"""
É o processo inverso da função indice().
Permite desenhar uma peça sabendo apenas sua posição na lista.
"""
def coordenadas(contador):
    """Converte o índice da peça em coordenadas (x, y)."""
    return (contador % 8) * 50 - 200, (contador // 8) * 50 - 200


"""
Lógica do jogo:
- Primeiro clique: apenas marca a peça
- Segundo clique:
    - Se for a mesma peça ou não formar par, apenas atualiza a marca
    - Se formar par, revela as duas peças
"""
def toque(x, y):
    """Atualiza a marcação e as peças escondidas com base no clique."""
    posicao = indice(x, y)
    marca = estado['marca']

    # Caso 1: nenhuma peça marcada ainda
    # Caso 2: clique na mesma peça
    # Caso 3: peças diferentes (não formam par)
    if marca is None or marca == posicao or pecas[marca] != pecas[posicao]:
        estado['marca'] = posicao
    else:
        # Par encontrado: revela ambas as peças
        escondido[posicao] = False
        escondido[marca] = False
        estado['marca'] = None


"""
Esta função é chamada repetidamente via ontimer,
funcionando como o 'loop principal' do jogo.
"""
def desenhar():
    """Desenha o estado atual do jogo."""
    turtle.clear()

    # Desenha a imagem de fundo
    turtle.goto(0, 0)
    turtle.shape(carro)
    turtle.stamp()

    # Desenha todas as peças ainda escondidas
    for contador in range(64):
        if escondido[contador]:
            x, y = coordenadas(contador)
            quadrado(x, y)

    # Se houver uma peça marcada, mostra seu valor
    marca = estado['marca']

    if marca is not None and escondido[marca]:
        x, y = coordenadas(marca)
        turtle.up()
        turtle.goto(x + 2, y)
        turtle.color('black')
        turtle.write(pecas[marca], font=('Arial', 30, 'normal'))

    turtle.update()

    # Agenda a próxima atualização da tela
    turtle.ontimer(desenhar, 100)


# Embaralha as peças antes de iniciar o jogo
shuffle(pecas)

# Configuração da janela
turtle.setup(420, 420, 370, 0)
turtle.addshape(carro)
turtle.hideturtle()
turtle.tracer(False)

# Associa o clique do mouse à função toque
turtle.onscreenclick(toque)

# Inicia o jogo
desenhar()
turtle.mainloop()
