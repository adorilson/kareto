# Melhorando o código do editor

Se você observar as funções que fazem a troca de ```shape```, perceberá que
todas elas possuem apenas uma linha de código.

Python fornece um recurso que pode ser utilizando nesse caso, que são as funções
anônimas, definidas a partir da instrução ```lambda``` - por este motivo são 
também chamadas de funções lambda. 

O último trecho apresentado na seção anterior é o seguinte:

```python
def shape_square():
    shape = square

def shape_circle():
    shape = circle

from turtle import onkey, listen

onkey(shape_square, 's')
onkey(shape_circle, 'c')
listen()
```

Com uso de expressões lambda, as funções criadas com ```def``` serão eliminadas
e o código delas vai, juntamente com a instrução ```lambda```, para os locais
onde elas são referenciadas. O trecho de código então ficará:


```python
from turtle import onkey, listen

onkey(lambda: shape = square, 's')
onkey(lambda: shape = circle, 'c')
listen()
```

Observe que as definições das funções não existem mais, e ```lambda``` foi
usada na chamada à ```onkey```.

**Desafio** Aplique essa refatoração para as demais funções de troca de 
```shape```.

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
Python Games, uma coleção de jogos com fins de diversão e educação. Estão 
inclusas diversos jogos de arcade clássicos, que foram escritos em Python puro
e módulo ```turtle```, projetados para experimentação e mudanças.

## Referências

[Expressões lambda](https://docs.python.org/pt-br/3/tutorial/controlflow.html#lambda-expressions)

[Funções anônimas em Python](https://giovannireisnunes.wordpress.com/2018/08/03/funcoes-anonimas-em-python/)

[Anterior](05_criando_figuras.md) | [Próximo](06_melhorando_o_editor_.md)
