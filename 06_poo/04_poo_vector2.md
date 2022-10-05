# Reconstruindo a classe vector - Parte 2

Nas seções anteriores, começamos a reconstrução da classe `vector`.
Se você seguiu as instruções corretamente, deverá ter algo parecido com:

```python
class vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f'({self.x}, {self.y})'

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return vector(x, y)

    def move(self, other):
        self.x = self.x + other.x
        self.y = self.y + other.y
```

Implemente agora os demais métodos de `vector`, de forma que a classe
ofereça suporte para as operações seguintes (algumas já implementadas, podendo
ter que serem alteradas ou não). Utilize as simulações de sessões do 
interpretador para testar suas implementações. Começaremos pelo métodos especiais
previsto na linguagem, e cujo comportamento irá se repetir em muitos e muitas
classes, trazendo consistência para manipulação de objetos de classes distintas. 
Posteriormente, criaremos métodos específicos para manipulação de vetores.

## Métodos especiais

Métodos especiais são definidos pela linguagem e são parte central do modelo de 
dados. Uma classe pode implementar certas operações que serão invocadas por uma
sintaxe especial (como operadores aritméticos) definindo métodos com nomes 
especiais. Essa é a abordagem pythonica para sobrecarga de operadores, 
permitindo classes definirem seus próprios comportamentos para operadores
da linguagem.

### Criação do vetor e atributos x e y

```python
>>> from vectors import vector
>>> v = vector(3, 4)
>>> v.x
3
>>> v.y
4
```

A inicialização de um objeto é definido no método `__init__(self)`. O parâmetro
`self` é obrigatório por definição da linguagem Python. Outros parâmetros podem
ser adicionados conforme a necessidade. No caso de `vector`, teremos dois 
parâmetros que representarão as coordenadas iniciais do vetor (`x` e `y`).

### Representação textual do vetor

```python
>>> v = vector(1, 2)
>>> v
vector(1, 2)
```

A representação textual é definida no método `__repr__(self)`. Observe que aqui 
há uma alteração do que fizemos anteriormente. Esse alteração tem por objetivo
distinguir um vetor de uma tupla.

### Comparação de igualdade

```python
>>> v = vector(1, 2)
>>> w = vector(1, 2)
>>> x = vector(2, 4)
>>> v == w
True
>>> v == x
False
```

A comparação de igualdade é definida no método `__eq__(self, other)`. Observe que
aqui há um parâmetro além do `self`. Esse parâmetro será outro vetor e dois 
vetores são consideradores iguais quando suas respectivas coordenadas `x` e `y` 
são iguais.

### Comparação de desigualdade

```python
>>> v = vector(1, 2)
>>> w = vector(3, 4)
>>> x = vector(1, 2)
>>> v != w
True
>>> v != x
False
```

A comparação de igualdade é definida no método `__ne__(self, other)`. Observe que
aqui há um parâmetro além do `self`. Esse parâmetro será outro vetor e dois 
vetores são consideradores diferentes quando ao menos uma de suas respectivas 
coordenadas `x` e `y`  são diferentes.

### Comprimento (distância até a origem)

```python
>>> v = vector(3, 4)
>>> abs(v)
5.0
```

O comprimento de um vetor, que é a distância até a origem (0, 0), é 
matematicamente chamado de norma ou módulo do vetor. Sendo módulo, ou valor 
absoluto, o cálculo em Python pode ser feito como para qualquer outra variável,
com a função embutida `abs`. Porém, precisamos definir como é feito esse cálculo,
o que será definido no método `__abs__(self)`. Quando executamos `abs(v)`, esse 
método é executado por baixo dos panos. 

### Adição de vetores (com outro vetor e com um número)

```python
>>> v = vector(1, 2)
>>> w = vector(3, 4)
>>> v + w
vector(4, 6)
>>> w + v
vector(4, 6)
>>> v + 1
vector(2, 3)
>> 2.0 + v
vector(3.0, 4.0)
```

A operação de adição, e que será executada com o operador `+`, é definida no 
método `__add__(self, other)`, o qual deverá retornar um novo objeto `vector`. 
Observe que aqui há um parâmetro além do `self`. Esse parâmetro poderá ser um 
outro vetor ou um número. Se for um vetor, as respectivas coordenadas `x` e `y`
serão somadas e um novo vetor será criado com essas novas coordenadas. Se o 
`other` for um número, este valor será somada a cada coordenada do vetor para 
definição das coordenados do novo vetor. `other` será um vetor se a expressão 
`isinstance (other, vector)` for verdadeira. Utilize isso em uma condicional.

### Subtração (com outro vetor ou com um número)

```
>>> v = vector(1, 2)
>>> w = vector(3, 4)
>>> v - w
vector(-2, -2)
>>> v - 1
vector(0, 1)
```

A operação de subtração, e que será executada com o operador `-`, é definida no 
método `__sub__(self, other)`, o qual deverá retornar um novo objeto `vector`.
Observe que aqui há um parâmetro além do `self`. Esse parâmetro poderá ser um 
outro vetor ou um número. Se for um vetor, as respectivas coordenadas `x` e `y` 
serão subtraídas e um novo vetor será criado com essas novas coordenadas. Se o 
`other` for um número, este valor será subtraído de cada coordenada do vetor 
para definição das coordenados do novo vetor. `other` será um vetor se a 
expressão `isinstance(other, vector)` for verdadeira. Utilize isso em uma 
condicional.

### Multiplicação (por outro vetor e por um número)

```python
>>> v = vector(1, 2)
>>> w = vector(3, 4)
>>> v * w
vector(3, 8)
>>> v * 2
vector(2, 4)
>>> 3.0 * v
vector(3.0, 6.0)
```

A operação de multiplicação, e que será executada com o operador `*`, é definida 
no método `__mul__(self, other)`, o qual deverá retornar um novo objeto `vector`.
Observe que aqui há um parâmetro além do `self`. Esse parâmetro poderá ser um 
outro vetor ou um número. Se for um vetor, as respectivas coordenadas `x` e `y` 
serão multiplicadas e um novo vetor será criado com essas novas coordenadas. Se 
`other` for um número, cada coordenada do vetor será multiplicada por este 
número para definição das coordenados do novo vetor. `other` será um vetor se a 
expressão `isinstance(other, vector)` for verdadeira. Utilize isso em uma 
condicional.

### Divisão (por outro vetor e por um número)

```python
>>> v = vector(2, 4)
>>> w = vector(4, 8)
>>> v = v / w
>>> v
vector(0.5, 0.5)
>>> v = v / 2
>>> v
vector(0.25, 0.25)
```

A operação de divisão, e que será executada com o operador `/`, é definida 
no método `__truediv__(self, other)`, o qual deverá retornar um novo objeto 
`vector`. Observe que aqui há um parâmetro além do `self`. Esse parâmetro poderá 
ser um outro vetor ou um número. Se for um vetor, as respectivas coordenadas `x` 
e `y` serão divididas e um novo vetor será criado com essas novas coordenadas. 
Se `other` for um número, cada coordenada do vetor será dividida por este 
número para definição das coordenados do novo vetor. `other` será um vetor se a 
expressão `isinstance(other, vector)` for verdadeira. Utilize isso em uma 
condicional.

### Inversão (ou negação)

```python
>>> v = vector(1, 2)
>>> -v
vector(-1, -2)
```

A operação de inversão ou negação de um vetor é uma operação unário, e que será 
executada com o operador `-` (`-v`), é definida no método `__neg__(self)`, o 
qual deverá retornar um novo objeto `vector`. As coordenadas desse novo vetor
serão as coordenadas do vetor original com sinal trocado.

## Métodos específicos para manipulação de vetores

Quando a utilização de operadores já existente na linguagem não são suficientes
para expressar todas as operações realizadas com um objeto, será necessário criar
métodos específicos. No caso de um vetor, as operações que criaremos tais métodos
são: movimentação, rotação, escala e cópia.

### Movimentação de um vetor (mudança interna no vetor)

```python
>>> v = vector(1, 2)
>>> w = vector(3, 4)
>>> v.move(w)
>>> v
vector(4, 6)
>>> v.move(3)
>>> v
vector(7, 9)
```

A movimentação de um vetor se dará pelo método `move(self, other)`. Essa operação
é bastante parecida com a operação de adição, podendo ser tomada como parâmetro
um número ou um outro vetor, porém no lugar de retornar o resultado da operação, 
o vetor terá suas próprias coordenadas atualizadas. É uma operação local, interna
ao objeto.

### Rotação (sentido anti-horário a partir de um ângulo, mudança interna no vetor)

```python
>>> v = vector(1, 2)
>>> v.rotate(90)
>>> v == vector(-2, 1)
True
```

Imagine um ângulo entre o vetor e o eixo `x`. A operação de rotação aqui definida
será manipular esse ângulo de acordo com o argumento do método, e será realizada
pelo método `rotate(angle)`, sendo o parâmetro `angle` o ângulo de rotação em 
graus, que ocorrerá no sentido anti-horário. Os novos valores das coordenados do
vetor serão calculados da seguinte forma:

```
x' = cos(a) * x + sin(a) * y
y' = - sin(a) * x + cos(a) * y
```

Onde `a` é o parâmetro `angle` convertido para radianos, `cos` e `sin` são
cosseno e seno, respectivamente. O módulo `math` pode ser utilizado aqui.

### Escala (mudança interna no vetor)

```python
>>> v = vector(1, 2)
>>> w = vector(3, 4)
>>> v.scale(w)
>>> v
vector(3, 8)
>>> v.scale(0.5)
>>> v
vector(1.5, 4.0)
```

A escala de um vetor se dará pelo método `scale(self, other)`. Essa operação
é bastante parecida com a operação de multiplicação, podendo ser tomada como
parâmetro um número ou um outro vetor, porém no lugar de retornar o resultado da 
operação, o vetor terá suas próprias coordenadas atualizadas. É uma operação 
local, interna ao objeto.

### Cópia

```python
>>> v = vector(1, 2)
>>> w = v.copy()
>>> v is w
False
>>> v == w
True
```

A forma óbvia de se fazer cópia de variáveis é com o operador de atribuição 
(`=`). Porém, com objetos isso não pode não funcionar como o esperado. Pois,
na verdade, uma variável é como se fosse uma referência, ou uma etiqueta, para
um objeto que está na memória do computador. Assim, se você fizer `v = w` onde
essas variáveis sejam objetos, você estará copiando a referência para o objeto,
e não o objeto em si. Então terá o mesmo objeto sendo referênciado por duas 
variáveis. Fazendo a alteração em um, irá impactar no outro. Isso porque, na 
verdade, trata-se do mesmo objeto.

Assim, implementaremos um método `copy(self)` específico para criar e retornar 
uma cópia do vetor.

## Conclusão

Durante as últimas seções introduzimos alguns conceitos de programação
orientada a objetos tomando como estudo de caso a classe `vector` já existente
no Free Python Games. Fizemos uma descontrução da classe, para visualizarmos
como seria caso essa classe nao existisse, ou seja, usando programação
estruturada, e depois reconstruimos a classe. Com isso, começamos a entender 
os benefícios da programação orientada a objetos e como ela é implementada em
Python, tanto utilizando métodos especiais já previstos pela linguagem quanto
métodos mais específicos para manipulação de vetores.

Nas próximos seções aprofundaremos o estudo da programação orientada com
dois jogos do Free Python Games já estudados e que foram portados para OO:
Snake e Pacman. 

## Referências

[Modelo de dados](https://docs.python.org/pt-br/3/reference/datamodel.html)

[Anterior](03_poo_encapsulamento.md) | [Próximo](04_poo_vector2.md)
