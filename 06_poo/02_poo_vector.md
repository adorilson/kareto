# Reconstruindo a classe vector

No tópico sobre a biblioteca `freegames`, tomamos conhecimento sobre a classe
`vector`. Criamos objetos dessa classe e executamos vários métodos. Iremos
agora fazer uma reconstrução de uma versão simplificada dessa classe.

A forma mais simples para definir uma classe é a seguinte:

```python
class NomeDaClasse:
    <instrucao-1>
    .
    .
    .
    <instrucao-N>
```

Portanto, para definir uma classe mínima `vector`, podemos fazer:

```python
class vector:
    pass
```

Crie um novo arquivo com este código e salve com o nome `vectors.py`. No caso
de Python, o nome do arquivo é arbitrário, não havendo nenhum relação sintática 
definida pela linguagem. Escolhemos este nome para indicar que ele contém código
relacionado à manipulação de vetores.

Com isso, já podemos criar objetos dessa classe. No contexto de classes, chamamos
a criação de objetos de **instanciação**. Para _instanciar_ uma classe, usa-se a 
mesma sintaxe de invocar uma função. Apenas finja que você definiu uma função o
sem parâmetros com o mesmo nome da classe, que devolve uma nova instância da
classe. Então, assumindo a classe `vector acima, execute o trecho de código abaixo::

```python
>>> from vectors import vector
>>> v = vector()
>>> v
<vectors.vector object at 0x7fdbf6feb490>
>>> type(v)
<class 'vectors.vector'>
```

Para que o `import` funcione corretamente é necessário que o interpretador Python
seja executado a partir do diretório que contém o arquivo. Caso você esteja 
utilizando o IDLE (ou algum outro ambiente) também pode executar o arquivo
`vectors.py` a partir dele e executar os comandos no intenpretador.

Após criar o objeto `v`,
podemos ver a sua representação textual simplesmente digitando o nome da variável
no interpretador e pressionando a tecla `enter`. Como resultado, temos a informação
que `v` é um 
objeto da classe `vector` e a que a classe veio do módulo `vectors`, e qual o 
endereço de memória `v` está. A classe do objeto também pode ser obtida com a
função embutida `type`.

Observamos na chamada a `vector()` que não passamos nenhum argumento. Veja o que aconteceria se fizesse isso:

```python
>>> v = vector(3, 4)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: vector() takes no arguments
```

## Inicialização do objeto

A operação de instanciação (“invocar” um objeto classe) cria um objeto vazio. Muitas classes preferem criar novos objetos com um estado inicial predeterminado. Para tanto, a classe pode definir um método especial chamado `__init__` (lê-se dunder init, e vem de initilization - inicialização em inglês), assim:

```python
def __init__(self):
    self.dados = []
```

Quando este método é definido em uma classe, ele é automaticamente invocado pelo
processo de iniciação para a instância recém criada. Naturalmente,  `__init__` pode
ter parâmetros, assim o objeto poderá ser criado com valores indicados na chamado.
Por exemplo, para que seja possível já criar um `vector` com valores de atributos
`x` e  `y` podemos acrescentar um método `__init__` que receba argumentos, assim:

```python
class vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
```

Podemos agora passar argumentos na criação do objeto:  

```python
>>> from vectors import vector
>>> v = vector(3, 4)
>>> v.x
3
>>> v.y
4
>>> v
<vectors.vector object at 0x7fdbf6feb490>
>>> type(v)
<class 'vectors.vector'>
```

Observe que além definir parâmetros para o método, é necessário programar
como eles serão utilizados. Note ainda que além dos parâmetros `x` e `y` existe 
ainda um terceiro, que é o `self`.  Este parâmetro representa o próprio objeto
e não precisa ser passado na chamada. Nas duas linhas seguintes está sendo dito,
com o `self`, que o objeto `vector` sendo criado terá um atributo `x` cujo valor 
será o parâmetro `x` e outro atributo `y`, cujo valor será o parâmetro `y`. 

Por isso, pudemos acessá-los nas duas linhas seguintes. Os nomes dos parâmetros
do método e dos atributos dos objetos não precisam ser os mesmos, mas comumente
o são. 

## Representação textual do objeto

Contudo, quando colocamos apenas o nome da variável, a representação textual
continua não sendo muito útil, por exemplo apresentando os valores das
coordenadas em um formato `(x, y)`. Isso deve ser programado em outro método
especial, o `__repr__` (lê-se dunder repr, e vem de representation -
representação em inglês), assim:

```python
class vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f'({self.x}, {self.y})'
```

Observe que na definição de uma classe, a referência ao objeto é sempre
através do parâmetro `self` dos métodos.

```python
>>> from vectors import vector
>>> v = vector(3, 4)
>>> v.x
3
>>> v.y
4
>>> v
(3, 4)
>>> type(v)
<class 'vectors.vector'>
```

## Métodos especiais

Com a implementação dos dois métodos especiais acima, talvez você esteja
suspeitando que tais métodos são importantes. E, de fato, são. Em Python,
esses métodos especiais são parte central do modelo de dados da linguagem.
Embora possa parecer feio quando você os escreve nas classes, observe que
eles foram executados não por você, mas pelo próprio interpretador, de forma
transparente para o usuário do objeto. E essa é a finalidade de tais métodos:
ser executados pelo Python. Isso torna a utilização de objetos
limpa e concisa.

## Adição de vetores

Como vimos em seções anteriores, uma operação envolvendo vetores é a adição.
O operador comum para adição é `+`, portanto é de se esperar que possamos 
fazer  `v1 + v2`, e ter como resultado um 3º vetor que é o resultado da soma.
Veja abaixo o que acontece quando você faz essa operação:

```python
>>> from vectors import vector
>>> v1 = vector(3, 4)
>>> v2 = vector(1, 3)
>>> v1 + v2 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'vector' and 'vector'
```

Veja a última linha: `TypeError: unsupported operand type(s) for +: 'vector' and 
'vector'`. Ou seja, não existe suporte para o operador `+` envolvendo dois objetos
`vector`.

Esse suporte é também adicionado com um método especial: `__add__`. Pela regra de 
adição de vetores, basta que sejam somados os coordenadas `x` e `y` de cada vetor.

```python
...
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return vector(x, y)
```

Com a inclusão desse método, será possível utilizar o operador `+` com dois
vetores:

```python
>>> from vectors import vector
>>> v1 = vector(3, 4)
>>> v2 = vector(1, 3)
>>> v1 + v2 
(4, 7)
```

O resultado apresentado após a operação (`(4, 7)`) é justamente o retorno do
método `__repr__` do vetor criado como resultado da operação, conforme definimos
anteriormente. Assim, isso não é o objeto em si, é apenas sua representação
textual. Naturalmente, o resultado da operação pode ser atribuída a uma nova 
variável, e o tipo dela ser verificado:

```python
>>> v3 = v1 + v2 
>>> type(v3)
<class 'vectors.vector'>
```

## Movimento de vetores

Outra operação possível com vetores, e extremamente útil quando o vetor 
representa a posição de um elemento em um jogo, é a movimentação do vetor.

A movimentação do vetor é bastante similar a operação de soma, no sentido de que 
as coordenadas de dois vetores serão somadas, porém haverá uma mudança no **estado** do vetor, e não a criação de outro vetor. Assim, acrescente à
classe o método abaixo:

```python
...
    def move(self, other):
        self.x = self.x + other.x
        self.y = self.y + other.y
```

Assim, para mover um vetor, basta chamar o método `move` passando como parâmetro
um outro vetor.

```python
>>> from vectors import vector
>>> v1 = vector(3, 4)
>>> v2 = vector(1, 3)
>>> v1.move(v2) 
>>> v1
(4, 7)
```

Observe que não houve um retorno na execução do método `move`, porém as 
coordenadas do vetor `v1` foram somadas às coordenadas do vetor `v2`.

Em um contexto de jogos, poderemos ter vetores de referências que serão 
utilizados quando quisermos mover algum elemento do jogo para esquerda, direita, 
cima e baixo. 


```python
>>> from vectors import vector
>>> direita = vector(1, 0)
>>> esquerda = vector(-1, 0)
>>> cima = vector(0, 1)
>>> baixo = vector(0, -1)
>>> v = vector(3, 1)
>>> v.move(direita)
>>> v
(4, 1)
>>> v.move(cima)
>>> v
(4, 2)
>>> v.move(esquerda)
>>> v
(3, 2)
>>> v.move(baixo)
>>> v
(3, 1)
```

[Anterior](01_poo_introducao.md) | [Próximo](03_poo_encapsulamento.md)
