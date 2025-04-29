# 🕒 A cada compasso!

Já vimos como usar `turtle.ontimer(...)` para **executar uma função depois de
um certo tempo**. Porém, essa instrução tem uma limitação importante: **ele
executa a função só uma vez**.

Veja só:

```python
turtle.ontimer(muda_palco, 1000)
```

Essa linha vai esperar 1 segundo e **executar** `muda_palco()` **uma única
vez**. Se quisermos que isso aconteça de novo e de novo, teríamos que 
escrever mais código dentro da própria função — o que complica um pouco as 
coisas.

Foi por isso que `festa_dançante` ganhou um novo bloco especial:

```
festa_dançante.a_cada_compasso(???, ???)
```

Essa linha vai chamar a função pisca_luz a cada 3 segundos — simples assim!

O melhor de tudo é que não precisa alterar a função original, nem usar 
comandos avançados. O `festa_dançante` faz esse trabalho nos bastidores.

Esse tipo de evento baseado no tempo é perfeito para **ações que devem
acontecer em ritmo constante**, como efeitos visuais, movimentos repetidos
ou reações automáticas da sua coreografia.

Dá para imaginar várias ideias legais a partir disso, né?

Ao colocar os outros novos blocos na sua caixa de ferramentas dentro do
bloco de repetição, você pode alterar repetidamente as propriedades dos
dançarinos ao longo do tempo. Seja criativo e divirta-se!

Neste exemplo, estamos mudando o palco a cada 3 compassos.

![A cada compasso](10_a_cada_compasso.gif "A cada compasso")


## Caixa de ferramentas

`festa_dançante.muda_palco()`

`festa_dançante.a_cada_compasso(???, ???)`

`festa_dançante.defina(???, ???, ???)`

`dançarino.setposition(???)`

`dançarino.setx(???)`

`dançarino.sety(???)`

`dançarino.setheading(???)`

`dançarino.speed(???)`

`dançarino.color(???)`

`dançarino.fillcolor(???)`

`dançarino.pencolor(???)`

`dançarino.shape(???)`

`dançarino.shapesize(???)`

## Código inicial

```python
# a partir do anterior
import turtle

import festa_dançante

festa_dançante.muda_palco()

festa_dançante.cria_dançarino('Principal', 'Centro')

festa_dançante.cria_dançarinos_apoio(10, 'Apoio', 'Circulo')

festa_dançante.defina('Principal', 'color', 'red')

festa_dançante.defina('Apoio', 'color', 'blue')

turtle.mainloop()

```


[Anterior](08_propriedades.md) | [Próximo](09_mais_propriedades.md)
