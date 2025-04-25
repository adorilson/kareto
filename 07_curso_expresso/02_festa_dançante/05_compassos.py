import turtle

import festa_dançante

dançarino = festa_dançante.cria_dançarino('Principal', 'Centro')

# Por causa do None, isso vai gerar um comportamente estranho de
# congelar a execução, mas não ocorre erro de execução
turtle.ontimer(dançarino.faz_rodopio, 4000)  
 

turtle.mainloop()