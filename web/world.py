import random

class World:
    def __init__(self, width=8, height=8):
        self.width = width
        self.height = height
        self.girassois = []
        self.colmeias = []
        self.nuvens = []

    def in_bounds(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def girassol_em(self, posicao):
        for gs in self.girassois:
            if gs.posicao == posicao:
                return gs

        raise RuntimeError(f'Não há girassol na posição {posicao}')

    def colmeia_em(self, posicao):
        for colmeia in self.colmeias:
            if colmeia.posicao == posicao:
                return colmeia

        raise RuntimeError(f'Não há colmeia na posição {posicao}')

    def remove_nuvens(self):
        for nuvem in self.nuvens:
            nuvem.renderer.remove_actor(nuvem)
        self.nuvens = []


    def sorteia_girassois(self):
        for girassol in list(self.girassois):
            prob = getattr(girassol, "remove_prob", None)
            if prob is None or prob <= 0:
                continue

            if prob >= 1 or random.random() <= prob:
                girassol.renderer.remove_actor(girassol)
                self.girassois.remove(girassol)

    def sorteia_colmeias(self):
        for colmeia in list(self.colmeias):
            prob = getattr(colmeia, "remove_prob", None)
            if prob is None or prob <= 0:
                continue

            if prob >= 1 or random.random() <= prob:
                colmeia.renderer.remove_actor(colmeia)
                self.colmeias.remove(colmeia)

    def sorteia_girassois_e_colmeias(self):
        posicoes_girassois = tuple(gs.posicao for gs in self.girassois)
        for posicao in posicoes_girassois:
            try:
                colmeia = self.colmeia_em(posicao)
            except RuntimeError:
                continue

            if random.random() <= 0.5:
                colmeia.renderer.remove_actor(colmeia)
                self.colmeias.remove(colmeia)
            else:
                girassol = self.girassol_em(posicao)
                girassol.renderer.remove_actor(girassol)
                self.girassois.remove(girassol)


class WorldError(Exception):
    pass
