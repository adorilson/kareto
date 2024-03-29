# Frente e fundo

Agora sabemos como alterar as propriedades de um(a) dançarino(a). Nós também
podemos fazer com que as mesmas propriedades respondam automaticamente a
algum evento. Veja a função abaixo:

```python
def para_frente():
    apoio_um.shapesize(5)
    apoio_dois.shapesize(5)
    turtle.ontimer(para_tras, 2000) 
```

Quando executada, ela aumenta o tamanho das duas dançarinas de apoio e depois
engatilha a função `para_tras` para ser executada em 2 segundos (2000
milissegundos).

Você deverá implementar a funções `para_frente`, conforme acima, e depois a
função `para_tras`, que deverá reduzir o tamanho das dançarinas para `3` e
engatilhar a função `para_frente` para ser executa também em 2 segundos.
Atende para os nomes das dançarinas no seu código.

Dessa forma, o tamanho das dançarinas serão alternadas a cada 2 segundos,
dando o efeito de irem para frente e para trás no palco.

Não esquece que será necessário dar o ponta-pé inicialmente a esse processo,
que deverá ser em 6 segundos.

## Resultado esperado
![Dançarina de apoio](09_frente_fundo.gif "Dançarina de apoio")

## Banco de instruções

```apoio = turtle.Turtle()```

```apoio.color(???)```

```apoio.shape(???)```

```apoio.shapesize(???)```

```apoio.setheading(???)```

```para_frente()```

```para_tras()```

```turtle.ontimer(???, ???)```

[Anterior](08_propriedades_cor.md) [Próxima](10_mais_eventos.md)
