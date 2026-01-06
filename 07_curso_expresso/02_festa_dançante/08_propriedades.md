# ✨ Deixando seu Dançarino Único: Propriedades!

Até agora, você já programou vários tipos de dançarinos e criou passos de
dança supercriativos. Mas já parou para pensar: **como esses movimentos
realmente funcionam?** 🕺💃

O segredo está nas **animações**: cada passo é feito de uma sequência de
imagens, chamadas **frames**. Cada frame mostra o dançarino numa posição um
pouquinho diferente. Quando o programa exibe esses frames bem rapidinho,
parece que o dançarino está se mexendo de verdade. É assim que qualquer
animação acontece — seja em games, filmes ou... na sua pista de dança! 🎥🎮

Mas não é só nos movimentos que você pode mandar! Você também pode mudar as
- **propriedades** dos seus dançarinos para deixá-los ainda mais estilosos.

As **propriedades** controlam coisas como:

- A posição do dançarino na tela,
- O tamanho dele,
- A rotação,
- E até a cor que ele está usando!

Para fazer isso, você vai usar um **bloco de definição**: um jeito de dizer ao programa como deve ser a nova aparência do dançarino.

## 🎨 Personalizando seu dançarino

Depois de colocar dançarinos no palco com os blocos `cria_dançarino` ou `cria_dançarino_apoio`, você poderá utilizar o novo bloco de definição:

```python
festa_dançante.defina("Principal", "color", "red"))
```
- o primeiro argumento (`"Principal"`) é o **tipo** do dançarino que você usou
na criação. Este valor vai depender do valor que você usou na criação dos
dançarinos.
- o segundo (`"color"`) é a **propriedade** que você quer definir. O valor
deste argumento é predefinido no módulo `turtle`, veremos mais valores depois.
- e o terceiro é o **novo valor** da propriedade. Os valores aqui dependem
do propriedade sendo definida. Por exemplo, se for `"color"` será o nome
de uma cor em inglês, já para `"shapesize"`, que define o tamanho do dançarino,
será um número maior que zero.

Veremos outras propriedades possíveis no próximo passo.


## 💃 Sua vez de praticar

Agora, defina `"color"` do seu dançarino principal e do apoio para cores
diferentes. Atente que isso deverá ser feita em duas instruções.

![Propriedades](08_propriedades.gif "Propriedades")


## 🧰 Caixa de ferramentas

`dançarino = festa_dançante.cria_dançarino("Principal", "Centro")`

`festa_dançante.cria_dançarinos_apoio(10, "Apoio", "Circulo")`

`festa_dançante.muda_palco()`

`festa_dançante.defina("Principal", "color", "red")`

`festa_dançante.defina("Apoio", "color", "blue")`


## 💻 Código inicial

```python
# a partir do anterior
import turtle

import festa_dançante

festa_dançante.muda_palco()

festa_dançante.cria_dançarino("Principal", "Centro")

festa_dançante.cria_dançarinos_apoio(10, "Apoio", "Circulo")

turtle.mainloop()

```


[Anterior](07_grupo_dançarinos.md) | [Próximo](09_mais_propriedades.md)
