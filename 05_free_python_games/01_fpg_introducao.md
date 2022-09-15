# Free Python Games

Free Python Games é uma coleção de jogos escritos em Python com propósitos
educativos e de diversão. Os jogos foram escritos em código Python simples
e projetos para experimentação e mudanças. 

Sua documentação original está disponível em:
https://grantjenks.com/docs/freegames/. Também existe um trabalho em andamento
de tradução para o português do Brasil em:
https://ifrn.github.io/free-python-games/pt_BR/

Embora seja possível ver e copiar o código dos jogos diretamente da documentação,
não será possível executá-los sem antes instalar um novo pacote no seu computador
(ou seja qual for o ambiente de execução). Isso ocorre porque o Free Python Games,
além da coleção de jogos, também é um biblioteca escrita em cima do ```turtle```,
contendo funcionalidades que facilitarão o desenvolvimento dos jogos, e serão
detalhadas mais adiante.

## Início rápido

A seguir, as iniciadas com **$** devem ser digitadas e executadas no terminal de
comandos do seu ambiente (você não deve digitar o cifrão em si), as demais linhas 
é o resultado esperado para o comando.

Para instalar Free Python Games basta utilizar [pip](https://pypi.python.org/pypi/pip), o gerenciador de pacotes Python:
 

```shell
$ python3 -m pip install freegames
Defaulting to user installation because normal site-packages is not writeable
Collecting freegames
  Using cached freegames-2.4.0-py3-none-any.whl (108 kB)
Installing collected packages: freegames
Successfully installed freegames-2.4.0
```

Free Python Games oferece uma interface de linha de comando, cuja ajuda está
disponível com:

```shell
$ python3 -m freegames --help
usage: freegames [-h] {list,copy,show} ...

Free Python Games

positional arguments:
  {list,copy,show}  sub-command help
    list            list games
    copy            copy game source code
    show            show game source code

options:
  -h, --help        show this help message and exit

Copyright 2022 Grant Jenks
```

Como apresentado acima, a interface de linha de comando possui 3 comandos: 
*list*, *copy* e *show*. Para listar todos os jogos disponíveis, execute:

```shell
$ python3 -m freegames list
ant
bagels
bounce
cannon
connect
crypto
fidget
flappy
guess
life
madlibs
maze
memory
minesweeper
pacman
paint
pong
simonsays
snake
tictactoe
tiles
tron
```

Para executar qualquer um dos jogos listados, pasta combinar “freegames” com o 
nome do jogo. Por exemplo, para jogar "snake", execute e divirta-se: 

```shell
$ python3 -m freegames.snake
```

Para modificar os jogos, você deve fazer uma cópia do código-fonte. O comando 
*copy* irá criar um arquivo Python em seu diretório local, que você poderá
editar. Por exemplo, para copiar e executar "pacman", execute:

```shell
$ python3 -m freegames copy pacman
$ python3 pacman.py
```

Agora, você pode abrir o arquivo *pacman.py*  com seu editor preferido. Ou 
utilizar a linha de comando abaixo e abrir com o editor chamado IDLE que vem
embutido com Python:

```shell
$ python3 -m idlelib.idle pacman.py
```

Por fim, você também pode acessar a documentação com a função Python embutida ```help```

```python
$ python3
>>> import freegames
>>> help(freegames)
```

## Referências

[Free Python Games](https://grantjenks.com/docs/freegames/)

[pip (gerenciador de pacotes)](https://pt.wikipedia.org/wiki/Pip_(gerenciador_de_pacotes))

[Anterior](04_indo_alem/06_melhorando_o_editor.md) | [Próximo](02_fpg_paint.md)
