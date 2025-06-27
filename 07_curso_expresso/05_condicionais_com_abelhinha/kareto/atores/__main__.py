import builtins
import time
import turtle

from atores import Abelha, Girassol, configurar_janela


def print(arg):
    """Função que encapsula um time.sleep"""
    builtins.print(arg)
    time.sleep(0.2)


configurar_janela()
maia = Abelha()
maia.posição = 0
maia.atualize()
maia.apareça()


for posicao in (7, 56, 63):
    flor = Girassol()
    flor.posicao = posicao
    flor.atualize()
    flor.apareça()

print("Temos a Maia e 3 girassois nos cantos")

print("Maia vai andar 3 vezes para o leste")
for n in range(3):
    maia.avance()

print("Maia vai virar a direita")
maia.direita()

print("Maia vai andar 2 vezes para o sul")
for n in range(2):
    maia.avance()


print("E agora uma exceção porque a direção não está implementada")
maia.direita()


turtle.update()
turtle.mainloop()
