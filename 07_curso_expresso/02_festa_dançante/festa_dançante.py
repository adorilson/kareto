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

    def _rodopia(self):
        if self.rodopiando:
            for _ in range(4):
                self.left(90)

            turtle.ontimer(self._rodopia, 4000)

    def rodopia(self):
        self.rodopiando = not self.rodopiando
        self._rodopia()

    def move(self):
        x = random.randint(-150, 150)
        y = random.randint(-150, 150)
        self.goto(x, y)

        turtle.ontimer(self.move, 3000)

    def para_tudo(self):
        self.balançando = False
        self.rodopiando = False

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


def muda_palco(repete=0):
    import random

    cores = ["lightyellow", "lightblue", "lightcyan",  "lightgray",
             "lightcoral",  "lightpink", "lightsalmon", "lightgreen"]
    cor = random.choice(cores)

    palco = turtle.Screen()
    palco.bgcolor(cor)

    if repete:
        turtle.ontimer(lambda: muda_palco(repete),  1000*repete)


def a_cada_compasso(fun, compasso=3):
    turtle.ontimer(lambda: fun(compasso), 1000*compasso)


def defina(tipo, propriedade, valor):
    for t in turtle.turtles():
        m = getattr(t, propriedade)
        m(valor)


turtle.setup(500, 500)
turtle.listen()

Contadora()

if __name__=='__main__':
    turtle.mainloop()
