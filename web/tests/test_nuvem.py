from web.entities import Nuvem, NuvemPequena


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


def test_nuvem_init_registra_e_define_shape_e_zindex():
    world = DummyWorld()
    renderer = DummyRenderer()
    queue = []

    nuvem = Nuvem(world, renderer, queue, x=2, y=1)

    assert renderer.registered == [nuvem]
    assert nuvem.shape() == Nuvem.NUVEM
    assert nuvem.z_index == 2
    assert nuvem.IMAGE_SIZE == (140, 140)


def test_nuvem_pequena_init_registra_e_define_shape_e_zindex():
    world = DummyWorld()
    renderer = DummyRenderer()
    queue = []

    nuvem_pequena = NuvemPequena(world, renderer, queue, x=2, y=1)

    assert renderer.registered == [nuvem_pequena]
    assert nuvem_pequena.shape() == Nuvem.NUVEM
    assert nuvem_pequena.z_index == 2
    assert nuvem_pequena.IMAGE_SIZE == (40, 40)
