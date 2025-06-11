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


def girassol_em(posição):
    for a in turtle.turtles():
        if  isinstance(a, Girassol) and a.posição == posição:
            return a


class Abelha(turtle.Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.apareça = super().showturtle
        self.esconda = super().hideturtle
        self.penup()
        self.posição = 0
        self.shape(ABELHA_LESTE)  # TODO: reduzir essas duas instruções para
        self.setheading(
            DIRECAO.LESTE
        )  # apenas uma, possivelmente a mudança de
        # shape encapsulada no setheading,
        # como já funciona em Turtle
        #self.jardim = jardim

    def atualize(self):
        x, y = xy(self.posição, centralizar=True)
        self.goto(x, y)
        turtle.update()

    def avance_leste(self):
        self.posição = self.posição + 1

    def avance_sul(self):
        self.posição = self.posição + 8

    def avance_oeste(self):
        self.posição = self.posição - 1

    def avance_norte(self):
        self.posição = self.posição - 8

    def avance(self):
        time.sleep(0.5)

        match self.heading():
            case DIRECAO.LESTE:
                self.avance_leste()
            case DIRECAO.SUL:
                self.avance_sul()
            case DIRECAO.OESTE:
                self.avance_oeste()
            case DIRECAO.NORTE:
                self.avance_norte()
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

    def vire_norte(self):
        self.setheading(DIRECAO.NORTE)
        self.shape(ABELHA_NORTE)

    def vire_leste(self):
        self.setheading(DIRECAO.LESTE)
        self.shape(ABELHA_LESTE)

    def vire_para(self, direção):
        match direção:
            case DIRECAO.SUL:
                self.vire_sul()
            case DIRECAO.OESTE:
                self.vire_oeste()
            case DIRECAO.NORTE:
                self.vire_norte()
            case DIRECAO.LESTE:
                self.vire_leste()
            case _:
                raise turtle.TurtleGraphicsError(
                    f"Direção não implementada: {direção=}."
                )

    def direita(self):
        time.sleep(0.3)

        match self.heading():
            case DIRECAO.LESTE:
                self.vire_sul()
            case DIRECAO.OESTE:
                self.vire_norte()
            case DIRECAO.NORTE:
                self.vire_leste()
            case DIRECAO.SUL:
                self.vire_oeste()
            case _:
                raise turtle.TurtleGraphicsError(
                    f"Direção não implementada: {self.heading()=}."
                )

        self.atualize()

    def esquerda(self):
        time.sleep(0.3)

        match self.heading():
            case DIRECAO.LESTE:
                self.vire_norte()
            case DIRECAO.OESTE:
                self.vire_sul()
            case DIRECAO.NORTE:
                self.vire_oeste()
            case DIRECAO.SUL:
                self.vire_leste()
            case _:
                raise turtle.TurtleGraphicsError(
                    f"Direção não implementada: {self.heading()=}."
                )

        self.atualize()

    def obtenha_nectar(self):
        girassol = girassol_em(self.posição)
        girassol.extract_nectar()
        turtle.update()



class Escritora(turtle.Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.color('white')
        self.penup()
        self.font = font=('Arial', 10, 'bold')

    def escreva(self, obj):
        self.write(obj, font=self.font)


class GirassolError(Exception):
    ...


class Girassol(turtle.Turtle):
    def __init__(self, posição, nectar=0):
        super().__init__(visible=False)
        self.apareça = super().showturtle
        self.esconda = super().hideturtle
        self.penup()
        self.shape(GIRASSOL)
        self.nectar = nectar
        self.escritora = Escritora()
        self.posição = posição

    def __str__(self):
        return f"Girassol(posição={self.posição}, nectar={self.nectar})"

    def atualize(self):
        x, y = xy(self.posição, centralizar=True)
        self.goto(x, y)

        escritora = self.escritora
        escritora.clear()
        escritora.goto(x+15, y-25)
        escritora.escreva(self.nectar)

        turtle.update()

    def extract_nectar(self):
        if self.nectar>0:
            self.nectar = self.nectar - 1
        else:
            raise GirassolError("Não há mais nectar para ser colhido.")
        self.atualize()
