# Tron

Neste jogo, inspirado no clássico **Tron**, dois jogadores controlam “motos de
luz” que se movem continuamente, deixando um rastro permanente. O objetivo é
**não colidir** com as bordas da tela nem com o rastro do adversário (e,
futuramente, com o próprio rastro).

O jogo explora conceitos fundamentais de programação como **movimento vetorial,
eventos de teclado, estruturas de dados, laços temporizados e detecção de colisões**,
servindo como base para extensões progressivamente mais complexas.

[Versão do professor](tron_prof.py) | [Versão do aluno](tron.py)

## Exercícios propostos

### TODO 1 – Cores diferentes para os jogadores

- **Conceitos:** parâmetros de funções, representação visual do estado,
separação lógica/visual.
- **Racional:** permite compreender que a lógica do jogo é independente da forma
como os elementos são desenhados. Introduz a ideia de camadas (comportamento ×
apresentação) com feedback visual imediato.
- **Avalia:** leitura de código, uso de parâmetros e modificação pontual sem quebrar
a lógica existente.
- **Nível:** básico

### TODO 2 – Configurar teclas do jogador 2

- **Conceitos:** programação orientada a eventos, funções de retorno, mapeamento
de teclado, reutilização de padrões.
- **Racional:** consolida o modelo de eventos e mostra como a mesma lógica
pode ser acionada por entradas diferentes. Estimula reconhecimento e
generalização de padrões já existentes no código.
- **Avalia:** compreensão do `onkey`, associação correta entre tecla e função e
replicação consciente de uma solução existente.
- **Nível:** básico–intermediário

### Exercício 1 – Ajustar velocidade dos jogadores

- **Conceitos:** temporização (`ontimer`), vetores, taxa de atualização
- **Racional:** introduz controle explícito do tempo no jogo, mostrando que
velocidade não depende apenas do deslocamento, mas também da frequência de atualização.
- **Avalia:** compreensão de tempo discreto e parâmetros de execução.
- **Nível:** básico (envolve apenas ajuste de parâmetros já existentes - `ontimer`,
vetor de direção)

### Exercício 2 – Colisão com o próprio rastro

- **Conceitos:** `set`, comparação de objetos, colisão lógica
- **Racional:** reforça o uso de estruturas de dados adequadas para testes de
pertencimento eficientes
- **Avalia:** modelagem de estado e raciocínio condicional
- **Nível:** intermediário (requer entender como o rastro é armazenado (`set`)
e como a verificação de colisão)

### Exercício 3 – Atravessar bordas da tela

- **Conceitos:** coordenadas, aritmética modular, lógica espacial
- **Racional:** desloca o aluno de uma validação simples para uma transformação
de estado mais sofisticada.
- **Avalia**: manipulação de coordenadas e pensamento matemático
- **Nível:** intermediário (exige reformular a lógica de validação espacial)

### Exercício 4 – Jogador controlado pelo computador

- **Conceitos:** heurísticas, tomada de decisão, automação
- **Racional:** introduz IA simples baseada em regras, sem exigir algoritmos
complexos
- **Avalia:** abstração, planejamento e lógica algorítmica.
- **Nível:** avançado (envolve tomada de decisção automática, exigindo projeto
algorítmico)

### Exercício 5 – Tornar as mensagens de vitória mais visuais

- **Conceitos:** saída gráfica, uso do turtle para texto, estado final do jogo,
separação entre lógica e apresentação.
- **Racional:** leva o aluno a substituir uma saída textual (print) por uma
representação gráfica coerente com o restante do jogo.
- **Avalia:** capacidade de identificar pontos de finalização do jogo, usar a
API gráfica para exibir informações e integrar apresentação visual sem alterar
a mecânica central.
- **Nível:** intermediário
