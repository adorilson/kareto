# Coletando néctar

Por enquanto, **Bee** tem apenas um comando: `avance()`, que faz com que ela
avance para frente. Diferente do comando `forward()` da tartaruga, este
comando não recebe argumentos e a abelhinha avança exatamente um quadradinho
no seu mundo a cada vez que que ela recebe essa mensagem.


## Sua vez de praticar

Faça a abelhinha avançar por todas as flores. Aqui, não é preciso
comando específico para a coleta do néctar. Basta a abelha chegar até a flor
para o néctar ser colhido e a flor desaparecer.


![Coletando néctar](cenario_01.png "Coletando néctar")


## Caixa de ferramentas

`import turtle`

`import fase01`

`bee = fase01.Abelha()`

`bee.avance()`

`turtle.mainloop()`


## Código inicial

```python
import turtle
from fase01.fase01 import Abelha

bee = Abelha()

## Seu código a partir aqui



# Fim do seu código aqui

turtle.mainloop()

```

[Anterior](../README.md) | [Próximo](fase01/README.md)