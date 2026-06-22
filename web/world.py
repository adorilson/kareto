import random

class World:
    def __init__(self, width=8, height=8, path=None):
        self.width = width
        self.height = height
        self.girassois = []
        self.colmeias = []
        self.nuvens = []
        self.path = path
        self.abelha = None

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


    def tem_nectar_no_girassol(self, posicao=None):
        if posicao is None:
            posicao = self.abelha._posicao_virtual

        try:
            girassol = self.girassol_em(posicao)
        except RuntimeError:
            return False

        return girassol.tem_nectar()

    def tem_nectar_na_colmeia(self, posicao=None):
        if posicao is None:
            posicao = self.abelha._posicao_virtual

        try:
            colmeia = self.colmeia_em(posicao)
        except RuntimeError:
            return False

        return colmeia.tem_nectar()

    def tem_caminho(self, destino=None):
        if self.path is None:
            return True

        if destino is not None:
            return destino in self.path

        destino = self.abelha._proxima_posicao_virtual()
        return destino in self.path


    def xy_to_pos(self, x, y):
        """Converte coordenadas (x, y) em posição linear (1 a width*height).
        A posição 1 corresponde a (0, 0), a posição 2 corresponde a (1, 0), e
        assim por diante, até a posição width*height que corresponde a
        (width-1, height-1).
        """
        if not self.in_bounds(x, y):
            raise RuntimeError(f'Coordenadas fora dos limites do mundo: ({x}, {y})')

        return y * self.width + x + 1

    def path_as_pos(self):
        """Retorna uma tupla de posições lineares correspondentes às coordenadas
        do caminho, caso o caminho esteja definido. Caso contrário, retorna uma
        tupla vazia.
        """
        if self.path is None:
            return tuple()

        return (self.xy_to_pos(x, y) for x, y in self.path)


class WorldError(Exception):
    pass
