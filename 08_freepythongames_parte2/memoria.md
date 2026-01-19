# Memória

Neste jogo, o aluno implementa uma versão do Jogo da Memória, em que o objetivo é encontrar pares de peças escondidas no tabuleiro. Cada clique do mouse revela uma peça e o jogo controla quais pares permanecem visíveis.

Do ponto de vista computacional, o jogo explora a relação entre interação gráfica e estado interno, usando listas para representar o tabuleiro, um dicionário para armazenar o estado do jogo e funções para converter cliques em posições lógicas.

Os exercícios propostos permitem trabalhar, de forma progressiva, conceitos como eventos, estruturas de dados, controle de estado e atualização da tela, tornando o jogo um bom exemplo de programação interativa com feedback visual imediato.

[Versão do professor](memoria_prof.py) | [Versão do aluno](memoria.py)

## Exercícios propostos

### TODO 1 - Corrigir função quadrado

- **Conceitos:** funções, parâmetros, coordenadas cartesianas, laços de repetição, abstração geométrica
- **Racional:** o exercício força o aluno a compreender que uma função deve ser genérica e reutilizável, respeitando seus parâmetros (x, y) em vez de usar valores fixos. Ele também consolida a noção de desenho geométrico baseado em deslocamentos relativos e dimensão fixa (lado de 50 pixels).
- **Avalia:** Capacidade de interpretar especificações, usar parâmetros corretamente e relacionar código com o resultado visual esperado.
- **Nível:** Básico → Intermediário

### TODO 2 - Associar o clique do mouse à função toque

- **Conceitos:** eventos, callbacks, interação com mouse, associação função–evento
- **Racional:** o exercício introduz explicitamente o modelo de programação orientada a eventos do turtle, levando o aluno a compreender que a lógica do jogo só reage a ações do usuário quando funções são registradas como manipuladores de eventos.
- **Avalia:** Compreensão do mecanismo de eventos do turtle e a habilidade de conectar uma função existente a uma interação do usuário.
- **Nível:** Básico


### Exercício 1 — Contar e exibir quantos cliques ocorreram

- **Conceitos:** eventos, variáveis, contadores, estado do jogo.
- **Racional:** introduz a instrumentação do jogo por meio da contagem de ações do jogador
- **Avalia:** uso de variáveis e resposta a eventos de entrada
- **Nível:** básico

### Exercício 2 — Reduzir o tabuleiro para uma tabuleiro 4×4

- **Conceitos:** listas, índices, organização espacial, relação dados–tela.
- **Racional:** evidencia a ligação entre estrutura de dados e representação visual.
- **Avalia:** compreensão de estado e atualização ao longo do tempo
- **Nível:** básico

### Exercício 3 — Detectar quando todas as peças foram reveladas

- **Conceitos:** booleanos, listas, condições, estado final.
- **Racional:** Introduz a definição de condição de término de um jogo.
- **Avalia:** Raciocínio lógico e leitura de estados globais.
- **Nível:** Intermediário

### Exercício 4 — Centralizar peças de um único dígito

- **Conceitos:** Coordenadas, alinhamento visual, ajuste fino.
- **Racional:** Trabalha percepção visual e precisão no posicionamento gráfico.
- **Avalia:** Controle de coordenadas e atenção à interface.
- **Nível:** Intermediário

### Exercício 5 — Usar letras em vez de números

- **Conceitos:** Strings, listas, abstração de dados
- **Racional:** Mostra que a lógica do jogo é independente do tipo de dado exibido.
- **Avalia:** Generalização e adaptação de estruturas de dados.
- **Nível:** Básico → Intermediário



