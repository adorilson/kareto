# Flappy

Este jogo permite trabalhar conceitos de programação imperativa e orientada a
eventos em um contexto dinâmico e visual. Ele funciona como um micro-laboratório
para discutir:
1. Estado mutável (posição do pássaro e dos obstáculos)
1. Laço de animação com tempo discreto
1. Eventos assíncronos (clique do mouse)
1. Detecção de colisão
1. Controle de fluxo por condições de erro (game over)

O aluno deve ser capaz de observar como pequenas alterações em regras e parâmetros
impactam diretamente o comportamento do sistema.

[Versão do professor](flappy_prof.py) | [Versão do aluno](flappy.py)

## Exercícios propostos

### TODO 1 - Alterar a cor do pássaro conforme o estado

- **Conceitos:** condicionais, variável de estado, parâmetros visuais.
- **Racional:** relacionar estado lógico do jogo à representação visual.
- **Avalia:** leitura de código, uso correto de if/else, modificação simples de
comportamento gráfico.
- **Nível:** básico–intermediário.

### TODO 2 - Remover bolas quando estão fora da tela

- **Conceitos:** listas, acesso por índice, remoção de elementos, laços while.
- **Racional:** evitar crescimento indefinido da lista e garantir o fluxo
correto do jogo. Além de evitar repetição infinita. Isso é o que causa o
travamento do jogo. Observe que é sempre quando a primeira bola chega no lado
esquerdo da tela.
- **Avalia:** compreensão de estruturas de dados, identificação de causa de
erro lógico e correção simples.
- **Nível:** intermediário.

### Exercício 1 — Manter e exibir pontuação

- **Conceitos:** variáveis globais, estado persistente, atualização incremental
- **Racional:** introduz acompanhamento de progresso e feedback ao jogador
- **Avalia:** compreensão de estado e atualização ao longo do tempo
- **Nível:** básico

### Exercício 2 — Variar velocidade

- **Conceitos:** parâmetros temporais (ontimer), constantes, abstração
- **Racional:** evidencia tempo como variável de controle
- **Avalia:** capacidade de localizar e ajustar parâmetros de execução
- **Nível:** básico

### Exercício 3 — Variar tamanho das bolas

- **Conceitos:** parâmetros gráficos, colisão dependente de escala
- **Racional:** mostra impacto visual e lógico de um mesmo parâmetro
- **Avalia:** consistência entre visual e lógica de colisão
- **Nível:** intermediário

### Exercício 4 — Movimento horizontal do pássaro

- **Conceitos:** vetores, eventos, controle bidimensional
- **Racional:** amplia o modelo mental do jogador/objeto
- **Avalia:** domínio de vetores e eventos adicionais
- **Nível:** intermediário