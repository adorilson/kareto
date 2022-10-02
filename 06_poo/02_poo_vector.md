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
