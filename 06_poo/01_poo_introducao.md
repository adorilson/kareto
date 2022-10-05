# Programação Orientada a Objetos

Paradigmas de programação fornecem e determinam a visão que o programador possui
sobre a estruturação e execução do programa. Por exemplo, em programação orientada
a objetos, os programadores podem abstrair um programa como uma coleção de objetos
que interagem entre si, enquanto em programação funcional os programadores abstraem
o programa como uma sequência de funções executadas de modo empilhado e, ainda,
programação estruturada tem ênfase em sequência, decisão e, iteração (sub-rotinas,
laços de repetição, condicionais e, estruturas em bloco), criado no final de 1950
junto às linguagens ALGOL 58 e ALGOL 60.

Raramente um software será escrito exclusivamente em um único paradigma. Nos 
programas que fizemos até aqui, utilizamos prioritariamente o paradigma programação
estrutura. Mas a programação orientada a eventos (lembre-se: quando alguma coisa 
acontecer, haverá uma resposta a este evento) e funcional estão presentes em 
linhas como:

```python
onscreenclick(tap)

onkey(lambda: color('black'), 'K')
```
Por outro lado, a programação orientada a objetos está presente no trecho abaixo e sempre que métodos desses objetos são executados:

```python
turtle = Turtle()

pacman = vector(13, 17)
```

As variáveis `turtle` e `pacman` são objetos das classes `Turtle` e `vector`, 
respectivamente. Então perceba que os paradigmas podem ser utilizados em conjunto,
e normalmente o são. Não criamos classes, mas utilizamos em nossos programas 
classes criados por outras pessoas. Criar nossas classes e conhecer os recursos
de Python para a orientação a objetos é o que veremos daqui para frente.

## Desconstruindo a orientação a objetos

Uma abordagem comum para iniciar os estudos de orientação a objetos é a construção 
de classes a partir de variáveis e funções da programação estruturada. Porém, 
como temos um conjunto de objetos da classe `vector` utilizada no jogo `Pacman`
e já termos discutidos conceitos em torno da definição do que é um vetor em seções
anteriores, faremos uma desconstrução dos objetos `vector` neste jogo e tomaremos
nota do processo.

Comece subtituindo todos as referencias para `vector` 

```python
aim = vector(5, 0)
pacman = vector(-40, -80)
ghosts = [
    [vector(-180, 160), vector(5, 0)],
    [vector(-180, -160), vector(0, 5)],
    [vector(100, 160), vector(0, -5)],
    [vector(100, -160), vector(-5, 0)],
]
```
por tuplas.
```python
aim = (5, 0)
pacman = (-40, -80)
ghosts = [
    [(-180, 160), (5, 0)],
    [(-180, -160), (0, 5)],
    [(100, 160), (0, -5)],
    [(100, -160), (-5, 0)],
]
```

Uma abordagem mais radical seria substituir cada variável por variáveis que
representaram as coordenadas `x` e `y` de cada ponto. Porém, uma tupla em que
o elemento no índice `0` representa o `x` e o elemento no índice `1` representa
o `y` já é o suficiente.

A partir daí, todas as referencias a `aim`, `pacman` e `ghosts` precisam ser
atualizadas. Perceba que anteriormente as oferações realizadas com essas variáveis
estavam **encapsuladas** nos objetos, e havia uma semântica explícita pois eram 
objetos da classe `vector`, com atributos e operações específicas. Agora teremos
variáveis do tipo tupla, que possuem finalidade genérica, e o uso enquanto pontos
em um plano cartesiado é implicito, não existindo no códigos estruturas sintáticas
que definam isso, sendo necessário agora explicitar as operações.

## Referências
[Paradigmas de programação](https://pt.wikipedia.org/wiki/Paradigma_de_programa%C3%A7%C3%A3o)

[Programação estruturada](https://pt.wikipedia.org/wiki/Programa%C3%A7%C3%A3o_estruturada)


[Anterior](/05_free_python_games/05_fpg_pacman.md) | [Próximo](02_poo_vector.md)
