# Pacman Orientado a Objetos

Assim como para `Snake`, foi feito uma análise do código da versão estruturada de
Pacman, identificando suas variáveis e funções relacionadas. Dessa análise, foram
identificadas classes que melhor representariam os conceitos deste jogo. Das
variáveis existentes, duas merecem destaque:

- pacman: essa variável na versão estruturada é um `vector`, mas poderia
ser um `Pacman`. Além de encapsular sua posição e operações relacionadas, a classe
poderia conter tanto outros atributos (como direção e estado - vivo ou morto)
quanto ações de mais alto nível, ou seja, ações pertinentes a um `Pacman` e não
a um `vector`, tais como morrer, virar para esquerda ou direita, calcular a próxima
posição.
- ghosts: essa variável é uma lista de `vector`, mas poderia ser uma lista de
`Ghost`. Para os fantasmas são necessários apenas duas ações: mover
e mudar de direção, além de possuir os atributos de posição e direção.

Além de uma classe `GamePacman` que faria a orquestração das classes anteriores
e desenho e atualização da tela. Essa classe conteria, principalmente mas não
só isso, as ações feitas na função `move` da versão estruturada, mas distribuídas
em diversos métodos.

[Anterior](06_poo_snake.md) | [Próximo](07_poo_pacman.md)
