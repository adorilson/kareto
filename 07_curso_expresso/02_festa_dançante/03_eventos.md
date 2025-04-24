# Eventos: dançando no ritmo!

Quando estamos numa festa de verdade, os passos de dança mudam conforme a música toca ou quando alguém faz um movimento novo na pista, certo? No mundo da programação, quem comanda esses momentos mágicos são os **eventos**.

## 🕺 O que são eventos?

Eventos são como sinais que o computador pode escutar e reagir imediatamente.
Eles dizem:
“Ei, algo aconteceu! Hora de agir!”

Alguns exemplos comuns de eventos:

- Alguém clicou com o mouse
- Uma tecla foi pressionada no teclado
- O tempo passou
- Um toque aconteceu na tela

## 💡 Como usamos isso na nossa festa dançante?

Você vai programar seu dançarino para reagir quando certas teclas forem
pressionadas. Por exemplo, apertou a seta para a direita? O dançarino gira!
Apertou pra frente? Ele avança com estilo!

```python
turtle.onkey(dançarino.anda_direita, "Right")
```

Essa linha tem um superpoder:
***"Quando alguém apertar a tecla de seta para a direita, execute o método
```anda_direita``` do meu dançarino."***

Repare em três detalhes importantes:

1. **Não colocamos os parênteses `()` no método.** Isso porque *ainda* não
queremos executá-lo — só queremos dizer ao programa qual ação tomar *quando* o
evento acontecer.
1. Estamos passando o nome do método como uma referência, e isso só funciona se ele for um chamável (como vimos em um Código Desvendado anterior).
1. `onkey` é uma função do módulo `turtle`, o que significa que é de uso geral,
não restrito a `festa_dançante`.

### 🛠️ E os nomes?

- O **nome do dançarino** é você quem escolhe, como `dançarino`, `bicho_solto`,
`michael`, `jackson` ou o que você quiser.
- Os **nomes dos métodos** vêm prontos no módulo `festa_dançante`, como:
  - `anda_direita`: move na horizontal para a direita
  - `anda_esquerda`: move na horizontal para a esquerda
  - `balança`: liga/desliga o balançar da dançarina
  - `move`: liga/desliga a movimentação para posições aleatórias do palco
  - `rodopia`: liga/desliga giros de 360º

Você pode conectar qualquer tecla a qualquer um desses movimentos usando `turtle.onkey`.
Aqui vão mais exemplos:

```python
turtle.onkey(dançarino.rodopia, "Up")
turtle.onkey(dançarino.move, "Down")
turtle.onkey(dançarino.anda_esquerda, "Left")
turtle.onkey(dançarino.anda_direita, "space")
```

🔠 Quando a tecla for uma letra, como "a", "b", ou "z", você pode escrevê-la
diretamente como string.

⚠️ Algumas teclas, como as setas ("Up", "Down", "Left", "Right") ou a barra de espaço ("space"), têm nomes especiais que você precisa escrever do jeito certo. O nome é sempre uma string sensível a maiúsculas e minúsculas — ou seja, "Up" é diferente de "up".

Abaixo, temos um palco com uma dançarina que dá passo de lado conforme as
teclas para direita e esquerda são pressionadas.

![Dançarina](03_eventos.gif "Dançarina")

## Caixa de ferramentas

`import turtle`

`import festa_dançante`

`dançarino = festa_dançante.cria_dançarino('Principal', 'Centro')`

`dançarino.anda_direita(???, ???)`

`dançarino.anda_esquerda(???, ???)`

`dançarino.balança()`

`dançarino.rodopia()`

`dançarino.move()`

`turtle.onkey(???, ???)`

`turtle.mainloop()`

## Código inicial

```python
import turtle
import festa_dançante

dançarino = festa_dançante.cria_dançarino('Principal', 'Centro')



turtle.mainloop()
```

[Anterior](02_cria_dançarino.md) | [Próximo](04_dois_dançarinos.md)
