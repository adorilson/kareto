import turtle
from fase13 import Abelha

maia = Abelha()

## Seu código a partir daqui
maia.avance()
for n in range(2):
    maia.avance()
    maia.obtenha_nectar()

maia.direita()

maia.avance()
for n in range(2):
    maia.avance()
    maia.obtenha_nectar()

maia.direita()

maia.avance()
for n in range(2):
    maia.avance()
    maia.obtenha_nectar()

maia.direita()

# Fim do seu código aqui

turtle.mainloop()