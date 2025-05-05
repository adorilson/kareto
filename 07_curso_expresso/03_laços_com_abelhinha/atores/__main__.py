import turtle

from atores import *

configurar_janela()
abelha = Abelha()
abelha.posicao = 0
abelha.atualize()
abelha.apareça()

for posicao in (7, 56, 63):
    flor = Girassol()
    flor.posicao = posicao
    flor.atualize()
    flor.apareça()

turtle.update()
turtle.mainloop()

