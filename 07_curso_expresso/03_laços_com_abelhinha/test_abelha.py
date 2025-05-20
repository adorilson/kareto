

def test_abelha_propriedades_publicas():
    bee = Abelha()
    assert bee.posicao == 0


def test_abelha_vire_oeste():
    bee = Abelha()
    bee.vire_oeste()
    assert bee.heading() == DIRECAO.OESTE
    assert bee.shape() == ABELHA_OESTE


def test_abelha_vire_norte():
    bee = Abelha()
    bee.vire_norte()
    assert bee.heading() == DIRECAO.NORTE
    assert bee.shape() == ABELHA_NORTE


def test_abelha_avance():
    bee = Abelha()
    bee.posicao = 10
    bee.vire_oeste()
    bee.avance()
    assert bee.posicao == 9