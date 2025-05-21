# tem que colocar o arquivo para fora de fase02,
# até resolver questão de import
import turtle

from fase01 import Abelha

maia = Abelha()

for _ in range(5):
    maia.avance()

turtle.mainloop()
