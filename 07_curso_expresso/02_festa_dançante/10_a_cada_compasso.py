import turtle

import festa_dançante

d = festa_dançante.cria_dançarino('turtle', 'Centro')

festa_dançante.cria_dançarinos_apoio(10, 'turtle', 'Circulo')

festa_dançante.a_cada_compasso(festa_dançante.muda_palco, 3)

festa_dançante.a_cada_compasso(d.faz_rodopio, 5)

turtle.mainloop()
