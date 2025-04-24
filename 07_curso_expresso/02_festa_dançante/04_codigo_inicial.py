import turtle
import festa_dançante

dançarino_um = festa_dançante.cria_dançarino('Um', 'Direita')
dançarino_dois = festa_dançante.cria_dançarino('Dois', 'Esquerda') 

turtle.onkey(dançarino_um.aleatório, 'Up') 
turtle.onkey(None, 'Down')

turtle.mainloop()
