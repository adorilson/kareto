import random
from enum import IntEnum


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
        super().__init__(visible=False)
        self._shape = ''
        self.world = world
        
        self.queue = command_queue

        self.x = x if x is not None else random.randint(0, world.width - 1)
        self.y = y if x is not None else random.randint(0, world.height - 1)

        self.setheading(direcao)


    def shape(self, name=None):
        if name is None:
            return self._shape
        else:
            self._shape = name

    def setheading(self, to_angle):
        if to_angle is None:
            return self.direcao
        elif to_angle not in Direcao:
            raise ValueError(f"Direção inválida: {to_angle}.")
        else:
            self.direcao = to_angle
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
        self.queue.append(self._avance)

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
            raise ValueError("Movimento para fora dos limites do mundo.")

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

    def direita(self):
        self.queue.append(self._direita)

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
        self.queue.append(self._esquerda)

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


class Girassol(Ator):
    GIRASSOL = "girassol.gif"

    def __init__(self, world, renderer, command_queue, x=None, y=None, direcao=Direcao.LESTE):
        super().__init__(world, command_queue, x, y, direcao)

        self.shape(self.GIRASSOL)
        self.z_index = 1

        self.renderer = renderer
        self.renderer.register_actor(self)
