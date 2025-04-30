# a partir do anterior
import turtle

import festa_dançante

festa_dançante.muda_palco()

festa_dançante.cria_dançarino("Principal", "Centro")

festa_dançante.cria_dançarinos_apoio(10, "Apoio", "Circulo")

festa_dançante.defina("Principal", "color", "red")

festa_dançante.defina("Apoio", "color", "blue")

turtle.mainloop()
