import random
import pytest

from web.world import World, WorldError

class DummyAtor:
    def __init__(self, x=None, y=None, renderer=None):
        self.x = x if x is not None else random.randint(0, 8)
        self.y = y if y is not None else random.randint(0, 8)
        self.renderer = renderer

    def __repr__(self):
        return f'{self.__class__.__name__}({self.x}, {self.y})'

    @property
    def posicao(self):
        return self.x, self.y


class DummyGirassol(DummyAtor):
    def tem_nectar(self):
        return getattr(self, 'nectares', 0) > 0


def test_init_defaults():
    world = World()

    assert world.width == 8
    assert world.height == 8
    assert world.girassois == []
    assert world.colmeias == []
    assert world.nuvens == []
    assert world.abelha == None


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


class DummyColmeia(DummyAtor):
    pass


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


class DummyNuvem(DummyAtor):
    pass



def test_remove_nuvens_limpa_e_remove_do_renderer():
    world = World()
    renderer = DummyRenderer()
    nuvem1 = DummyNuvem(renderer=renderer)
    nuvem2 = DummyNuvem(renderer=renderer)

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


def test_sorteia_4_girassois_e_4_colmeias_com_nuvens():
    world = World()
    renderer = DummyRenderer()

    posicoes = [(4, 1), (7, 1), (7, 4), (4, 4)]
    for x, y in posicoes:
        g = DummyGirassol(x, y, renderer)
        g.remove_prob = 1
        world.girassois.append(g)

        c = DummyColmeia(x, y, renderer)
        c.remove_prob = 1
        world.colmeias.append(c)

        n = DummyNuvem(x, y, renderer)
        world.nuvens.append(n)

    assert len(world.girassois) + len(world.colmeias) == 8
    world.sorteia_girassois_e_colmeias()

    assert len(world.girassois) + len(world.colmeias) == 4
    assert len({gs.posicao for gs in world.girassois} | {c.posicao for c in world.colmeias}) == 4


def test_tem_nectar_no_girassol_retorna_true_quando_tem_nectar():
    world = World()
    g1 = DummyGirassol(1, 2)
    g1.nectares = 2
    world.girassois.append(g1)

    assert world.tem_nectar_no_girassol((1, 2)) is True


def test_tem_nectar_no_girassol_retorna_false_quando_nao_tem_nectar():
    world = World()
    g1 = DummyGirassol(1, 2)
    g1.nectares = 0
    world.girassois.append(g1)

    assert world.tem_nectar_no_girassol((1, 2)) is False

class DummyAbelha:
    pass

def test_tem_nectar_no_girassol_com_posicao_none():
    world = World()
    abelha = DummyAbelha()
    abelha.posicao = (1, 2)
    world.abelha = abelha
    g1 = DummyGirassol(1, 2)
    world.girassois.append(g1)

    g1.nectares = 1
    assert world.tem_nectar_no_girassol() is True

    g1.nectares = 0
    assert world.tem_nectar_no_girassol() is False
