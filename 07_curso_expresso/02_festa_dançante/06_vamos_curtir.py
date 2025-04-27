# a partir do anterior
import turtle

import festa_dançante

dançarino = festa_dançante.cria_dançarino('turtle', 'Centro')

turtle.ontimer(dançarino.faz_rodopio, 4000)

turtle.ontimer(dançarino.move, 6000)

turtle.mainloop()