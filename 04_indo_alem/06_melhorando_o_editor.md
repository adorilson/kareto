# Melhorando o código do editor

O último trecho apresentado na seção anterior é o seguinte:

```python
def shape_square():
    global shape
    shape = square

def shape_circle():
    global shape
    shape = circle

from turtle import onkey, listen, mainloop

onkey(shape_square, 's')
onkey(shape_circle, 'c')
listen()
mainloop()
```

Se você observar as funções que fazem a troca de ```shape```, perceberá que a única diferença é o valor atribuído a essa variável. Neste caso, podemos *refatorar* este código para termos apenas uma função (```change_shape```) que de fato faz a 
atribuição da variável ```shape```. Para tal, ela deverá possuir um parâmetro e na 
chamada da função é que faremos a distinção da figura. Assim:

```python
def change_shape(new_shape):
    global shape
    shape = new_shape

def shape_square():
    change_shape(square)

def shape_circle():
    change_shape(circle)

from turtle import onkey, listen, mainloop

onkey(shape_square, 's')
onkey(shape_circle, 'c')
listen()
mainloop()
```

Com isso, caso tenhamos que fazer alguma alteração (por exemplo, renomear ```shape```
para ```figure```) precisamos mexer em apenas uma função.  

**Desafio** Aplique essa refatoração para as demais funções de troca de 
```shape```.

Olhando novamente para os novos códigos das funções que fazem a troca de ```shape```,
perceberá que todas elas possum apenas uma linha de código.

Python fornece um recurso que pode ser utilizando nesse caso, que são as funções
anônimas, definidas a partir da instrução ```lambda``` - por este motivo são 
também chamadas de funções lambda. 

Com uso de expressões lambda, as funções criadas com ```def``` serão eliminadas
e o código delas vai, juntamente com a instrução ```lambda```, para os locais
onde elas são referenciadas. O trecho de código então ficará:


```python
def change_shape(new_shape):
    global shape
    shape = new_shape

# as funções que estavam aqui foram removidas

from turtle import onkey, listen, mainloop

onkey(lambda: change_shape(square), 's')
onkey(lambda: change_shape(circle), 'c')
listen()
mainloop()
```

Observe que as definições das funções não existem mais, e ```lambda``` foi
usada na chamada à ```onkey```.

**Desafio** Remova todas as funçoes de troca de ```shape```, utilizando ```lambda```
no lugar.

As funções lambda podem ser usadas sempre que objetos função forem necessários,
por exemplo quando você passa uma função como argumento de outra função. 
Eles são sintaticamente restritos a uma única expressão. Semanticamente, eles 
são apenas açúcar sintático para uma definição de função normal. Juntamente com 
os iteradores e os geradores são a base da programação funcional, um outro 
paradigma de programação com suporte de Python.

## Indo além com Free Python Games

Em termos de linguagem de programação e módulo ```turtle```, vimos uma visão 
geral de tudo que é necessário para o desenvolvimento de jogos com essa 
biblioteca. A partir disso, o grande desafio será definir as estruturas de dados
e algoritmos dos jogos. A medida que forem necessários, novos recursos de Python
e de ```turtle``` vão sendo estudados e aprendidos.

Por outro lado, começar um jogo do zero, por mais simples que ele seja, pode ser 
desafiador. Por este motivo, daremos continuidade ao nosso curso com o Free 
Python Games, uma coleção de jogos com fins de diversão e educação. 

## Referências

[Expressões lambda](https://docs.python.org/pt-br/3/tutorial/controlflow.html#lambda-expressions)

[Funções anônimas em Python](https://giovannireisnunes.wordpress.com/2018/08/03/funcoes-anonimas-em-python/)

[Anterior](05_criando_figuras.md) | [Próximo](/05_free_python_games/01_fpg_introducao.md)
