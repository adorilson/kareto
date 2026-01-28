# Labirinto

Neste jogo, é explorada a ideia de labirintos gerados proceduralmente,
utilizando decisões aleatórias para criar padrões diferentes a cada execução.
O jogador não controla um personagem tradicional, mas desenha seu próprio caminho,
o que reforça a relação entre entrada do usuário, estado gráfico e resposta visual
imediata.

O jogo é especialmente adequado para introduzir:
- eventos de mouse,
- estruturas de repetição aninhadas,
- uso de aleatoriedade,
- noções de limites espaciais.

[Versão do professor](labirinto_prof.py) | [Versão do aluno](labirinto.py)


## Exercícios propostos

### TODO 1 - Chamar a função que desenha o labirinto
- **Conceitos:** Fluxo de execução, chamada de funções.
- **Racional:** Evidenciar que funções precisam ser chamadas para produzir efeito no programa.
- **Avalia:** Compreensão da ordem de execução do código.
- **Nível:** Básico

### TODO 2 - Completar a linha alternativa do labirinto
- **Conceitos:** Coordenadas, chamada de função, geometria básica.
- **Racional:** Compreender como o padrão visual do labirinto é formado a partir de linhas com diferentes orientações.
- **Avalia:** Leitura de código e uso correto de parâmetros geométricos.
- **Nível:** Básico

### TODO 3 - Associar o clique do mouse à função de toque

- **Conceitos:** Eventos, callbacks, interação gráfica.
- **Racional:** Introduzir programação orientada a eventos por meio de interação direta com o usuário.
- **Avalia:** Uso correto de tratamento de eventos e ligação ação–resposta.
- **Nível:** Básico

### Exercício 1 - Manter pontuação contando os cliques (e tempo).

- **Conceitos:**  variáveis de estado, eventos, contadores
- **Racional:**  introduz persistência de dados em jogos orientados a eventos
- **Avalia:**  compreensão de estado global e atualização incremental
- **Nível:** Básico

### Exercício 2 - Gerar o mesmo labirinto duas vezes.

- **Conceitos:** semente aleatória (seed), determinismo
- **Racional:** introduz controle da aleatoriedade e reprodutibilidade
- **Avalia:**  compreensão de aleatoriedade controlada
- **Nível:** Intermediário

### Exercício 3 - Permitir que o jogador desfaça o último movimento

- **Conceitos:** Funções da biblioteca (turtle.undo), pilha interna de ações, eventos de teclado.
- **Racional:** Mostrar ao aluno que bibliotecas frequentemente oferecem abstrações prontas para resolver problemas comuns, evitando reimplementações desnecessárias e reforçando o uso consciente de APIs.
- **Avalia:**  Capacidade de identificar, compreender e aplicar corretamente uma função existente da biblioteca.

- **Nível:** Básico - Intermediário

### Exercício 4 - Fazer com que o caminho percorrido seja gradualmente.

- **Conceitos:** Controle de animação (turtle.tracer), velocidade de execução (turtle.speed), renderização incremental.
- **Racional:** Evidenciar que o tempo e a atualização da tela são variáveis controláveis, permitindo transformar um traço instantâneo em uma animação progressiva e compreensível para o jogador.
- **Avalia:** Compreensão do ciclo de desenho da Turtle e uso adequado de funções de controle visual.
- **Nível:** Intermediário


## Exercício 5 - Evitar que no primeiro clique seja feito um traço.

- **Conceitos:** Controle de animação (turtle.tracer), velocidade de execução (turtle.speed), renderização incremental.
- **Racional:** Evidenciar que o tempo e a atualização da tela são variáveis controláveis, permitindo transformar um traço instantâneo em uma animação progressiva e compreensível para o jogador.
- **Avalia:** Compreensão do ciclo de desenho da Turtle e uso adequado de funções de controle visual.
- **Nível:** Intermediário
