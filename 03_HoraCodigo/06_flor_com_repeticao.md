# Flor de diamantes com repetição

Observe abaixo como simplificamos o código do diamante, transformando-o em um
laço com a instrução ```for _ in range(???)```. Compare com o que você fez no
[exercício 02](02_diamante.md). Você pode fazer 12 iterações (uma para cada pétala
da flor) de toda a sequência para desenhar a flor.
Dica: você terá que virar 30 graus depois de iterar seu diamante para não continuar
desenhando o mesmo diamante todas as vezes.

```python
import turtle

esguicho = turtle.Turtle()

for _ in range(2):
    esguicho.forward(60)
    esguicho.left(30)
    esguicho.forward(60)
    esguicho.left(150)
```

Não esqueça da identação.

## Figura a ser desenhada
![Flor de diamantes](05_flor_diamante.png "Flor de diamantes")

## Banco de instruções

```import turtle```

```esguicho = turtle.Turtle()```

```esguicho.forward(???)```

```esguicho.left(???)```

```esguicho.right(???)```

```for _ in range(???):```


[Anterior](05_flor_diamante.md) | [Próximo](07_hexagono_de_hexagonos.md)
