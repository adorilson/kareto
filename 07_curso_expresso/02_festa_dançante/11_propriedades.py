# a partir do anterior
import turtle

import festa_dançante

festa_dançante.cria_dançarino('turtle', 'Centro')

festa_dançante.cria_dançarinos_apoio(10, 'turtle', 'Circulo')

turtle.ontimer(lambda: festa_dançante.defina('turtle', 'color', 'red'), 3000)

turtle.mainloop()