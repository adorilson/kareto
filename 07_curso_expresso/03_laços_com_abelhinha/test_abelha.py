from atores import Abelha, DIRECAO, ABELHA_OESTE


def test_abelha_vire_oeste():
    bee = Abelha()
    bee.vire_oeste()
    assert bee.heading() == DIRECAO.OESTE
    assert bee.shape() == ABELHA_OESTE
