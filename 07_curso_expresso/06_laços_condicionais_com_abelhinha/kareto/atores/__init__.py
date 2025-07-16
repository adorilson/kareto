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
COLMEIA = caminho("colmeia.gif")
NUVEM = caminho("nuvem.gif")

turtle.register_shape(ABELHA_LESTE)
turtle.register_shape(ABELHA_OESTE)
turtle.register_shape(ABELHA_NORTE)
turtle.register_shape(ABELHA_SUL)
turtle.register_shape(GIRASSOL)
turtle.register_shape(COLMEIA)
turtle.register_shape(NUVEM)


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


def colméia_em(posição):
    for a in turtle.turtles():
        if  isinstance(a, Colméia) and a.posição == posição:
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

        # Verifica se há caminho à frente antes de avançar
        caminho_posicoes = getattr(self, 'caminho_posicoes', None)
        if caminho_posicoes is not None:
            direcao = self.heading()
            pos = self.posição
            if direcao == DIRECAO.LESTE:
                proxima = pos + 1
            elif direcao == DIRECAO.OESTE:
                proxima = pos - 1
            elif direcao == DIRECAO.NORTE:
                proxima = pos - 8
            elif direcao == DIRECAO.SUL:
                proxima = pos + 8
            else:
                raise AbelhaError(f"Direção não implementada: {self.heading()=}")
            if proxima not in caminho_posicoes:
                raise AbelhaError("Não há caminho à frente da abelha!")

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

    def faça_mel(self):
        colméia = colméia_em(self.posição)
        colméia.faça_mel()
        turtle.update()

    def na_colmeia(self):
        return colméia_em(self.posição) is not None

    def no_girassol(self):
        return girassol_em(self.posição) is not None


class Escritora(turtle.Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.color('white')
        self.penup()
        self.font = font=('Arial', 10, 'bold')

    def escreva(self, obj):
        self.write(obj, font=self.font, align="center")


class GirassolError(Exception):
    ...


class ColméiaError(turtle.TurtleGraphicsError):
    ...


class AbelhaError(turtle.TurtleGraphicsError):
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
        time.sleep(0.3)
        if self.nectar>0:
            self.nectar = self.nectar - 1
        else:
            raise GirassolError("Não há mais nectar para ser colhido.")
        self.atualize()


class Colméia(turtle.Turtle):
    def __init__(self, posição, nectar=0):
        super().__init__(visible=False)
        self.apareça = super().showturtle
        self.esconda = super().hideturtle
        self.penup()
        self.shape(COLMEIA)
        self.nectar = nectar
        self.escritora = Escritora()
        self.posição = posição

    def __str__(self):
        return f"Colméia(posição={self.posição}, nectar={self.nectar})"

    def atualize(self):
        x, y = xy(self.posição, centralizar=True)
        self.goto(x, y)

        escritora = self.escritora
        escritora.clear()
        escritora.goto(x+15, y-25)
        escritora.escreva(self.nectar)

        turtle.update()

    def faça_mel(self):
        time.sleep(0.3)
        if self.nectar>0:
            self.nectar = self.nectar - 1
        else:
            raise ColméiaError("Não há mais nectar para fazer mel.")
        self.atualize()


class Nuvem(turtle.Turtle):
    def __init__(self, posição):
        super().__init__(visible=False)
        self.apareça = super().showturtle
        self.esconda = super().hideturtle
        self.penup()
        self.shape(NUVEM)
        self.posição = posição

    def __str__(self):
        return f"Nuvem(posição={self.posição})"

    def atualize(self):
        x, y = xy(self.posição, centralizar=True)
        self.goto(x, y)
        turtle.update()


def tem_nectar_no_girassol():
    """Retorna True se o girassol na posição da abelha tiver néctar, False caso contrário."""
    for a in turtle.turtles():
        if isinstance(a, Abelha):
            pos = a.posição
            girassol = girassol_em(pos)
            if girassol is not None and getattr(girassol, 'nectar', 0) > 0:
                return True
            else:
                return False
    return False


def tem_mel_na_colmeia():
    """Retorna True se a colmeia na posição da abelha tiver néctar para fazer mel, False caso contrário."""
    for a in turtle.turtles():
        if isinstance(a, Abelha):
            pos = a.posição
            colmeia = colméia_em(pos)
            if colmeia is not None and getattr(colmeia, 'nectar', 0) > 0:
                return True
            else:
                return False
    return False


def tem_caminho(caminho_posicoes):
    """Retorna True se há caminho (posição numérica) à frente da abelha, False caso contrário."""
    for a in turtle.turtles():
        if isinstance(a, Abelha):
            pos = a.posição
            direcao = a.heading()
            if direcao == DIRECAO.LESTE:
                proxima = pos + 1
            elif direcao == DIRECAO.OESTE:
                proxima = pos - 1
            elif direcao == DIRECAO.NORTE:
                proxima = pos - 8
            elif direcao == DIRECAO.SUL:
                proxima = pos + 8
            else:
                return False
            return proxima in caminho_posicoes
    return False

