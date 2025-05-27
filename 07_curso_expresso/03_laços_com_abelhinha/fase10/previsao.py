
import turtle

from fase10 import Abelha


maia = Abelha()

for _ in range(2):
    maia.avance()

maia.esquerda()
for _ in range(3):
    maia.avance()

maia.direita()
for _ in range(3):
    maia.avance()

maia.esquerda()
for _ in range(3):
    maia.avance()

turtle.mainloop()

