import pytest

from atores import Abelha, DIRECAO, ABELHA_LESTE, ABELHA_OESTE, ABELHA_NORTE, ABELHA_SUL


@pytest.fixture
def bee():
    return Abelha()

def test_abelha_propriedades_publicas(bee):
    assert bee.posicao == 0


def test_abelha_vire_oeste(bee):
    bee.vire_oeste()
    assert bee.heading() == DIRECAO.OESTE
    assert bee.shape() == ABELHA_OESTE


def test_abelha_vire_norte(bee):
    bee.vire_norte()
    assert bee.heading() == DIRECAO.NORTE
    assert bee.shape() == ABELHA_NORTE


def test_abelha_vire_leste(bee):
    bee.vire_leste()
    assert bee.heading() == DIRECAO.LESTE
    assert bee.shape() == ABELHA_LESTE


def test_abelha_avance(bee):
    bee.posicao = 10

    bee.vire_oeste()
    bee.avance()
    assert bee.posicao == 9

    bee.vire_norte()
    bee.avance()
    assert bee.posicao == 1


def test_abelha_direita(bee):
    bee.vire_oeste()

    bee.direita()
    assert bee.heading() == DIRECAO.NORTE
    assert bee.shape() == ABELHA_NORTE

    bee.direita()
    assert bee.heading() == DIRECAO.LESTE
    assert bee.shape() == ABELHA_LESTE

    bee.direita()
    assert bee.heading() == DIRECAO.SUL
    assert bee.shape() == ABELHA_SUL

    bee.direita()
    assert bee.heading() == DIRECAO.OESTE
    assert bee.shape() == ABELHA_OESTE
