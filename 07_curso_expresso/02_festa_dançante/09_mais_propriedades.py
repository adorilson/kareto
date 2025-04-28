# a partir do anterior
import turtle

import festa_dançante

um = festa_dançante.cria_dançarino('Principal', 'Centro')
um.setx(-50)
um.color('pink')

dois = festa_dançante.cria_dançarino('Principal', 'Centro')
dois.setx(50)
dois.color('yellow')

festa_dançante.cria_dançarinos_apoio(10, 'Apoio', 'Circulo')
festa_dançante.defina('Apoio', 'fillcolor', 'red')
festa_dançante.defina('Apoio', 'pencolor', 'blue')

turtle.mainloop()