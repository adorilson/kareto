import pytest

from atores import Abelha, DIRECAO, ABELHA_LESTE, ABELHA_OESTE, ABELHA_NORTE, ABELHA_SUL


@pytest.fixture
def maia():
    return Abelha()

def test_abelha_propriedades_publicas(maia):
    assert maia.posicao == 0


def test_abelha_vire_oeste(maia):
    maia.vire_oeste()
    assert maia.heading() == DIRECAO.OESTE
    assert maia.shape() == ABELHA_OESTE


def test_abelha_vire_norte(maia):
    maia.vire_norte()
    assert maia.heading() == DIRECAO.NORTE
    assert maia.shape() == ABELHA_NORTE


def test_abelha_vire_leste(maia):
    maia.vire_leste()
    assert maia.heading() == DIRECAO.LESTE
    assert maia.shape() == ABELHA_LESTE


def test_abelha_avance(maia):
    maia.posicao = 10

    maia.vire_oeste()
    maia.avance()
    assert maia.posicao == 9

    maia.vire_norte()
    maia.avance()
    assert maia.posicao == 1


def test_abelha_direita(maia):
    maia.vire_oeste()

    maia.direita()
    assert maia.heading() == DIRECAO.NORTE
    assert maia.shape() == ABELHA_NORTE

    maia.direita()
    assert maia.heading() == DIRECAO.LESTE
    assert maia.shape() == ABELHA_LESTE

    maia.direita()
    assert maia.heading() == DIRECAO.SUL
    assert maia.shape() == ABELHA_SUL

    maia.direita()
    assert maia.heading() == DIRECAO.OESTE
    assert maia.shape() == ABELHA_OESTE


def test_abelha_esquerda(maia):
    maia.vire_oeste()

    maia.esquerda()
    assert maia.heading() == DIRECAO.SUL
    assert maia.shape() == ABELHA_SUL

    maia.esquerda()
    assert maia.heading() == DIRECAO.LESTE
    assert maia.shape() == ABELHA_LESTE

    maia.esquerda()
    assert maia.heading() == DIRECAO.NORTE
    assert maia.shape() == ABELHA_NORTE

    maia.esquerda()
    assert maia.heading() == DIRECAO.OESTE
    assert maia.shape() == ABELHA_OESTE


def test_abelha_vire_para(maia):
    maia.vire_para(DIRECAO.SUL)
    assert maia.heading() == DIRECAO.SUL
    assert maia.shape() == ABELHA_SUL

    maia.vire_para(DIRECAO.OESTE)
    assert maia.heading() == DIRECAO.OESTE
    assert maia.shape() == ABELHA_OESTE

    maia.vire_para(DIRECAO.NORTE)
    assert maia.heading() == DIRECAO.NORTE
    assert maia.shape() == ABELHA_NORTE

    maia.vire_para(DIRECAO.LESTE)
    assert maia.heading() == DIRECAO.LESTE
    assert maia.shape() == ABELHA_LESTE
