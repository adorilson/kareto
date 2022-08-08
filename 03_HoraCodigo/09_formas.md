# Formas

Temos agora uma função chamada ```desenhe_forma()```, que programamos para
desenhar hexágonos. Execute o código para ver o que ele faz e, em seguida,
tente usá-lo com a função para ver o que acontece. Você consegue fazer com que
ela desenhe um padrão de quadrados, triângulos ou octógonos? Ou melhor, crie
novas funções para essas figuras.

Também criamos uma nova função ```pule(???)``` para facilitar a ação de pular,
incluindo pular para trás. Basta indicar um número negativo.

```python
import turtle

turtle = turtle.Turtle()

# definindo as funções
def desenhe_forma():
    for _ in range(6):
        turtle.forward(25)
        turtle.right(60)

def pule(pixels):
    turtle.penup()
    turtle.forward(pixels)
    turtle.pendown()


# Aqui é o código principal
for _ in range(6):
    for _ in range(2):
        for _ in range(4):
            desenhe_forma()
            pule(75)
        pule(-25)
        turtle.right(60)
        pule(25)
        turtle.right(120)
    pule(-25)
    turtle.left(60)
    pule(50)
    turtle.right(60)

```

Em um primeiro momento, apenas crie as novas funções com os lados das figuras
iguais aos do hexágono. Posteriormente, altere essas dimensões e os saltos
executados no código principal. Observe as mudanças nos padrões desenhados.

## Banco de instruções

```import turtle```

```turtle = turtle.Turtle()```

```turtle.forward(???)```

```turtle.left(???)```

```turtle.right(???)```

```turtle.penup()```

```turtle.pendown()```

```for _ in range(???):```

```desenhe_forma()```

```pule(???)```

[Anterior](08_flor_com_funcao.md) | [Próximo](10_sua_vez.md)
