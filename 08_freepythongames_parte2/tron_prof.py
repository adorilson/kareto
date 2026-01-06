"""Tron, jogo clássico de arcade.

Este jogo está parcialmente implementado.
Seu objetivo é compreender o funcionamento do código
e completar ou melhorar os trechos indicados com TODO,
para que fique funcionalmente semelhante ao jogo
presente no pacote freegames.

Depois, você deverá resolver os desafios propostos abaixo:

Exercícios

1. Tornar os jogadores mais rápidos ou mais lentos.
2. Impedir que um jogador colida com o próprio rastro.
3. Permitir que o jogador atravesse as bordas da tela.
4. Como criar um jogador controlado pelo computador?
5. Tornar as mensagens de vitória mais visuais.
"""

import turtle
from freegames import square, vector

# Cada jogador é definido por:
# - uma posição (vector)
# - uma direção de movimento (vector)
# - um conjunto com todas as posições já ocupadas (rastro)
j1_pos = vector(-100, 0)
j1_dir = vector(4, 0)
j1_rastro = set()

j2_pos = vector(100, 0)
j2_dir = vector(-4, 0)
j2_rastro = set()


def dentro_da_tela(cabeca):
    """
    Função de validação espacial.
    Central para o controle de colisão com as bordas.
    """
    return -200 < cabeca.x < 200 and -200 < cabeca.y < 200


def desenhar():
    """
    Laço principal do jogo.
    Executa movimento, verifica colisões,
    desenha os rastros e agenda a próxima atualização.
    """
    j1_pos.move(j1_dir)
    cabeca1 = j1_pos.copy()

    j2_pos.move(j2_dir)
    cabeca2 = j2_pos.copy()

    if not dentro_da_tela(cabeca1) or cabeca1 in j2_rastro:
        print('Jogador azul venceu!')
        return

    if not dentro_da_tela(cabeca2) or cabeca2 in j1_rastro:
        print('Jogador vermelho venceu!')
        return

    # Armazenamento do rastro como conjunto (set)
    j1_rastro.add(cabeca1)
    j2_rastro.add(cabeca2)

    # TODO : Desenhar os jogadores com cores diferentes
    square(j1_pos.x, j1_pos.y, 3, 'red') 
    square(j2_pos.x, j2_pos.y, 3, 'blue')
    turtle.update()

    # Controle da velocidade do jogo (Ex. 1)
    turtle.ontimer(desenhar, 50)


# Configuração da janela e eventos
turtle.setup(420, 420, 370, 0)
turtle.hideturtle()
turtle.tracer(False)
turtle.listen()

# Eventos de rotação da direção
turtle.onkey(lambda: j1_dir.rotate(90), 'a')
turtle.onkey(lambda: j1_dir.rotate(-90), 'd')

# TODO : configurar as teclas do jogador 2
turtle.onkey(lambda: j2_dir.rotate(90), 'j')
turtle.onkey(lambda: j2_dir.rotate(-90), 'l')

desenhar()
turtle.mainloop()
