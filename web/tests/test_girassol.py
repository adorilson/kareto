import pytest

from web.entities import GirassolPersistente


class DummyRenderer:
    def __init__(self):
        self.registered = []
        self.rendered = []

    def register_actor(self, actor):
        self.registered.append(actor)

    def render_actor(self, actor):
        self.rendered.append((actor.x, actor.y))


class DummyWorld:
    def __init__(self, width=4, height=4):
        self.width = width
        self.height = height


def test_girassol_persistente_reduz_nectar_e_nao_esconde():
    world = DummyWorld()
    renderer = DummyRenderer()
    queue = []

    girassol = GirassolPersistente(world, renderer, queue, x=0, y=0, nectares=2)

    assert girassol.value == 2
    assert girassol._hidden is False

    girassol._extract_nectar()
    assert girassol.value == 1
    assert girassol._hidden is False

    girassol._extract_nectar()
    assert girassol.value == 0
    assert girassol._hidden is False


def test_girassol_persistente_sem_nectar_gera_erro():
    world = DummyWorld()
    renderer = DummyRenderer()
    queue = []

    girassol = GirassolPersistente(world, renderer, queue, x=0, y=0, nectares=0)

    with pytest.raises(RuntimeError):
        girassol._extract_nectar()


def test_tem_nectar_retorna_true_quando_tem_nectar():
    world = DummyWorld()
    renderer = DummyRenderer()
    queue = []

    girassol = GirassolPersistente(world, renderer, queue, x=0, y=0, nectares=2)

    assert girassol.tem_nectar() is True


def test_tem_nectar_retorna_false_quando_nao_tem_nectar():
    world = DummyWorld()
    renderer = DummyRenderer()
    queue = []

    girassol = GirassolPersistente(world, renderer, queue, x=0, y=0, nectares=0)

    assert girassol.tem_nectar() is False

def test_extraia_nectar_enqueues_and_extracts():
    world = DummyWorld()
    renderer = DummyRenderer()
    queue = []

    girassol = GirassolPersistente(world, renderer, queue, x=0, y=0, nectares=2)

    assert girassol.value == 2

    girassol.extract_nectar()

    assert girassol.value == 2

    assert len(queue) == 1
    queue.pop(0)()
    assert girassol.value == 1
