import turtle

import festa_dançante

d = festa_dançante.cria_dançarino("Principal", "Centro")

festa_dançante.cria_dançarinos_apoio(10, "Apoio", "Circulo")

# Essa linha abaixo está comentada para não dar erro de sintaxe
#festa_dançante.a_cada_compasso(???, ???)

# Comece removendo o # do inicio dela e depois alterando os ???
# pelos valores dos argumentos. Então acrescente outras chamadas
# a a_cada_compasso para alterar outras propriedades das dançarinas 

turtle.mainloop()
