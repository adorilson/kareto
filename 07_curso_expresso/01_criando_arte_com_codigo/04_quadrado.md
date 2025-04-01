# Completando o quadrado

Vamos agora completar o quadrado e conhecer mais alguns detalhes do código
inicial.

Primeiro, vamos fazer um quadrado simples usando as instruções
```artista.right(90)``` (ou ```artista.left(90)```) e
```artista.forward(100)```. Cada lado deve medir 100 pixels e todos os ângulos
são de 90 graus.

![Quadrado](04_quadrado.gif "Quadrado")


## Explicação sobre o código inicial

A instrução `import turtle` informa ao Python que carregue o módulo `turtle`
para que possamos usá-lo. No Python, *módulos* são coleções de funções e
classes que ajudam a organizar e reutilizar código. No caso do módulo `turtle`,
é onde estão definidas a classe `Turtle` e a função `mainloop`, por exemplo.
Já `import` é uma palavra reservada, ou seja, um comando próprio da linguagem
que não pode ser usado para outro fim.

A linha `artista = turtle.Turtle()` cria um *objeto* da classe `Turtle` e o
associa (com o operador `=`) à variável `artista`. Em programação, uma
*classe* é um modelo que define características e comportamentos de um
conjunto de elementos semelhantes. Já um *objeto* é uma instância concreta de
uma classe, ou seja, um elemento criado a partir desse modelo. A *variável*
`artista` serve como um nome para acessar esse objeto e interagir com ele no
programa.

No código, o nome da variável pode ser alterado conforme necessário. Na
*Caixa de ferramentas*, usamos `artista`, mas qualquer outro nome válido pode
ser utilizado para representar o objeto. Você pode, por exemplo, chamar a sua
artista de `tarsila_do_amaral`. Porém, é importante que seja um nome intuitivo.

Note que `Turtle` (classe) começa com letra maiúscula, enquanto `turtle`
(módulo) começa com minúscula. Essa é uma convenção do Python: nomes de
classes começam com letra maiúscula, enquanto módulos e variáveis usam
minúsculas. Além disso, Python diferencia maiúsculas de minúsculas, então
`turtle` e `Turtle` são nomes distintos. Muita atenção com isso.

Por fim, a instrução `turtle.mainloop()` mantém a janela aberta após a
execução do código. *Funções* como `mainloop` são blocos de código prontos que
realizam uma ação específica. Neste caso, `turtle.mainloop()` faz com que o
programa continue rodando e exibindo a janela gráfica até que o usuário a
feche. Ela deve ser a última linha de qualquer programa que utilize o módulo
`turtle`.


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


[Anterior](03_L_invertido.md) | [Próximo](05_triangulo.md)
