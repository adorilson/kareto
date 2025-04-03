# Completando o quadrado

Vamos agora completar o quadrado e conhecer mais alguns detalhes do código
inicial.

Primeiro, vamos fazer um quadrado simples usando as instruções
```artista.right(90)``` (ou ```artista.left(90)```) e
```artista.forward(100)```. Cada lado deve medir 100 pixels e todos os ângulos
são de 90 graus.

![Quadrado](04_quadrado.gif "Quadrado")


## Caixa de ferramentas

```import turtle```

```artista = turtle.Turtle()```

```artista.shape('turtle')```

```artista.forward(100)```

```artista.left(90)```

```artista.right(90)```

```turtle.mainloop()```


## Código inicial

Copie e cole no seu editor, salve o arquivo e execute antes de fazer qualquer 
alteração.

```python

import turtle

artista = turtle.Turtle()
artista.shape('turtle')

artista.forward(100)
artista.right(90)

## Seu código a partir daqui




# Instrução necessária para que a janela não se feche
turtle.mainloop()

```


[Anterior](03a_codigo_desvendado.md) | [Próximo](05_triangulo.md)
