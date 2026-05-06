class World:
    def __init__(self, width=8, height=8):
        self.width = width
        self.height = height
        self.girassois = []

    def in_bounds(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def girassol_em(self, posicao):
        for gs in self.girassois:
            if gs.posicao == posicao:
                return gs

        raise RuntimeError(f'Não há girassol na posição {posicao}')

class WorldError(Exception):
    pass