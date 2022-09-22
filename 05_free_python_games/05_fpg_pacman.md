# Pacman, classic arcade game.

Analise o código do Pacman e resolva os exercícios propostos, cujas
traduções livres são:

1. Mude o tabuleiro
1. Mude o número de fantasmas
1. Mude onde o Pacman inicia
1. Faça os fantasmas serem mais lentos/rápidos
1. Faça os fantasmas serem mais inteligentes

Todos os exercícios propostos são relativos ao funcionamento do jogo,
perceptível para o usuário. Porém, também é possível melhorar a qualidade do código, que não será perceptível ao usuário, mas deixará o código com melhor
manutenabilidade. Assim, faça mais alguns exercícios que podem atender a um ou
outro desses aspectos.

1. Mude as cores
1. Os vetores de referências estão espalhados pelo código, caso seja preciso
modificá-los, terá de fazer em múltiplos locais. Você deverá criar constantes
com esses valores e utilizadas no lugar
1. O código possui uma linha com `for index in range(len(tiles)):`. O uso
de `range(len(tiles))` é uma má prática. Melhore esse código utilizando a função
embutida ` enumerate(iterable, start=0)`
1. Identifique a variável responsável por escrever a pontuação. Análise se 
poderia ter um melhor nome e mude se for o caso
1. Faça o jogo parar caso Pacman coma todas as frutinhas, exibindo alguma 
indicação de Winner!


![Pacman](https://grantjenks.com/docs/freegames/_static/pacman.gif
"Pacman")

[Anterior](04_fpg_tictactoe.md) | [Próximo](05_fpg_pacman.md)
