# Criando figuras (tudo junto e misturado)

Agora vamos juntar o que aprendemos nas seções anteriores com mais alguns novos
truques e criar uma espécie de editor de imagens.

Os requisitos para esse "editor" são simples:

```
1. O usuário deve ser capaz de clicar na tela em duas posições.
    A distância entre esses dois pontos será o parâmetro para o tamanho da 
    figura. (raio se for um círculo, lado se for uma quadrado ou retângulo e 
    assim por diante)
2. O usuário deve ser capaz de escolher qual figura deseja desenhar
```

Embora um algoritmo, depois de pronto, seja comparada a uma receito de bolo,
não existe uma receita de bolo para a construção em si. A construção de 
algoritmo pode ser inicializada por diferentes formas e seguir diferentes 
caminhos, inclusives por caminhos que não pareçam levar ao destino, até que
ele esteja pronto.

Um caminho comum é começarmos por aquilo que já temos pronto, ou o que 
consideramos mais simples de ser feito, e irmos evoluindo ao redor disso
até que ele esteja finalizado.

Dos exercícios anteriores, já temos funções que desenham as figuras.
Começaremos por elas.

## Começando

Considere a função para desenhar um quadrado:

```python
def square():
    for _ in range(4):
        turtle.forward(50)
        turtle.right(90)
```

Vamos associar essa função ao evento de clique na tela, o que é feito
com a função ```onscreenclick(fun, btn=1, add=None)```:

```python
# código omitido aqui
from turtle import onscreenclick, mainloop
onscreenclick(square)
mainloop()
```

A chamada à função ```mainloop()``` inicia o laço de eventos. É ela que faz
com que a tela não se feche imediatamente. No lugar disso, ficará repetidamente 
ouvindo os eventos, daí o nome _main loop_ (loop principal).

Porém, é provável que tenha ocorrido o seguinte erro:

```
Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python3.10/tkinter/__init__.py", line 1921, in __call__
    return self.func(*args)
  File "/usr/lib/python3.10/turtle.py", line 674, in eventfun
    fun(x, y)
TypeError: square() takes 0 positional arguments but 2 were given
```

Ler essas mensagens de erro também é uma habilidade que devemos desenvolver.
Essas sequências são conhecidas como _traceback_ ou pilha de execução, e a 
leitura é feita de baixo para cima.

A linha mais importante é a última, pois ela diz qual erro ocorreu. Neste 
caso, ela está dizendo que a função ```square()``` possui 0 (zero) argumentos 
posicionais, mas que foram passados 2 valores. 

As linhas seguintes ajudarão a rastrear o erro. A linha imediatamente acima, 
indica em qual arquivo e o número da linha de código ocorreu o erro, e mostra
também o conteúdo, no caso ```fun(x, y)```.

Lembre-se que estamos trabalhando com *eventos* e *funções de retorno*, daí a
linha não ser ```square(x, y)```. Isso é porque neste momento, ```fun``` é a
referência para ```square```. Durante a execução do programa, ela será referência
para funções diversas.

Uma vez identificado o erro, no caso uma chamada com argumentos incorretos,
precisamos decidir como fazer a correção. Um caminho seria simplesmente 
adicionar parâmetros à função (```def square(x, y)```), mesmo que internamente
eles não seja utilizados. **Desafio** Tente isto.

Porém, faremos uma função semelhante à ```goto_and_write``` criada em seções
anteriores. Já à ```square```, posteriormente serão adicionados parâmetros
referentes às dimensões. Veja como fica a nova função
```goto_and_square(x, y)```.

```python
def goto_and_square(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    square()
```

**Desafio** Lembre-se de mudar na chamada à ```onscreenclick(...)```.

Se tudo estiver correto, agora quadrados são desenhados na tela a partir
do clique do mouse. Porém, eles tem tamanho fixo.

## Dando tamanho para as figuras

Vamos começar o próximo passo adicionando um parâmetro ```width``` à função
```square```.

```python
def square(width):
    for _ in range(4):
        turtle.forward(width)
        turtle.right(90)
```

Agora, na chamada à função poderemos passar o tamanho que queremos para o lado 
do quadrado. Como existe apenas um evento de clique e não dois ou mais, teremos
que programaticamente determinar se o clique é o primeiro ou o segundo, e agir
conforme.

Vamos utilizar o seguinte algoritmo para este trecho:

```
Se é o primeiro clique:
    armazene a posição
Se não:
    calcule a distância entre as posicoes dos cliques
    move a tartaruga para a posicao do primeiro clique
    desenhe o quadrado informe o tamanho calculado
    inicialize o marcador de cliques
```

Aqui, uma decisão chave a ser tomada é como identificar se é o primeiro ou
segundo clique e como armazenar a posição. Mais um vez, podemos fazer de 
diversas formas, mas usaremos uma única variável, que chamaremos de ```start```. 
Ela armazenará a posição do primeiro clique e terá valor ```None``` caso ainda 
não tenha ocorrido o primeiro clique.

Com isso em mente, criaremos a variável ```start``` com valor inicial ```None```
**fora** da função ```goto_and_square(x, y)``` e dentro dela faremos a
implementação do algoritmo acima.

```python
start = None

def goto_and_square(x, y):
    global start
    if start is None:
        start = x, y
    else:
        width = start[0] - x

        turtle.penup()
        turtle.goto(start[0], start[1])
        turtle.pendown()

        square(width)

        start = None
```

Esclarecimentos:
1. a instrução ```global``` indica que a variável ```start``` vem de fora da 
função,
que ela é do escopo global e não do escopo local da função
1. a forma de verificar se uma variável/objeto é ```None``` é com o operador
```is```
1. no bloco dentro do ```else``` cada passo do algoritmo está separado por uma
linha em branco. É fácil perceber que alguns passos precisam de mais uma linha.
Além disso, por questão de simplificação, o tamanho do lado do quadrado foi uma
diferença simples entre as coordenadas **x** do primeiro e segundo cliques.

## Evitando repetição de código

Podemos seguir essa estratégia e implementar uma função dessa para cada figura
que o nosso editor será capaz de criar, além de fazer as devidas adequações
nas funções que efetivamente desenham as figuras.  

Porém, ficaríamos com uma certa repetição de código nas funções ```goto_and_```.
Além disso, iremos precisar de mecanismo que nos permita escolher 
qual figura será desenhada.

Agora que temos um par de função para cada figura, podemos fazer isso 
associando uma tecla do teclado à uma figura, e criando novas funções para
fazer a troca da figura (acréscimo e uso de parâmetro).

Então, faremos mudanças na função ```goto_and_square```, que será agora 
genérica e não mais específica para quadrados, e em cada função que desenha
as figuras. As mudanças em ```goto_and_square``` serão as seguintes:
1. renomear para ```tap``` (já que nem sempre há deslocamento e desenho)
1. no lugar de executar ```square```, executaremos ```shape```, que será 
referência
para as funções de desenho. Ela será peça importante na troca de figuras
1. A "nova função" ```shape``` receberá dois argumentos, que representam o ponto
inicial e o ponto final de desenho da figura
1. Em consequência dos itens anteriores, a definição das dimensões da figuras,
assim como a movimento para o ponto inicial será deslocado para dentro 
das funções de cada figura.

Cada função das figuras, deverá agora:
1. receber dois parâmetros, ```start``` e ```end```, que indicam o primeiro e o 
segundo ponto em que a tela foi clicada
1. fazer o deslocamento da tartaruga para o ponto inicial
1. calcular a dimensão de interesse, a partir dos parâmetros
1. desenhar a figura conforme

Aplicando essas alterações, teremos o seguinte:

```python
def tap(x, y):
    global start
    if start is None:
        start = x, y
    else:
        end = x, y

        shape(start, end)

        start = None

def square(start, end):
    turtle.penup()
    turtle.goto(start[0], start[1])
    turtle.pendown()

    width = start[0] - end[0]
    for _ in range(4):
        turtle.forward(width)
        turtle.right(90)

```

**Desafio** Como renomeamos a função  ```goto_and_square``` para ```tap```, 
precisamos atualizar a chamada à ```onscreenclick(...)```. Faça isso.

## Trocando as figuras

Mesmo após a conclusão do desafio, ainda não será possível a execução.
Se executar isso dessa forma, ocorrerá um erro na chamada
```shape(start, end)```,
tão pouco ainda somos capazes de alternar entre as figuras. Vamos fazer isso em 
duas
etapas. Primeiro a definição de ```shape```, depois a alternância.

### Definindo a função de retorno

```shape``` será uma função de retorno. Então vamos simplesmente atribuir
a ela a função da figura que será executada em algum momento no futuro.

```python
shape = square
```

Observe que não estamos usamos os parênteses, pois a função deve ser executada
agora, apenas em algum momento no futuro. Em um primeiro momento, faça a
alternancia das figuras editando o código-fonte e executando, por vez o editor
será capaz de desenhar apenas um tipo de figura.

Agora que validamos esse mecanismo e verificamos que somos capaz de desenhar
figuras distintas, precisamos implementar a alternância entre elas à livre
escolha do usuário. Para tal, cada figura será associada a uma tecla. 

### Alternando entre as figuras

Inicialmente, deveremos criar funções que farão a alteração do conteúdo de
```shape```. Depois, deveremos associar a execução de cada uma dessas funções
à tecla escolhida, arbitrariamente por você, pessoa programadora.

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

Quando *s* for pressionada, alteramos ```shape``` para ```square```.
Quando *c* for pressionada, alteramos ```shape``` para ```circle```.

**Desafio** Complete para todas as figuras.

E pronto. Temos um editor que atende aos requisitos propostos no início da seção.

## Referências

[Callback](https://pt.wikipedia.org/wiki/Callback)

[Laço de eventos](https://pt.wikipedia.org/wiki/La%C3%A7o_de_eventos)

[Anterior](04_respondendo_eventos.md) | [Próximo](06_melhorando_o_editor.md)
