import turtle
from fase04 import Abelha

bee = Abelha()

## Seu código a partir aqui

for n in range(4):
    bee.avance()

bee.direita()

for n in range(5):
    bee.avance()
 
# Fim do seu código aqui

turtle.mainloop()
