# Paint, for drawing shapes

O primeiro jogo do Free Python Games a ser estudado será o Paint, que na
realidade não é um jogo, mas um editor de figuras tal qual o desenvolvido
nas seções anteriores. Com isso, a ambientação ao Free Python Games será
facilitada. Antes mesmo de começar a estudar o código-fonte e começar a
alterá-lo é importante que você execute o programa. Assim entenderá como
funciona do ponto de vista do usuário e também terá a certeza que está de
fato funcionando, e que os erros que surgirão ao longo das 
mudanças foram introduzidos por você e não erros que já vieram com o programa.

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
faz (ou deverá saber), e a palavra `pass` (indicando que ela não faz nada, como
quem diz "passe direto").

### Ponto de entrada

Por fim...

## Referências
PEP-8


[Anterior](01_fpg_introducao.md) | [Próximo](02_fpg_paint.md)