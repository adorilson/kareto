import turtle
import festa_dançante

dançarino_um = festa_dançante.cria_dançarino('turtle', 'Direita')
dançarino_dois = festa_dançante.cria_dançarino('turtle', 'Esquerda') 

turtle.onkey(dançarino_um.aleatório, 'Up') 
turtle.onkey(dançarino_dois.aleatório, 'Down')

"""
# Isso foi usado para gerar o gif sempre precisar usar as teclas
# o Peek gravando atrapalhava
import time
for _ in range(10):
    time.sleep(0.5)
    dançarino_dois.aleatório()
    time.sleep(0.5)
    dançarino_um.aleatório()
"""

turtle.mainloop()
