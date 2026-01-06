# Pacman

O Pacman é o jogo mais rico da coleção para trabalhar:
- modelagem de mundo discreto,
- múltiplos agentes autônomos,
- colisão, estado global e laço temporal.

Conjuntamente, os exercícios avaliam:
- Leitura e compreensão de código existente
- Manipulação consciente de estado e lógica
- Coerência entre dados, regras e visualização
- Capacidade de intervenção incremental em sistemas interativos

[Versão do professor](pacman_prof.py) | [Versão do aluno](pacman.py)


## Exercícios propostos

### TODO 1 – Evitar rastro do objeto escritor

- **Conceitos:** penup/pendown, controle de desenho, objetos gráficos.
- **Racional:** avalia se o aluno distingue deslocamento de desenho e entende
o uso de objetos auxiliares para interface.
- **Avalia:** compreensão do comportamento da turtle ao se mover e desenhar e
capacidade de identificar efeitos colaterais visuais no código.
- **Nível:** básico

### TODO 2 – Remover a comida após ser coletada

- **Conceitos:** estruturas de dados, estado do jogo, atualização gráfica.
- **Racional:** Verifica se o aluno compreende que alterações no estado devem
refletir imediatamente na interface.
- **Avalia:** capacidade de relacionar dados internos (tiles) com a visualização
e entendimento de eventos e consequências no jogo
- **Nível:** intermediário

### Exercício 1 – Alterar o tabuleiro

- **Conceitos:** listas, indexação, representação espacial, mapeamento 2D → 1D.
- **Avalia:** compreensão de estruturas de dados que representam o mundo do jogo
e capacidade de relacionar dados abstratos com o espaço visual
- **Racional:** avalia se o aluno entende que o cenário do jogo é uma construção
lógica e manipulável, não algo fixo ou “desenhado manualmente”.
- **Nível:** intermediário

### Exercício 2 – Alterar a quantidade de fantasmas

- **Conceitos:** listas, composição de dados, laços.
- **Avalia:** manipulação de coleções de objetos e entendimento da relação entre
quantidade de dados e comportamento emergente
- **Racional:** reforça a noção de escalabilidade do código e introduz a ideia
de que o mesmo algoritmo pode operar sobre diferentes tamanhos de conjuntos.
- **Nível:** básica a intermediário

### Exercício 3 – Alterar a posição inicial do Pacman

- **Conceitos:** variáveis, coordenadas, estado inicial.
- **Avaia:** leitura e interpretação de código de inicialização e capacidade de
identificar pontos de configuração do sistema
- **Racional:** trabalha a distinção entre lógica do jogo e parâmetros iniciais,
habilidade essencial para personalização e testes
- **Nível:** básico

### Exercício 4 – Alterar a velocidade dos fantasmas

- **Conceitos:** vetores, tempo, parâmetros de movimento.
- **Avalia:** compreensão do modelo de movimento baseado em vetores e capacidade
de ajustar dinamicamente o comportamento de agentes
- **Racional:** introduz a noção de que velocidade é um parâmetro lógico, não
visual, reforçando o controle matemático do movimento.
- **Nível:** intermediário

### Exercício 5 – Tornar os fantasmas mais inteligentes

- **Conceitos:** tomada de decisão, lógica condicional, heurísticas simples,
comportamento de agentes.
- **Avalia:** capacidade de projetar lógica além do comportamento aleatório e
raciocínio algorítmico aplicado a problemas abertos
- **Racional:** Estimula pensamento computacional de nível mais alto, aproximando
o aluno de conceitos iniciais de inteligência artificial e design de algoritmos.
- **Dificuldade:** avançado
