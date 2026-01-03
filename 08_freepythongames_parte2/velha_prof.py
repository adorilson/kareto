"""
Jogo da Velha

Este jogo está parcialmente implementado.
Seu objetivo é compreender o funcionamento do código
e completar ou melhorar os trechos indicados com TODO,
para que fique funcionalmente semelhante ao jogo
presente no pacote freegames.

Depois, você deverá resolver os desafios propostos abaixo.

Exercícios

1. Dar cores e espessuras diferentes para X e O.
2. Tratar o clique em uma casa já ocupada.
3. Detectar quando um jogador venceu.
4. Criar um jogador computador.
"""

import turtle
from freegames import line


# --------------------------------------------------
# DESENHO DO TABULEIRO
# --------------------------------------------------
def desenhar_grade():
    """Desenha a grade do jogo da velha.

    Leitura orientada:
    - O tabuleiro é fixo, desenhado diretamente na tela.
    - Não existe ainda uma estrutura de dados representando as casas.
    - As coordenadas foram calculadas manualmente.
    """
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


# --------------------------------------------------
# DESENHO DOS JOGADORES
# --------------------------------------------------
def desenhar_x(x, y):
    """Desenha o símbolo X.

    Leitura orientada:
    - O X é composto por duas linhas diagonais.
    - O tamanho do símbolo está embutido nos valores constantes (133).
    - O Exercício 1 propõe alterar cor e espessura aqui.
    """
    line(x, y, x + 133, y + 133)
    line(x, y + 133, x + 133, y)


def desenhar_o(x, y):
    """Desenha o símbolo O.

    Leitura orientada:
    - O O é desenhado usando turtle.circle.
    - O deslocamento em y melhora o alinhamento visual.
    - O Exercício 1 também atua neste ponto.
    """
    turtle.up()
    turtle.goto(x + 67, y + 5)
    turtle.down()
    turtle.circle(62)


# --------------------------------------------------
# CÁLCULO DA CÉLULA
# --------------------------------------------------
def ajustar_para_celula(valor):
    """Ajusta um valor para a célula correspondente do tabuleiro.

    Leitura orientada:
    - Converte uma coordenada qualquer do clique
      no canto inferior esquerdo da célula.
    - Esta função é essencial para mapear o mouse à grade.
    """
    return ((valor + 200) // 133) * 133 - 200


# --------------------------------------------------
# ESTADO DO JOGO
# --------------------------------------------------
estado = {'jogador': 0}

# Lista de funções de desenho:
# índice 0 → jogador X
# índice 1 → jogador O
jogadores = [desenhar_x, desenhar_o]

# Leitura orientada:
# - Não há controle das casas ocupadas.
# - Isso permite sobrescrever jogadas.
# - Exercícios 2 e 3 exigem introduzir esse controle.


# --------------------------------------------------
# TRATAMENTO DO CLIQUE
# --------------------------------------------------
def ao_clicar(x, y):
    """Desenha X ou O na célula clicada.

    Leitura orientada:
    - Identifica o jogador atual a partir do estado.
    - Seleciona dinamicamente a função de desenho.
    - Alterna o jogador ao final da jogada.
    - Não há validação de jogada (Exercício 2).
    """
    x = ajustar_para_celula(x)
    y = ajustar_para_celula(y)

    jogador = estado['jogador']
    desenhar = jogadores[jogador]

    desenhar(x, y)
    turtle.update()

    # TODO
    # Finalizar o controle de estado definir o próximo jogador
    estado['jogador'] = not jogador


# --------------------------------------------------
# CONFIGURAÇÃO DA JANELA
# --------------------------------------------------
turtle.setup(420, 420, 370, 0)
turtle.hideturtle()
turtle.tracer(False)

desenhar_grade()
turtle.update()

turtle.onscreenclick(ao_clicar)

turtle.mainloop()
