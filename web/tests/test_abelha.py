import pytest

from web.entities import Abelha, Direcao


class DummyRenderer:
    def __init__(self):
        self.registered = []
        self.rendered = []

    def register_actor(self, actor):
        self.registered.append(actor)

    def render_actor(self, actor):
        self.rendered.append((actor.x, actor.y, actor.direcao))


class DummyWorld:
    def __init__(self, width=4, height=4):
        self.width = width
        self.height = height
        self._girassois = {}
        self._colmeias = {}

    def in_bounds(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def add_girassol(self, posicao, girassol):
        self._girassois[posicao] = girassol

    def girassol_em(self, posicao):
        if posicao not in self._girassois:
            raise KeyError("girassol not found")
        return self._girassois[posicao]

    def add_colmeia(self, posicao, colmeia):
        self._colmeias[posicao] = colmeia

    def colmeia_em(self, posicao):
        if posicao not in self._colmeias:
            raise KeyError("colmeia not found")
        return self._colmeias[posicao]


class DummyGirassol:
    def __init__(self):
        self.extracted = 0

    def extract_nectar(self):
        self.extracted += 1


class DummyColmeia:
    def __init__(self, nectares=0):
        self.nectares = nectares

    def faça_mel(self):
        self.nectares -= 1


def make_abelha(x=1, y=1, direcao=Direcao.LESTE, world=None, renderer=None):
    world = world or DummyWorld()
    renderer = renderer or DummyRenderer()
    queue = []
    return Abelha(world, renderer, queue, x=x, y=y, direcao=direcao), queue


def test_init_registers_actor_and_sets_shape_and_zindex():
    world = DummyWorld()
    renderer = DummyRenderer()
    queue = []

    abelha = Abelha(world, renderer, queue, x=2, y=3, direcao=Direcao.NORTE)

    assert renderer.registered == [abelha]
    assert abelha.z_index == 3
    assert abelha.shape() == Abelha.IMAGENS[Direcao.NORTE]
    assert abelha.image_size == (80, 80)


def test_goto_enqueues_and_moves_and_renders():
    abelha, queue = make_abelha(x=0, y=0)

    abelha.goto(3, 2)

    assert len(queue) == 1
    queue.pop(0)()
    assert abelha.posicao == (3, 2)
    assert abelha.renderer.rendered[-1][:2] == (3, 2)


@pytest.mark.parametrize(
    "direcao, start, expected",
    [
        (Direcao.LESTE, (1, 1), (2, 1)),
        (Direcao.OESTE, (2, 1), (1, 1)),
        (Direcao.NORTE, (1, 2), (1, 1)),
        (Direcao.SUL, (1, 1), (1, 2)),
    ],
)
def test_avance_moves_and_renders(direcao, start, expected):
    world = DummyWorld(width=4, height=4)
    renderer = DummyRenderer()
    queue = []
    abelha = Abelha(
        world, renderer, queue, x=start[0], y=start[1], direcao=direcao
    )

    abelha._avance()

    assert abelha.posicao == expected
    assert renderer.rendered[-1][:2] == expected


def test_avance_raises_out_of_bounds():
    world = DummyWorld(width=2, height=2)
    renderer = DummyRenderer()
    queue = []
    abelha = Abelha(world, renderer, queue, x=1, y=0, direcao=Direcao.LESTE)

    with pytest.raises(RuntimeError):
        abelha._avance()


def test_direita_enqueues_and_rotates():
    abelha, queue = make_abelha(direcao=Direcao.LESTE)

    abelha.direita()

    assert len(queue) == 1
    queue.pop(0)()
    assert abelha.heading() == Direcao.SUL


def test_esquerda_enqueues_and_rotates():
    abelha, queue = make_abelha(direcao=Direcao.LESTE)

    abelha.esquerda()

    assert len(queue) == 1
    queue.pop(0)()
    assert abelha.heading() == Direcao.NORTE


def test_extraia_nectar_enqueues_and_extracts():
    world = DummyWorld()
    renderer = DummyRenderer()
    queue = []
    abelha = Abelha(world, renderer, queue, x=1, y=1, direcao=Direcao.LESTE)
    girassol = DummyGirassol()
    world.add_girassol((1, 1), girassol)

    abelha.extraia_nectar()

    assert len(queue) == 1
    queue.pop(0)()
    assert girassol.extracted == 1


def test_faca_mel_enqueues_and_extracts():
    world = DummyWorld()
    renderer = DummyRenderer()
    queue = []
    abelha = Abelha(world, renderer, queue, x=1, y=1, direcao=Direcao.LESTE)
    colmeia = DummyColmeia(nectares=2)
    world.add_colmeia((1, 1), colmeia)

    abelha.faça_mel()

    assert len(queue) == 1
    queue.pop(0)()
    assert colmeia.nectares == 1
