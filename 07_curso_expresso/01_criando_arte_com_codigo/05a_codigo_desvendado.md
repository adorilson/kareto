# Código desvendado

Você já utilizou dois símbolos especiais diversas vezes: o *ponto* (`.`) e os
*parênteses* (`()`). Chegou a hora de entender melhor como eles funcionam.

## O operador . (ponto)

O *ponto* é usado para acessar *atributos* e *métodos* de um objeto ou
definições em um módulo. Quando criamos um objeto de uma classe, ele pode ter
*dados* (chamamos de *atributos*) e *ações*  associadas (chamadas de
*métodos*). O ponto permite acessar esses elementos. Por exemplo:

```python
import turtle

artista = turtle.Turtle() # Acessa a classe Turtle do módulo turtle

artista.forward(100) # Acessa o método forward do objeto artista
```

Aqui, `artista.forward` significa "*pegue o método `forward` do objeto
`artista`*". De forma similar,  `turtle.Turtle` significa *"pegue a classe
`Turtle` do módulo `turtle`"*. 

Da mesma forma, podemos acessar atributos:

```python
artista.speed = 5 # Define o valor 5 para o atributo speed do objeto artista
```


## O operador () (parênteses)

Os *parênteses* são usados para *executar funções, métodos e outros chamáveis*.
Quando colocamos `()` após um nome, estamos dizendo ao Python para
*chamar/executar* aquela coisa. Por exemplo:

```python
artista.forward(100) # Chama/executa o método forward no objeto artista 
```

Sem os `()`, estaríamos apenas acessando o método, mas sem executá-lo.
Veja como se isso se comporta em uma sessão interativa do interpretador
do Python (abra um e execute):

```python
>>> import turtle
>>> artista = turtle.Turtle()
>>> artista.forward
<bound method TNavigator.forward of <turtle.Turtle object at 0x700f163db5c0>>
>>> turtle.Turtle
<class 'turtle.Turtle'>
```

As linhas `artista.forward` e `turtle.Turtle` acessaram os elementos, mas eles
não foram executados. Ficando restrito a exibir uma representação textual 
daquele elemento.

Note ainda que uma classe também é um chamável, daí a necessidade dos
parênteses em `turtle.Turtle()` quando se deseja criar um novo objeto.
A ausência dos parênteses é uma *sintaxe* válida em Python, por isso é 
executado sem erros, mas a *semântica* é bem diferente quando eles estão
presentes. É preciso ficar atento. Por outro lado, isso pode ser útil para 
criar apelidos. Veja:

```python
import turtle

Tartaruga = turtle.Turtle # Está criando um apelido para a classe

artista = Tartaruga() # Aqui estamos executando a classe, portanto, criando o objeto
```

## Resumo

- O *ponto* (`.`) é o operador de acesso a membros de um objeto
- Os parênteses (`()`) chamam *funções*, *métodos* e *classes*, permitindo 
executar ações ou criar objetos.
- Sem os `()`, apenas obtemos uma referência ao método, função ou classe, sem
executá-los.

[Anterior](05_triangulo.md) | [Próximo](06_retangulo.md)
