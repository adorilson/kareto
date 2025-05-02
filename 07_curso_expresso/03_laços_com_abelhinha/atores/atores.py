import turtle
import time
import random

ABELHA_LESTE = "abelha_leste.gif"
ABELHA_NORTE = "abelha_norte.gif"
ABELHA_OESTE = "abelha_oeste.gif"
ABELHA_SUL = "abelha_sul.gif"

GIRASSOL = "girassol.gif"

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
    """Converte um número de célula para coordenadas (x, y), com origem no canto superior esquerdo."""
    return ((celula % 8) * 50 - 200 + centralizar*25), (200 - (celula // 8) * 50 - centralizar*25)


class Abelha(turtle.Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.apareça = super().showturtle
        self.esconda = super().hideturtle
        self.penup()
        self.shape(ABELHA_LESTE)

    def atualize(self):
        x, y = xy(self.posicao, centralizar=True)
        self.goto(x, y)
        turtle.update()

    def avance(self):
        time.sleep(0.5)
        self.posicao += 1
        self.atualize()
        time.sleep(0.5)


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


if __name__ == "__main__":
    configurar_janela()
    abelha = Abelha()
    abelha.posicao = 0
    abelha.atualize()
    abelha.apareça()

    for posicao in (7, 56, 63):
        flor = Girassol()
        flor.posicao = posicao
        flor.atualize()
        flor.apareça()

    turtle.update()
    turtle.mainloop()
