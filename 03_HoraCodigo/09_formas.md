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

esguicho = turtle.Turtle()

# definindo as funções
def desenhe_forma():
    for _ in range(6):
        esguicho.forward(25)
        esguicho.right(60)

def pule(pixels):
    esguicho.penup()
    esguicho.forward(pixels)
    esguicho.pendown()


# Aqui é o código principal
for _ in range(6):
    for _ in range(2):
        for _ in range(4):
            desenhe_forma()
            pule(75)
        pule(-25)
        esguicho.right(60)
        pule(25)
        esguicho.right(120)
    pule(-25)
    esguicho.left(60)
    pule(50)
    esguicho.right(60)

```

Em um primeiro momento, apenas crie as novas funções com os lados das figuras
iguais aos do hexágono. Posteriormente, altere essas dimensões e os saltos
executados no código principal. Observe as mudanças nos padrões desenhados.

## Banco de instruções

```import turtle```

```esguicho = turtle.Turtle()```

```esguicho.forward(???)```

```esguicho.left(???)```

```esguicho.right(???)```

```esguicho.penup()```

```esguicho.pendown()```

```for _ in range(???):```

```desenhe_forma()```

```pule(???)```

[Anterior](08_flor_com_funcao.md) | [Próximo](10_sua_vez.md)
