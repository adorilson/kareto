# ✨ Mais propriedades!

Na seção anterior, vimos que as **propriedades** de um dançarino controlam:

- Sua posição no palco,
- Seu tamanho,
- Sua rotação,
- E até sua cor!

Agora, vamos mergulhar um pouquinho mais fundo:
**Quais são os nomes reais dessas propriedades? E quais valores você pode usar?**


## 🎯 Movimento e posição
  - `setposition(???, ???)` - move a dançarina para uma posição **absoluta**
  no palco.

    O centro do palco é a posição `(0, 0)`, como em um
    **[plano cartesiano](https://pt.wikipedia.org/wiki/Sistema_de_coordenadas_cartesiano)**.
    - Primeiro argumento: **coordenada** `x` (horizontal) - aumenta para
    direita, diminui para a esquerda.
    - Segundo argumento: **coordenada** `y` (vertical) - aumenta para cima,
    diminui para baixo.

     O palco tem 500 x 500 pixels, então normalmente trabalhamos com valores
     entre **`-250`** e **`250`**. Se passar disso... a dançarina pode "cair" do
     palco.

  - `setx(???)` - move a dançarina só na horizontal (`x`).
  - `sety(???)` - move a dançarina só na vertical (`y`).
  - `setheading(???)` - define a direção que a dançarina está "olhando".
  
    Os ângulos mais comuns são:
     - `0` - leste (direita)
     - `90` - norte (cima)
     - `180` - oeste (esquerda)
     - `270` - sul (baixo)
  - `speed(???)` - define a velocidade da dançarina.
  
    Os valores válidos vão de `0` a `10`:
    - `0` - velocidade máxima (sem animação, a mudança é instantânea)
    - `10` - muito rápido
    - `6` - normal
    - `3 ` - lento
    - `1` - velocidade mínima (super devagar)

## 🎨 Aparência
  - `color(???)` - define **tanto** a cor de preenchimento **quanto** a cor da
  borda. A cor deve ser informada **em inglês**. Exemplos: `"red"`, `"blue"`,
  `"yellow"`.
  - `fillcolor(???)` - define **só** a cor de preenchimento (por dentro).
  - `pencolor(???)` - define **só** a cor da borda (contorno).
  - `shape(???)` - define a forma da dançarina.

    Os valores válidos são:
    - `"arrow"` (seta)
    - `"turtle"` (tartaruga)
    - `"circle"` (círculo)
    - `"square"` (quadrado)
    - `"triangle"` (triângulo)
    - `"classic"` (clássico). 
  - `shapesize(???)` - define o tamanho da dançarina. Quanto maior, maior fica
  a sua dançarina.

## Como usar essas propriedades?

Essas propriedades fazem parte do próprio módulo `turtle` — ou seja, você pode
usá-las tanto para as dançarinas da festa dançante, quanto para tartarugas
normais (`turtle.Turtle()`).

Quando você usa diretamente no objeto, é só usar o operador ponto `.`:

```python

principal_um = festa_dançante.cria_dançarina("Principal", "Esquerda")

principal_dois = festa_dançante.cria_dançarina("Principal", "Direita")

principal_um.color("yellow") # Deixa a primeira dançarina amarela
principal_dois.color("pink") # Deixa a segunda dançarina rosa
```

Mas na festa dançante você também pode usar a função de definição coletiva
para modificar várias de uma vez::

```python
festa_dançante.defina("Principal", "shapesize", 10)
```

Assim você altera todos os dançarinos com o papel "Principal" de uma vez só! 🎶✨

## Sua vez de praticar

Crie um palco com duas dançarinas principais e 10 dançarinas de apoio.
Depois, altere pelo menos duas propriedades de cada dançarina principal e das
dançarinas de apoio.


![Mais propriedades](09_mais_propriedades.gif "Mais propriedades")


## Caixa de ferramentas

`dançarino = festa_dançante.cria_dançarino("Principal", "Centro")`

`festa_dançante.cria_dançarinos_apoio(10, "Apoio", "Circulo")`

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

festa_dançante.cria_dançarino("Principal", "Centro")

festa_dançante.cria_dançarinos_apoio(10, "Apoio", "Circulo")

festa_dançante.defina("Principal", "color", "red")

festa_dançante.defina("Apoio", "color", "blue")

turtle.mainloop()

```


[Anterior](08_propriedades.md) | [Próximo](10_a_cada_compasso.md)
