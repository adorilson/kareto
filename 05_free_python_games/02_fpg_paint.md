# Paint, for drawing shapes

O primeiro jogo do Free Python Games a ser estudado será o Paint, que na
realidade não é um jogo, mas um editor de figuras tal qual o desenvolvido
nas seções anteriores. Com isso, a ambientação ao Free Python Games será
facilitada. Antes mesmo de começar a estudar o código-fonte e começar a
alterá-lo é importante que você execute o programa. Assim entenderá como
funciona do ponto de vista do usuário e também terá a certeza que está de
fato funcionando, e que os erros que surgirão ao longo das 
mudanças foram introduzidos por você e não erros que já vieram com o programa.

## Pequeno manual de uso

Ao iniciar o `Paint` ele desenhará por padrão linhas. Clique em dois
pontos da tela e uma linha será desenhada entre eles. Para alternar
entre linha e quadrado, use as teclas `l` e `s`. Também é possível
mudar as cores: `K` para preto, `W` para branco, `G` para verde, `B`
para azul e `R` para vermelho.

## Anatomia do código-fonte

### Comentários com exercícios

```python
"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.
"""
```

Os jogos presentes no Free Python Games foram projetos para experimentação e
mudanças. Mais do que isso, já estão inclusos exercícios propostos no topo de
cada arquivo com o código-fonte dos jogos.

### Importações de módulos

```python
from turtle import *

from freegames import vector
```

As primeiras linhas executáveis são as importações de módulos e funções.
Seja da biblioteca padrão, com `turtle` neste caso, seja do módulo 
`freegames`. Como dito anteriormente, o Free Python Games também possui
uma biblioteca em si, a qual será detalhado futuramente.

#### import *

Observe que foi utilizado um `*`, no lugar de explicitar o que está sendo
do módulo. Essa importação curinga é uma má prática e deve ser evitada, pois
não fica claro quais os nomes estarão presentes no espaço de nomes, confundindo
tanto leitores quanto ferramentas de automação. Inclusive, essa má prática é
apontada pela PEP-8, um documento que descreve convenções para codificação 
Python.

Aqui, um exercício adicional e que vai ajudar você a conhecer e 
descobrir novas funções de `turtle` é remover essa importação (apenas adicione
um `#` no início da linha que a linha será convertida em um comentário), executar
o jogo e ir atualizando a importações conforme os erros forem aparecendo. Veja o
exemplo.

1. Remover a importação 
```python
# from turtle import *
```

2. Executar e observar o erro, semelhante a pilha de execução com o erro,
e identificar o nome ausente
```shell
Traceback (most recent call last):
  File ".../paint.py", line 80, in <module>
    setup(420, 420, 370, 0)
NameError: name 'setup' is not defined
```

Neste caso, não foi localizado algo com o nome `setup`. A rigor, você nem
precisa ir até a linha em que o erro ocorreu. Chegaremos lá depois.

3. Adicionar o nome ausente na importação
```python
from turtle import setup
``` 

4. Repetir os passos 2 e 3 até que o programe rode com sucesso

**Desafio** Execute este algoritmo para todas os nomes importados de `turtle`

#### from freegames import vector

Uma das classes definidas pelo módulo `freegames` é `vector`. Estudaremos em detalhes mais adiante. Mas, por hora, o que precisamos entender é que facilita o 
manuseio das coordenadas `x` e `y` dos pontos no sistema de coordenadas.

No editor que criamos, utilizamos tuplas para identificar um ponto:

```python
>>> ponto = (10, 20)
>>> ponto[0]
10
>>> ponto[1]
20
```

Veja como fica com `vector`:

```python
>>> from freegames import vector
>>> ponto = vector(10, 20)
>>> ponto.x
10
>>> ponto.y
20
```

Observe que para além do nome `ponto`, de fato é uma estrutura que possui os 
atributos `x` e `y`, com uma semântica explícita. O que torna a leitura e 
escrita mais claras e significativas.

### Funções

Na sequência, teremos as definições de diversas funções, que serão chamadas
ao longo da execução do programa. Algumas funções virão completas e funcionais,
podendo haver algum exercício que precisará alterá-las, outras funções nada 
farão. Contendo apenas a string de documentação, para que saibamos o que ele
faz (ou deverá fazer), e a palavra `pass` (indicando que ela não faz nada, como
quem diz "passe direto").

### Ponto de entrada

Por fim, chegamos ao ponto de entrada do programa, que é onde de fato começará
a interação com o usuário. No caso de  `Paint`, temos o seguinte:

```python
state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
```

A primeira linha contém definição da variável responsável por manter o estado 
do programa. Enquanto no editor que criamos utilizamos duas variáveis, aqui 
está sendo utilizado apenas uma, `state`. Mas é uma estrutura composta, 
conhecida como dicionário, podendo armazenar diversos valores, que são 
acessados por meio de chaves. No caso, as chaves são `start` e `shape`, e os
valores iniciais  `None` e `line`, respectivamente.

A linha seguinte contém a chamada a uma nova função, `setup`, que é utilizada
para definir dimensões e posicionamento da tela do programa.

A linha `onscreenclick(tap)` nos indica que quando a tela for clicada, será
executada a função `tap`.

Temos então a chamada à `listen`, que faz com que `turtle` fique escutando
as teclas que serão pressionadas, e que são definidas nas chamadas à `onkey` que se seguem. Em `Paint`, além de escolher entre figuras, também é possível
escolher entre cores.

Por fim, a última linha chama a função `done()`, que é exatamente igual
`mainloop()` que usamos no nosso editor.

É importante observar que no Free Python Games foi utilizado uma abordagem mais
de programação estruturada e menos de orientação a objetos. Por este motivo,
não temos a criação de um objeto `turtle` (`turtle = turtle.Turtle()`), como 
fizemos em nosso editor. No lugar disso, as funções são importadas e chamadas 
diretamente do módulo.

**Desafio** Resolva os exercícios proposta para `Paint`.

## Referências
[PEP-8 e imports em Python](https://medium.com/gbtech/pep-8-e-imports-em-python-78a6fbf53475)


[Anterior](01_fpg_introducao.md) | [Próximo](02_fpg_paint.md)