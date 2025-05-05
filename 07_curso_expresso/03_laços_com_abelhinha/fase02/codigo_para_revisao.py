# tem que colocar o arquivo para fora de fase02,
# até resolver questão de import
import turtle
from fase01 import Abelha

bee = Abelha()

for _ in range(5):
    bee.avance()

turtle.mainloop()
