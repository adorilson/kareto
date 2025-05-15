import builtins
import time
import turtle

from atores import Abelha, Girassol, configurar_janela


def print(arg):
    """Função que encapsula um time.sleep"""
    builtins.print(arg)
    time.sleep(0.2)


configurar_janela()
bee = Abelha()
bee.posicao = 0
bee.atualize()
bee.apareça()


for posicao in (7, 56, 63):
    flor = Girassol()
    flor.posicao = posicao
    flor.atualize()
    flor.apareça()

print("Temos a Bee e 3 girassois nos cantos")

print("Bee vai andar 3 vezes para o leste")
for n in range(3):
    bee.avance()

print("Bee vai virar a direita")
bee.direita()

print("Bee vai andar 2 vezes para o sul")
for n in range(2):
    bee.avance()


print("E agora uma exceção porque a direção não está implementada")
bee.direita()


turtle.update()
turtle.mainloop()
