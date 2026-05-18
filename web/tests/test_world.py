import pytest

from web.world import World, WorldError


class DummyGirassol:
    def __init__(self, x, y):
        self._posicao = (x, y)

    @property
    def posicao(self):
        return self._posicao


def test_init_defaults():
    world = World()

    assert world.width == 8
    assert world.height == 8
    assert world.girassois == []
    assert world.colmeias == []


def test_in_bounds_true():
    world = World(width=3, height=2)

    assert world.in_bounds(0, 0) is True
    assert world.in_bounds(2, 1) is True


def test_in_bounds_false():
    world = World(width=3, height=2)

    assert world.in_bounds(-1, 0) is False
    assert world.in_bounds(0, -1) is False
    assert world.in_bounds(3, 0) is False
    assert world.in_bounds(0, 2) is False


def test_girassol_em_retorna_correspondente():
    world = World()
    g1 = DummyGirassol(1, 2)
    g2 = DummyGirassol(3, 4)

    world.girassois.extend([g1, g2])

    assert world.girassol_em((1, 2)) is g1
    assert world.girassol_em((3, 4)) is g2


def test_girassol_em_gera_erro_quando_nao_encontra():
    world = World()

    with pytest.raises(RuntimeError):
        world.girassol_em((9, 9))


class DummyColmeia:
    def __init__(self, x, y):
        self._posicao = (x, y)

    @property
    def posicao(self):
        return self._posicao


def test_colmeia_em_retorna_correspondente():
    world = World()
    c1 = DummyColmeia(2, 1)
    c2 = DummyColmeia(4, 3)

    world.colmeias.extend([c1, c2])

    assert world.colmeia_em((2, 1)) is c1
    assert world.colmeia_em((4, 3)) is c2


def test_colmeia_em_gera_erro_quando_nao_encontra():
    world = World()

    with pytest.raises(RuntimeError):
        world.colmeia_em((9, 9))
