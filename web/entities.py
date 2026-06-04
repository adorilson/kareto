import random
from enum import IntEnum
from re import match


class Direcao(IntEnum):
    LESTE = 0
    NORTE = 90
    OESTE = 180
    SUL = 270


class Ator:
    ATOR_LESTE = "abelha_leste.gif"
    ATOR_NORTE = "abelha_norte.gif"
    ATOR_OESTE = "abelha_oeste.gif"
    ATOR_SUL = "abelha_sul.gif"

    IMAGENS = {
        Direcao.LESTE: ATOR_LESTE,
        Direcao.NORTE: ATOR_NORTE,
        Direcao.OESTE: ATOR_OESTE,
        Direcao.SUL: ATOR_SUL}

    def __init__(self, world, command_queue, x=None, y=None, direcao=Direcao.LESTE):
        super().__init__()
        self._shape = ''
        self._value = ''
        self.image_size = (80, 80)

        self.world = world
        
        self.queue = command_queue

        self.x = x if x is not None else random.randint(0, world.width - 1)
        self.y = y if y is not None else random.randint(0, world.height - 1)

        self._posicao_virtual = (self.x, self.y)
        self._direcao_virtual = direcao

        self.setheading(direcao)

    @property
    def value(self):
        return self._value

    def shape(self, name=None):
        if name is None:
            return self._shape
        else:
            self._shape = name

    def setheading(self, to_angle):
        if to_angle is None:
            return self.direcao
        
        direcao = Direcao(to_angle)
        self.direcao = direcao
        self.shape(self.IMAGENS[self.direcao])
    
    def heading(self):
        return self.direcao

    def goto(self, x, y):
        self.x = x
        self.y = y

    @property
    def posicao(self):
        return self.x, self.y

    def __str__(self):
        return super().__str__() + f" at ({self.x}, {self.y}) facing {self.direcao}"


class Abelha(Ator):
    ABELHA_LESTE = "abelha_leste.gif"
    ABELHA_NORTE = "abelha_norte.gif"
    ABELHA_OESTE = "abelha_oeste.gif"
    ABELHA_SUL = "abelha_sul.gif"

    IMAGENS = {
        Direcao.LESTE: ABELHA_LESTE,
        Direcao.NORTE: ABELHA_NORTE,
        Direcao.OESTE: ABELHA_OESTE,
        Direcao.SUL: ABELHA_SUL}

    def __init__(self, world, renderer, command_queue, x=None, y=None, direcao=Direcao.LESTE):
        super().__init__(world, command_queue, x, y, direcao)
        self.shape(self.IMAGENS[direcao])
        self.z_index = 3

        self.renderer = renderer
        self.renderer.register_actor(self)
        

    def goto(self, x, y):
        self.queue.append(lambda: self._goto(x, y))

    def _goto(self, x, y):
        super().goto(x, y)
        self.renderer.render_actor(self)

    def avance(self):
        self._posicao_virtual = self._proxima_posicao_virtual()
        self.queue.append(self._avance)

    def _proxima_posicao_virtual(self):
        x, y = self._posicao_virtual
        match self._direcao_virtual:
            case Direcao.LESTE:
                return x + 1, y
            case Direcao.OESTE:
                return x - 1, y
            case Direcao.NORTE:
                return x, y - 1
            case Direcao.SUL:
                return x, y + 1
            case _:
                raise NotImplementedError(
                    f"Direção não implementada: {self._direcao_virtual=}."
                )

    def proxima_posicao(self):
        match self.heading():
            case Direcao.LESTE:
                return self.x + 1, self.y
            case Direcao.OESTE:
                return self.x - 1, self.y
            case Direcao.NORTE:
                return self.x, self.y - 1
            case Direcao.SUL:
                return self.x, self.y + 1
            case _:
                raise NotImplementedError(
                    f"Direção não implementada: {self.heading()=}."
                )

    def tem_caminho_frente(self):
        match self.heading():
            case Direcao.LESTE:
                return self.world.in_bounds(self.x + 1, self.y)
            case Direcao.SUL:
                return self.world.in_bounds(self.x, self.y + 1)
            case Direcao.OESTE:
                return self.world.in_bounds(self.x - 1, self.y)
            case Direcao.NORTE:
                return self.world.in_bounds(self.x, self.y - 1)
            case _:
                raise NotImplementedError(
                    f"Direção não implementada: {self.heading()=}."
                )

    def _avance(self):
        if not self.tem_caminho_frente():
            raise RuntimeError("Movimento para fora dos limites do mundo.")

        match self.heading():
            case Direcao.LESTE:
                self.avance_leste()
            case Direcao.SUL:
                self.avance_sul()
            case Direcao.OESTE:
                self.avance_oeste()
            case Direcao.NORTE:
                self.avance_norte()
            case _:
                raise NotImplementedError(
                    f"Direção não implementada: {self.heading()=}."
                )

        self.renderer.render_actor(self)

    def _proxima_direcao_virtual(self):
        match self._direcao_virtual:
            case Direcao.LESTE:
                return Direcao.SUL
            case Direcao.SUL:
                return Direcao.OESTE
            case Direcao.OESTE:
                return Direcao.NORTE
            case Direcao.NORTE:
                return Direcao.LESTE
            case _:
                raise NotImplementedError(
                    f"Direção não implementada: {self._direcao_virtual=}."
                )

    def direita(self):
        self._direcao_virtual = self._direita_virtual()
        self.queue.append(self._direita)

    def _direita_virtual(self):
        match self._direcao_virtual:
            case Direcao.LESTE:
                return Direcao.SUL
            case Direcao.SUL:
                return Direcao.OESTE
            case Direcao.OESTE:
                return Direcao.NORTE
            case Direcao.NORTE:
                return Direcao.LESTE
            case _:
                raise NotImplementedError(
                    f"Direção não implementada: {self._direcao_virtual=}."
                )

    def _direita(self):
        match self.heading():
            case Direcao.LESTE:
                self.vire_sul()
            case Direcao.OESTE:
                self.vire_norte()
            case Direcao.NORTE:
                self.vire_leste()
            case Direcao.SUL:
                self.vire_oeste()
            case _:
                raise NotImplementedError(
                    f"Direção não implementada: {self.heading()=}."
                )

        self.renderer.render_actor(self)

    def esquerda(self):
        self._direcao_virtual = self._esquerda_virtual()
        self.queue.append(self._esquerda)

    def _esquerda_virtual(self):
        match self._direcao_virtual:
            case Direcao.LESTE:
                return Direcao.NORTE
            case Direcao.SUL:
                return Direcao.LESTE
            case Direcao.OESTE:
                return Direcao.SUL
            case Direcao.NORTE:
                return Direcao.OESTE
            case _:
                raise NotImplementedError(
                    f"Direção não implementada: {self._direcao_virtual=}."
                )

    def _esquerda(self):
        match self.heading():
            case Direcao.LESTE:
                self.vire_norte()
            case Direcao.OESTE:
                self.vire_sul()
            case Direcao.NORTE:
                self.vire_oeste()
            case Direcao.SUL:
                self.vire_leste()
            case _:
                raise NotImplementedError(
                    f"Direção não implementada: {self.heading()=}."
                )
        self.renderer.render_actor(self)

    def vire_sul(self):
        self.setheading(Direcao.SUL)
        self.renderer.render_actor(self)

    def vire_oeste(self):
        self.setheading(Direcao.OESTE)
        self.renderer.render_actor(self)

    def vire_norte(self):
        self.setheading(Direcao.NORTE)
        self.renderer.render_actor(self)

    def vire_leste(self):
        self.setheading(Direcao.LESTE)
        self.renderer.render_actor(self)

    def avance_leste(self):
        self.x = self.x + 1

    def avance_oeste(self):
        self.x = self.x - 1

    def avance_sul(self):
        self.y = self.y + 1

    def avance_norte(self):
        self.y = self.y - 1

    def extraia_nectar(self):
        self.queue.append(self._extraia_nectar)

    def _extraia_nectar(self):  
        girassol = self.world.girassol_em(self.posicao)
        girassol.extract_nectar()

    def faça_mel(self):
        self.queue.append(self._faça_mel)

    def _faça_mel(self):
        colmeia = self.world.colmeia_em(self.posicao)
        colmeia.faça_mel()

    def _no_girassol(self):
        try:
            return self.world.girassol_em(self.posicao) is not None
        except RuntimeError:
            return False

    def no_girassol(self):
        return self._no_girassol()

    def _na_colmeia(self):
        try:
            return self.world.colmeia_em(self.posicao) is not None
        except RuntimeError:
            return False

    def na_colmeia(self):
        return self._na_colmeia()


class Girassol(Ator):
    GIRASSOL = "girassol.gif"

    def __init__(self, world, renderer, command_queue, x=None, y=None, nectares=None):
        super().__init__(world, command_queue, x, y)

        self.shape(self.GIRASSOL)
        self.z_index = 1
        self.nectares = nectares

        self.renderer = renderer
        self.renderer.register_actor(self)
        self._hidden = False

    def esconda(self):
        if self._hidden:
            return

        self._hidden = True
        self.renderer.remove_actor(self)

    def extract_nectar(self):
        self.esconda()

    @property
    def value(self):
        if self.nectares is not None:
            return self.nectares
        else:
            return '' # TODO isso de retornar tipos diferentes não é legal.


class GirassolPersistente(Girassol):
    def __init__(self, world, renderer, command_queue, x=None, y=None, nectares=None):
        super().__init__(world, renderer, command_queue, x, y, nectares)
        self.nectares = self._parse_nectares(nectares)
        self.renderer.render_actor(self)

    def _parse_nectares(self, nectares):
        if nectares is None:
            return 0

        try:
            return int(nectares)
        except (TypeError, ValueError):
            return 0

    def esconda(self):
        self._hidden = False
        self.renderer.render_actor(self)

    def extract_nectar(self):
        if self.nectares <= 0:
            raise RuntimeError("Não há néctar para extrair.")

        self.nectares -= 1
        self.renderer.render_actor(self)

    @property
    def value(self):
        return self.nectares

class GirassolError(Exception):
    pass


class Colmeia(Ator):
    COLMEIA = "colmeia.gif"

    def __init__(self, world, renderer, command_queue, x=None, y=None, nectares=None):
        super().__init__(world, command_queue, x, y)

        self.shape(self.COLMEIA)
        self.z_index = 1
        self.nectares = self._parse_nectares(nectares)

        self.renderer = renderer
        self.renderer.register_actor(self)

    def _parse_nectares(self, nectares):
        if nectares is None:
            return 0
        elif isinstance(nectares, int):
            return nectares
        else:
            raise TypeError(f"nectares deve ser um inteiro ou None, recebeu {type(nectares)}")


    def faça_mel(self):
        if self.nectares <= 0:
            raise RuntimeError("Não há mais néctar para fazer mel.")

        self.nectares = self.nectares - 1
        self.renderer.render_actor(self)

    @property
    def value(self):
        return self.nectares


class Nuvem(Ator):
    NUVEM = "nuvem.gif"

    def __init__(self, world, renderer, command_queue, x=None, y=None):
        super().__init__(world, command_queue, x, y)

        self.shape(self.NUVEM)
        self.z_index = 2
        self.image_size = (140, 140)

        self.renderer = renderer
        self.renderer.register_actor(self)


