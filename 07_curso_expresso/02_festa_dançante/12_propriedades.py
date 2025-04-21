# a partir do anterior
import turtle

import festa_dançante

festa_dançante.cria_dançarino('turtle', 'Centro')

festa_dançante.cria_dançarinos_apoio(10, 'turtle', 'Circulo')

turtle.ontimer(lambda: festa_dançante.defina('turtle', 'fillcolor', 'red'), 3000)
# TODO definir melhor propriedades para uso
turtle.ontimer(lambda: festa_dançante.defina('turtle', 'pencolor', 'blue'), 3000)

turtle.mainloop()