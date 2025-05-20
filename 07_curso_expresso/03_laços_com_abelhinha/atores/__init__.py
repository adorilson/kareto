import os
import time
import turtle
from enum import IntEnum


def caminho(nome_arquivo):
    """Retornar o caminho completo para `nome_arquivo`."""
    caminho = os.path.realpath(__file__)
    diretorio = os.path.dirname(caminho)
    caminho_completo = os.path.join(diretorio, nome_arquivo)
    return caminho_completo


ABELHA_LESTE = caminho("abelha_leste.gif")
ABELHA_NORTE = caminho("abelha_norte.gif")
ABELHA_OESTE = caminho("abelha_oeste.gif")
ABELHA_SUL = caminho("abelha_sul.gif")

GIRASSOL = caminho("girassol.gif")

turtle.register_shape(ABELHA_LESTE)
turtle.register_shape(ABELHA_OESTE)
turtle.register_shape(ABELHA_NORTE)
turtle.register_shape(ABELHA_SUL)
turtle.register_shape(GIRASSOL)


def configurar_janela():
    tela = turtle.Screen()
    tela.setup(420, 420)
    tela.cv._rootwindow.resizable(False, False)
    tela.title("Abelhinha")  # Pode ser atualizado a cada fase

    turtle.hideturtle()
    turtle.tracer(False)


def xy(celula, centralizar=False):
    """Converte um número de célula para coordenadas (x, y),
    com origem no canto superior esquerdo."""
    return ((celula % 8) * 50 - 200 + centralizar * 25), (
        200 - (celula // 8) * 50 - centralizar * 25
    )


class DIRECAO(IntEnum):
    LESTE = 0
    NORTE = 90
    OESTE = 180
    SUL = 270


class Abelha(turtle.Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.apareça = super().showturtle
        self.esconda = super().hideturtle
        self.penup()
        self.shape(ABELHA_LESTE)  # TODO: reduzir essas duas instruções para
        self.setheading(
            DIRECAO.LESTE
        )  # apenas uma, possivelmente a mudança de
        # shape encapsulada no setheading,
        # como já funciona em Turtle

    def atualize(self):
        x, y = xy(self.posicao, centralizar=True)
        self.goto(x, y)
        turtle.update()

    def avance_leste(self):
        self.posicao = self.posicao + 1

    def avance_sul(self):
        self.posicao = self.posicao + 8

    def avance(self):
        time.sleep(0.5)

        match self.heading():
            case DIRECAO.LESTE:
                self.avance_leste()
            case DIRECAO.SUL:
                self.avance_sul()
            case _:
                raise turtle.TurtleGraphicsError(
                    f"Direção não implementada: {self.heading()=}."
                )

        self.atualize()

        time.sleep(0.5)

    def vire_sul(self):
        self.setheading(DIRECAO.SUL)
        self.shape(ABELHA_SUL)

    def vire_oeste(self):
        self.setheading(DIRECAO.OESTE)
        self.shape(ABELHA_OESTE)

    def direita(self):
        time.sleep(0.3)

        match self.heading():
            case DIRECAO.LESTE:
                self.vire_sul()
            case _:
                raise turtle.TurtleGraphicsError(
                    f"Direção não implementada: {self.heading()=}."
                )

        self.atualize()


class Girassol(turtle.Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.apareça = super().showturtle
        self.esconda = super().hideturtle
        self.penup()
        self.shape(GIRASSOL)

    def atualize(self):
        x, y = xy(self.posicao, centralizar=True)
        self.goto(x, y)
        turtle.update()
