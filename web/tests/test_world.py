import pytest

from web.world import World, WorldError


class DummyGirassol:
    def __init__(self, x, y, renderer=None):
        self._posicao = (x, y)
        self.renderer = renderer

    @property
    def posicao(self):
        return self._posicao


def test_init_defaults():
    world = World()

    assert world.width == 8
    assert world.height == 8
    assert world.girassois == []
    assert world.colmeias == []
    assert world.nuvens == []


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
    def __init__(self, x, y, renderer=None):
        self._posicao = (x, y)
        self.renderer = renderer

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


class DummyRenderer:
    def __init__(self):
        self.removed = []

    def remove_actor(self, actor):
        self.removed.append(actor)


class DummyNuvem:
    def __init__(self, renderer):
        self.renderer = renderer


def test_remove_nuvens_limpa_e_remove_do_renderer():
    world = World()
    renderer = DummyRenderer()
    nuvem1 = DummyNuvem(renderer)
    nuvem2 = DummyNuvem(renderer)

    world.nuvens.extend([nuvem1, nuvem2])

    world.remove_nuvens()

    assert renderer.removed == [nuvem1, nuvem2]
    assert world.nuvens == []


def test_sorteia_girassois_remove_com_probabilidade_1_e_deixa_com_0():
    world = World()
    renderer = DummyRenderer()
    g1 = DummyGirassol(1, 2, renderer)
    g1.remove_prob = 1
    g2 = DummyGirassol(3, 4, renderer)
    g2.remove_prob = 0

    world.girassois.extend([g1, g2])

    world.sorteia_girassois()

    assert renderer.removed == [g1]
    assert world.girassois == [g2]


def test_sorteia_girassois_remove_com_probabilidade_varias():
    world = World()
    renderer = DummyRenderer()
    g1 = DummyGirassol(1, 2, renderer)
    g1.remove_prob = 0.5
    g2 = DummyGirassol(3, 4, renderer)
    g2.remove_prob = 0.5
    g3 = DummyGirassol(5, 6, renderer)
    g3.remove_prob = 0.5

    world.girassois.extend([g1, g2, g3])

    import random
    random.seed(1)  # Garante que o teste seja determinístico
    world.sorteia_girassois()

    assert renderer.removed == [g1]
    assert world.girassois == [g2, g3]


def test_sorteia_colmeias_remove_com_probabilidade_1_e_deixa_com_0():
    world = World()
    renderer = DummyRenderer()
    c1 = DummyColmeia(1, 2, renderer)
    c1.remove_prob = 1
    c2 = DummyColmeia(3, 4, renderer)
    c2.remove_prob = 0

    world.colmeias.extend([c1, c2])

    world.sorteia_colmeias()

    assert renderer.removed == [c1]
    assert world.colmeias == [c2]


def test_sorteia_colmeias_remove_com_probabilidade_varias():
    world = World()
    renderer = DummyRenderer()
    c1 = DummyColmeia(1, 2, renderer)
    c1.remove_prob = 0.5
    c2 = DummyColmeia(3, 4, renderer)
    c2.remove_prob = 0.5
    c3 = DummyColmeia(5, 6, renderer)
    c3.remove_prob = 0.5

    world.colmeias.extend([c1, c2, c3])

    import random
    random.seed(1)  # Garante que o teste seja determinístico
    world.sorteia_colmeias()

    assert renderer.removed == [c1]
    assert world.colmeias == [c2, c3]


def test_solteia_girassois_e_colmeias_juntos():
    world = World()
    renderer = DummyRenderer()
    g1 = DummyGirassol(1, 2, renderer)
    c1 = DummyColmeia(1, 2, renderer)

    g2 = DummyGirassol(4, 2, renderer)
    c2 = DummyColmeia(4, 2, renderer)

    world.girassois.extend([g1, g2])
    world.colmeias.extend([c1, c2])

    import random
    random.seed(1)  # Garante que o teste seja determinístico
    world.sorteia_girassois_e_colmeias()

    assert renderer.removed == [c1, g2]
    assert world.girassois == [g1]
    assert world.colmeias == [c2]
