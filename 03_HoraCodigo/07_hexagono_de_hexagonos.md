# Hexágono de hexágonos

Faça 6 iterações no código abaixo do hexágono para criar um hexágono maior.
Quantos graus você terá que virar de cada vez? Dica: divida o número de graus
de um círculo pelo número de iterações que fizer.

```python
import turtle

esguicho = turtle.Turtle()

for _ in range(6):
    esguicho.forward(50)
    esguicho.right(60)
```

Não esqueça da identação.

## Figura a ser desenhada
![Hexágono de hexágonos](07_hexagono_de_hexagonos.png "Hexágono de hexágonos")

## Banco de instruções

```import turtle```

```esguicho = turtle.Turtle()```

```esguicho.forward(???)```

```esguicho.left(???)```

```esguicho.right(???)```

```for _ in range(???):```

[Anterior](06_flor_com_repeticao.md) | [Próximo](08_flor_com_funcao.md)
