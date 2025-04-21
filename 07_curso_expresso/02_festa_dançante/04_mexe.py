import turtle
import festa_dançante

dançarino = festa_dançante.cria_dançarino('turtle', 'Centro')

# exercicio
turtle.onkey(dançarino.anda_direita, 'Right') 
turtle.onkey(dançarino.anda_esquerda, 'Left')

turtle.mainloop()