import turtle
import festa_dançante

import time
time.sleep(1)

dançarino = festa_dançante.cria_dançarino('turtle', 'Centro')

# exercicio
turtle.onkey(dançarino.anda_direita, 'Right') 
turtle.onkey(dançarino.anda_esquerda, 'Left')

turtle.mainloop()