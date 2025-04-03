# Código desvendado

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

[Anterior](03_L_invertido.md) | [Próximo](04_quadrado.md)
