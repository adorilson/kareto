import pytest

from web.entities import Colmeia


class DummyRenderer:
    def __init__(self):
        self.registered = []
        self.rendered = []

    def register_actor(self, actor):
        self.registered.append(actor)
        self.render_actor(actor) # isso talvez seja um erro de modelagem OO

    def render_actor(self, actor):
        self.rendered.append((actor.x, actor.y))


class DummyWorld:
    def __init__(self, width=4, height=4):
        self.width = width
        self.height = height


def test_colmeia_init_registra_e_renderiza():
    world = DummyWorld()
    renderer = DummyRenderer()
    queue = []

    colmeia = Colmeia(world, renderer, queue, x=1, y=2, nectares=3)

    assert renderer.registered == [colmeia]
    assert colmeia.shape() == Colmeia.COLMEIA
    assert colmeia.z_index == 1
    assert colmeia.value == 3
    assert renderer.rendered[-1] == (1, 2)


def test_colmeia_init_com_nectar_nao_inteiro():
    world = DummyWorld()
    renderer = DummyRenderer()
    queue = []

    colmeia = Colmeia(world, renderer, queue, x=2, y=1, nectares=None)

    assert colmeia.value == 0
    assert renderer.rendered[-1] == (2, 1)

    with pytest.raises(TypeError):
        colmeia = Colmeia(world, renderer, queue, x=2, y=1, nectares='42')


def test_colmeia_faca_mel_diminui_e_renderiza():
    world = DummyWorld()
    renderer = DummyRenderer()
    queue = []

    colmeia = Colmeia(world, renderer, queue, x=0, y=0, nectares=2)

    colmeia.faça_mel()
    assert colmeia.value == 1
    assert renderer.rendered[-1] == (0, 0)

    colmeia.faça_mel()
    assert colmeia.value == 0


def test_colmeia_faca_mel_sem_nectar_gera_erro():
    world = DummyWorld()
    renderer = DummyRenderer()
    queue = []

    colmeia = Colmeia(world, renderer, queue, x=0, y=0, nectares=0)

    with pytest.raises(RuntimeError):
        colmeia.faça_mel()


def test_colmeia_tem_nectar_retorna_true_quando_tem_nectar():
    world = DummyWorld()
    renderer = DummyRenderer()
    queue = []

    colmeia = Colmeia(world, renderer, queue, x=0, y=0, nectares=2)

    assert colmeia.tem_nectar() is True


def test_colmeia_tem_nectar_retorna_false_quando_nao_tem_nectar():
    world = DummyWorld()
    renderer = DummyRenderer()
    queue = []

    colmeia = Colmeia(world, renderer, queue, x=0, y=0, nectares=0)

    assert colmeia.tem_nectar() is False
