from functools import partial
import turtle
import random


locais = {'Direita': 150,
          'Esquerda': -150,
          'Centro': 0,
          }


class Contadora(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-200, 200)
        self.tempo = 0
        self.tipo = 'Contadora'
        self.atualiza_tempo()

    def atualiza_tempo(self):
        self.clear()
        self.write(f'Compasso: {self.tempo}', font=('Arial', 20, 'bold'))
        self.tempo = self.tempo + 1
        turtle.ontimer(self.atualiza_tempo, 1000)


class Dançarino(turtle.Turtle):
    metodos_balanço = {'mexe_direita': 'mexe_esquerda',
                    'mexe_esquerda': 'mexe_direita'}

    def __init__(self, tipo='Principal', local='Centro'):
        turtle.Turtle.__init__(self, visible=False)
        self.penup()
        self.setx(locais[local])
        self.shape('turtle')
        self.shapesize(3)
        self.posicao_base = 90
        self.setheading(self.posicao_base)
        self.showturtle()
        self.tipo = tipo

        self.balançando = False
        self.proximo_balanço = 'mexe_direita'
        self.balança()

        self.rodopiando = False
        self.movendo = False

    def aleatório(self):
        ações = (self.mexe_direita, self.mexe_esquerda,
                 self.anda_direita, self.anda_esquerda,
                 self.faz_rodopio, self.rodopia,
                 self.balança,
                 self.move, self._move,
                 self.para_tudo,
                 self.muda_cor,
        )
        ação = random.choice(ações)
        ação()

    def muda_cor(self):
        r = random.randint(1, 255)
        g = random.randint(1, 255)
        b = random.randint(1, 255)
        self.color(r, g, b)

    def _balança(self, lado):
         if self.balançando:
            metodo = getattr(self, lado)
            metodo()
            turtle.ontimer(lambda: self._balança(self.proximo_balanço), 1000)
            self.proximo_balanço = self.metodos_balanço[self.proximo_balanço]

    def balança(self):
        self.balançando = not self.balançando
        self._balança(self.proximo_balanço)

    def mexe_direita(self):
        self.setheading(self.posicao_base + 5)

    def mexe_esquerda(self):
        self.setheading(self.posicao_base - 5)

    def anda_esquerda(self):
        self.setx(self.xcor()-10)

    def anda_direita(self):
        self.setx(self.xcor()+10)

    def faz_rodopio(self):
        for _ in range(4):
            self.left(90)

    def _rodopia(self):
        if self.rodopiando:
            self.faz_rodopio()
            turtle.ontimer(self._rodopia, 4000)

    def rodopia(self):
        self.rodopiando = not self.rodopiando
        self._rodopia()

    def _move(self):
        if self.movendo:
            x = random.randint(-150, 150)
            y = random.randint(-150, 150)
            self.goto(x, y)

            turtle.ontimer(self._move, 3000)

    def move(self):
        self.movendo = not self.movendo
        self._move()

    def para_tudo(self):
        self.balançando = False
        self.rodopiando = False
        self.movendo = False

def cria_dançarino(tipo, local):
    dançarino = Dançarino(tipo, local)
    return dançarino


def cria_dançarinos_apoio(quantidade, tipo, local):
    turtle.tracer(0)
    posicao_base = 360/quantidade
    for q in range(quantidade):
        apoio = Dançarino(tipo)
        apoio.penup()
        apoio.shape('turtle')
        apoio.shapesize(2)
        apoio.setheading(posicao_base*(q+1))
        apoio.forward(150)
        apoio.posicao_base =  apoio.heading()
    turtle.update()
    turtle.tracer(1)


def muda_palco():
    import random

    cores = ["lightyellow", "lightblue", "lightcyan",  "lightgray",
             "lightcoral",  "lightpink", "lightsalmon", "lightgreen"]
    cor = random.choice(cores)

    palco = turtle.Screen()
    palco.bgcolor(cor)


def a_cada_compasso(func, compasso=3, *args, **kwargs):
    func_com_args = partial(func, *args, **kwargs)

    def repetidor():
        func_com_args()
        turtle.ontimer(repetidor, 1000 * compasso)

    turtle.ontimer(repetidor, 1000 * compasso)


def defina(tipo, propriedade, valor):
    dançarinos = tuple(filter(lambda t: t.tipo==tipo, turtle.turtles()))
    if not dançarinos:
        raise turtle.TurtleGraphicsError(f'Tipo de dançarino inexistente.: {tipo}')

    for d in dançarinos:
        m = getattr(d, propriedade)
        m(valor)


turtle.colormode(255)
turtle.setup(500, 500)
turtle.listen()

Contadora()

if __name__=='__main__':
    d = Dançarino()

    turtle.onkey(d.aleatório, 'a')
    turtle.onkey(d.rodopia, 'r')
    turtle.onkey(d.balança, 'b')
    turtle.onkey(d.muda_cor, 'c')
    turtle.onkey(d.move, 'm')
    turtle.onkey(d.para_tudo, 'p')
    a_cada_compasso(muda_palco, 2)
    a_cada_compasso(cria_dançarino, 3, 'Apoio', 'Centro')

    turtle.listen()
    turtle.mainloop()
