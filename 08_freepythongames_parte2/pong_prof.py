"""
Pong — versão para estudo orientado (professor).

IDEIA CENTRAL:
Este jogo funciona como um micro-laboratório de programação
imperativa orientada a eventos e tempo.

PONTOS-CHAVE PARA OBSERVAÇÃO:
- O estado do jogo está concentrado nas variáveis `bola`,
    `direcao` e `estado`.
- Não existe um laço `while`: o tempo é controlado por ontimer().
- Colisões são tratadas com condicionais simples e geometria básica.
- Pequenas alterações numéricas produzem mudanças visíveis no jogo.

PONTOS DE INTERVENÇÃO:
- Função valor(): controle da velocidade inicial.
- Função desenhar(): lógica central do jogo (loop temporal).
- Retângulos das raquetes: tamanho, posição e colisão.
- ontimer(desenhar, 50): taxa de atualização.
"""

from random import choice, random
import turtle
from freegames import vector


def valor():
        """Gera um valor aleatório entre (-5, -3) ou (3, 5)."""
        return (3 + random() * 2) * choice([1, -1])


# Estado global do jogo
bola = vector(0, 0)                 # posição da bola
direcao = vector(valor(), valor())  # velocidade da bola
raquetes = {1: 0, 2: 0}             # posição vertical das raquetes


def mover(jogador, deslocamento):
    """Atualiza o estado da raquete de um jogador."""
    raquetes[jogador] += deslocamento


def raquete(x, y, largura, altura):
    """Abstração gráfica para desenhar raquetes."""
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(largura)
        turtle.left(90)
        turtle.forward(altura)
        turtle.left(90)
    turtle.end_fill()


def desenhar():
    """
    Função central do jogo.
    Executa repetidamente:
    - desenha o cenário
    - move a bola
    - detecta colisões
    - agenda a próxima atualização
    """
    turtle.clear()

    # Raquetes
    raquete(-200, raquetes[1], 10, 50)
    # TODO Criar a segunda raquete
    raquete(190, raquetes[2], 10, 50)


    # Movimento da bola
    bola.move(direcao)

    turtle.up()
    turtle.goto(bola.x, bola.y)
    turtle.dot(10)
    turtle.update()

    # Colisão com paredes superior e inferior
    if bola.y < -200 or bola.y > 200:
        direcao.y = -direcao.y

    # Colisão com raquete esquerda
    if bola.x < -185:
        if raquetes[1] <= bola.y <= raquetes[1] + 50:
            direcao.x = -direcao.x
        else:
            return  # fim do jogo

    # Colisão com raquete direita
    if bola.x > 185:
        if raquetes[2] <= bola.y <= raquetes[2] + 50:
            direcao.x = -direcao.x
        else:
            return

    # Controle do tempo (frame rate)
    turtle.ontimer(desenhar, 50)


# Configuração da janela e eventos
turtle.setup(420, 420, 370, 0)
turtle.hideturtle()
turtle.tracer(False)
turtle.listen()

turtle.onkey(lambda: mover(1, 20), 'w')
turtle.onkey(lambda: mover(1, -20), 's')
turtle.onkey(lambda: mover(2, 20), 'i')
turtle.onkey(lambda: mover(2, -20), 'k')

turtle.desenhar()

turtle.mainloop()
