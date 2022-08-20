# Respondendo a eventos

Capturar movimentos e cliques do mouse e teclas pressionadas é fundamental no
desenvolvimento de jogos eletrônicos. É isso que aprenderemos nessa seção.

## Programação orientada a eventos

Programação orientada a eventos é quando você escreve código para responder a
eventos.

Para tal, você irá precisar de dois elementos:

- Evento a ser capturado
- Resposta ao evento

```Turtle``` fornece mecanismo para registrar os eventos que serão **escutados**
por meio dos métodos ```on```:

- ```onclick(fun, btn=1, add=None)```
- ```onscreenclick(fun, btn=1, add=None)```
- ```onrelease(fun, btn=1, add=None)```
- ```ondrag(fun, btn=1, add=None)```
- ```onkey(fun, key)```
- ```onkeypress(fun, key=None)```
- ```ontimer(fun, t=0)```

Esses métodos definem os eventos a serem **capturados**. Perceba que todos eles 
possuem um parâmetro obrigatório ```fun```. Este ```fun``` é de  ```function```.
Ou seja, é uma função que será executada em **resposta** ao evento. Essa função
pode ser definida por você, ou pode ser uma função já existente, desde que ela 
possua a quantidade de parâmetros esperada.

Vejamos um exemplo.

Imagine um cenário em que a tartaruga deve movimentar-se até o ponto em que a
tela foi clicada.

Já vimos anteriormente que o método ```goto(x, y)``` recebe dois parâmetros,
que indicam um ponto para onde a tartaruga deve ir.

Já o evento que queremos capturar é o clique na tela, o que é feito com a função
```onscreenclick(fun, btn=1, add=None)```.

Porém, essa função não é de uma tartaruga em específico, mas da tela. Então
precisaremos importa-lá do módulo ```turtle``` antes de utiliza-lá.
Aproveitaremos para ver outra sintaxe de importação com a instrução ```from```.
Veja como fica:

```python
>>> from turtle import Turtle, onscreenclick, listen
>>> turtle = Turtle()
>>> onscreenclick(turtle.goto)
>>> listen()
```

Perceba que você não deve colocar os parênteses no ```goto```, tão pouco os
parâmetros. Isso será feito internamente. Quando a tela for clicada, os
parâmetros receberão a posição em que a tela foi clicada e a função será 
executada.

Além disso, após a definição dos eventos que serão escutados, a escuta deve ser
iniciada com a função ```listen()```.

Vamos agora definir uma função própria. Essa função vai mandar a tarturuga ir
para o ponto clicado e depois escrever na tela a sua nova posição (veja o novo
método ```write```).

```python
>>> def goto_and_mark(x, y):
...    turtle.goto(x, y)
...    turtle.write(turtle.position())
>>> 
>>> goto_and_mark(191, 183)
```

A última linha acima serve apenas para testarmos se a função faz o que queremos.
Execute algumas vezes com argumentos diferentes, se quiser. Assim, quando for 
feita a ligação com o evento, você terá certeza que a função está correta.

Agora, precisamos atualizar qual será a resposta ao evento de clique na tela.

```python
>>> onscreenclick(goto_and_mark)
```

Novamente, lembre-se de não utilizar parênteses e argumentos. Essas funções que
serão executadas em algum momento no futuro, são chamadas de **funções de 
retorno**.

Vamos agora responder às teclas pressionadas.

Imagine agora que você queira movimentar a tartaruga através das teclas de setas
(cima/baixo, direta/esquerda). Para isso, deverá escrever 4 funções de retorno,
que irão manipular as coordenadas **x** e **y** da tartaruga. Neste caso, essas
funções não terão parâmetro algum.

```python
>>> def up():
...     y_atual = turtle.ycor()
...     novo_y = y_atual + 5
...     turtle.sety(novo_y)
>>> 
>>> up() 
```

A última linha acima serve apenas para testarmos se a função faz o que queremos.
Execute algumas vezes, se quiser.

Agora precisamos associar essa funcao à tecla de seta para cima. 

```python
>>> from turtle import onkey, listen
>>> onkey(up, 'Up')
>>> listen()
```

Da mesma forma, podemos criar uma função para movimentar a tartaruga para baixo.

```python
>>> def down():
...     y_atual = turtle.ycor()
...     novo_y = y_atual - 5
...     turtle.sety(novo_y)
>>> 
>>> down() 
```

E depois associa-lá à tecla da seta.

```python
>>> from turtle import onkey, listen
>>> onkey(down, 'Down')
>>> listen()
```

**Desafio** Sabendo que para movimentar a tartatura na horizontal você deve 
manipular a coordenada **x** e que as teclas para direita e esquerda são 
```Right``` e ```Left```, respectivamente, faça a tartaruga movimentar-se 
nessa direção.

[Anterior](03_caneta.md) | [Próximo](04_respondendo_eventos.md)
