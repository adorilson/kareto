import turtle

import festa_dançante

dançarino_um = festa_dançante.cria_dançarino('turtle', 'Direita')
dançarino_dois = festa_dançante.cria_dançarino('turtle', 'Esquerda') 

turtle.onkey(dançarino_um.anda_direita, 'Right') 
turtle.onkey(dançarino_um.anda_esquerda, 'Left')

turtle.onkey(dançarino_dois.anda_direita, 'a') 
turtle.onkey(dançarino_dois.anda_esquerda, 'd')


turtle.mainloop()