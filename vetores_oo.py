from freegames import floor

class Humano:
    ...

class Mulher(Humano):
    ...

class Homem(Humano):
    ...

class Ponto(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return f'Ponto({self.x}, {self.y})'

    def __add__(self, ponto):
        return Ponto(self.x + ponto.x, self.y + ponto.y)

    def mova(self, ponto):
        self.x = self.x + ponto.x
        self.y = self.y + ponto.y

class PlanoCartesiano:
    def __init__(self, pontos):
        self.pontos = pontos

coord_x = 0
coord_y = 0

g1_x = 10
g1_y = 20

gn_x = 38
gn_y = 1

# funcoes / operacoes
def exiba(point):
    return f'({coord_x}, {coord_y})'

def soma(point, x, y):
    return (coord_x + x, coord_y + y)

def mova(point, x, y):
    coord_x = coord_x + x
    coord_y = coord_y + y

def deslocamento(coord_x, coord_y):
    x = (floor(coord_x, 20) + 200) / 20
    y = (180 - floor(coord_y, 20)) / 20
    index = int(x + y * 20)
    return index


def validação():
    pass

def distancia():
    pass

def diferença():
    pass






