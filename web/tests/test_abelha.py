import pytest

from web.world import World, WorldError
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
            raise RuntimeError("girassol not found")
        return self._girassois[posicao]

    def add_colmeia(self, posicao, colmeia):
        self._colmeias[posicao] = colmeia

    def colmeia_em(self, posicao):
        if posicao not in self._colmeias:
            raise RuntimeError("colmeia not found")
        return self._colmeias[posicao]


class DummyGirassol:
    def __init__(self, queue):
        self.extracted = 0
        self.queue = queue

    def extract_nectar(self):
        self.queue.append(self._extract_nectar)

    def _extract_nectar(self):
        self.extracted = 1


class DummyColmeia:
    def __init__(self, queue=None, nectares=0):
        self.nectares = nectares
        self.queue = queue if queue is not None else []
        self.mel_feito = 0

    def faça_mel(self):
        self.queue.append(self._faça_mel)

    def _faça_mel(self):
        self.mel_feito = 1


def make_abelha(x=1, y=1, direcao=Direcao.LESTE, world=None, renderer=None):
    world = world or DummyWorld()
    renderer = renderer or DummyRenderer()
    queue = []
    return Abelha(world, renderer, queue, x=x, y=y, direcao=direcao), queue


def test_abelha_init():
    world = DummyWorld()
    renderer = DummyRenderer()
    queue = []

    abelha = Abelha(world, renderer, queue, x=2, y=3, direcao=Direcao.NORTE)

    assert world.abelha == abelha
    assert renderer.registered == [abelha]
    assert abelha.z_index == 3
    assert abelha.shape() == Abelha.IMAGENS[Direcao.NORTE]
    assert abelha.IMAGE_SIZE == (80, 80)


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
    assert abelha.heading() == Direcao.LESTE

    assert len(queue) == 1
    queue.pop(0)()
    assert abelha.heading() == Direcao.SUL


def test_esquerda_enqueues_and_rotates():
    abelha, queue = make_abelha(direcao=Direcao.LESTE)

    abelha.esquerda()

    assert len(queue) == 1
    queue.pop(0)()
    assert abelha.heading() == Direcao.NORTE


def test_abelha_proxima_posicao():
    abelha, _ = make_abelha(x=1, y=1, direcao=Direcao.LESTE)
    assert abelha.proxima_posicao() == (2, 1)

    abelha, _ = make_abelha(x=1, y=1, direcao=Direcao.SUL)
    assert abelha.proxima_posicao() == (1, 2)

    abelha, _ = make_abelha(x=1, y=1, direcao=Direcao.OESTE)
    assert abelha.proxima_posicao() == (0, 1)

    abelha, _ = make_abelha(x=1, y=1, direcao=Direcao.NORTE)
    assert abelha.proxima_posicao() == (1, 0)


def test_abelha_proxima_posicao_virtual():
    abelha, _ = make_abelha(x=1, y=1, direcao=Direcao.LESTE)
    assert abelha._proxima_posicao_virtual() == (2, 1)

    abelha, _ = make_abelha(x=1, y=1, direcao=Direcao.SUL)
    assert abelha._proxima_posicao_virtual() == (1, 2)

    abelha, _ = make_abelha(x=1, y=1, direcao=Direcao.OESTE)
    assert abelha._proxima_posicao_virtual() == (0, 1)

    abelha, _ = make_abelha(x=1, y=1, direcao=Direcao.NORTE)
    assert abelha._proxima_posicao_virtual() == (1, 0)


def test_extraia_nectar_enqueues_and_extracts():
    world = DummyWorld()
    renderer = DummyRenderer()
    queue = []
    abelha = Abelha(world, renderer, queue, x=1, y=1, direcao=Direcao.LESTE)
    girassol = DummyGirassol(queue=queue)
    world.add_girassol((1, 1), girassol)

    abelha.extraia_nectar()
    assert girassol.extracted == 0

    assert len(queue) == 1
    queue.pop(0)()
    assert girassol.extracted == 1


def test_abelha_faça_mel_enqueues_and_makes_honey():
    world = DummyWorld()
    renderer = DummyRenderer()
    queue = []
    abelha = Abelha(world, renderer, queue, x=1, y=1, direcao=Direcao.LESTE)
    colmeia = DummyColmeia(queue=queue, nectares=2)
    world.add_colmeia((1, 1), colmeia)

    abelha.faça_mel()
    assert len(queue) == 1
    assert colmeia.mel_feito == 0

    assert len(queue) == 1
    queue.pop(0)()
    assert colmeia.mel_feito == 1


def test_no_girassol_retornando_true_quando_na_mesma_posicao():
    world = DummyWorld()
    renderer = DummyRenderer()
    queue = []
    abelha = Abelha(world, renderer, queue, x=1, y=1, direcao=Direcao.LESTE)
    world.add_girassol((1, 1), DummyGirassol(queue=queue))

    assert abelha.no_girassol() is True


def test_no_girassol_retornando_false_quando_nao_ha_girassol():
    world = DummyWorld()
    renderer = DummyRenderer()
    queue = []
    abelha = Abelha(world, renderer, queue, x=1, y=1, direcao=Direcao.LESTE)

    assert abelha.no_girassol() is False


def test_abelha_avance():
    """
    Abelha.avance() should call _avance() and enqueue it, plus
    update Abelha._posicao_virtual
    """
    world = DummyWorld(width=4, height=4)
    world.tem_caminho = lambda: True  # Override tem_caminho to check the path
    renderer = DummyRenderer()
    queue = []
    abelha = Abelha(world, renderer, queue, x=1, y=1, direcao=Direcao.LESTE)

    abelha.avance()

    assert len(queue) == 1
    queue[0] == Abelha.avance  # executa o avance enqueued
    # posição real não deve mudar até a execução
    assert abelha.posicao == (1, 1)
    assert abelha._posicao_virtual == (2, 1)

    queue.pop(0)()  # executa o avance enqueued
    assert abelha.posicao == (2, 1)  # posição real deve ser atualizada
    # posição virtual se mantém igual à real após a execução do avance
    assert abelha._posicao_virtual == (2, 1)


def test_abelha_avance_sem_caminho():
    """
    Abelha.avance() should raise RuntimeError when there is no path to the
    next position
    """
    world = DummyWorld(width=4, height=4)
    world.path = [(1, 1), (1, 2)]  # Only allow movement to (1, 2)
    world.tem_caminho = lambda: False  # Override tem_caminho to check the path
    renderer = DummyRenderer()
    queue = []
    abelha = Abelha(world, renderer, queue, x=1, y=1, direcao=Direcao.LESTE)

    with pytest.raises(WorldError):
        abelha.avance()

    assert len(queue) == 1
    with pytest.raises(RuntimeError):
        # This should raise an error since (2, 1) is not in the path
        queue.pop(0)()


def test_abelha_avance_na_fila():
    """
    Executar a função enqueued por Abelha.avance() deve atualizar a posição real
    """
    world = DummyWorld(width=4, height=4)
    world.tem_caminho = lambda: True  # Override tem_caminho to check the path
    renderer = DummyRenderer()
    queue = []
    abelha = Abelha(world, renderer, queue, x=1, y=1, direcao=Direcao.LESTE)

    abelha.avance()

    cmd = queue.pop(0)
    cmd()  # executa o avance enqueued
    assert abelha.posicao == (2, 1)  # posição real deve ser atualizada


def test_direita():
    """
    Abelha.direita() should call _direita() and enqueue it, plus
    update Abelha._direcao_virtual
    """
    world = DummyWorld()
    renderer = DummyRenderer()
    queue = []
    abelha = Abelha(world, renderer, queue, x=1, y=1, direcao=Direcao.LESTE)

    abelha.direita()

    assert len(queue) == 1
    queue[0] == Abelha.direita  # executa o direita enqueued
    assert abelha.heading() == Direcao.LESTE  # direção real não deve mudar até a execução
    assert abelha._direcao_virtual == Direcao.SUL


def test_na_colmeia_retornando_true_quando_na_mesma_posicao():
    world = DummyWorld()
    renderer = DummyRenderer()
    queue = []
    abelha = Abelha(world, renderer, queue, x=1, y=1, direcao=Direcao.LESTE)
    world.add_colmeia((1, 1), DummyColmeia())

    assert abelha.na_colmeia() is True


def test_na_colmeia_retornando_false_quando_nao_ha_colmeia():
    world = DummyWorld()
    renderer = DummyRenderer()
    queue = []
    abelha = Abelha(world, renderer, queue, x=1, y=1, direcao=Direcao.LESTE)

    assert abelha.na_colmeia() is False
