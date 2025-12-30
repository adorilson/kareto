# Pong

O Pong é um artefato didático para trabalhar programação interativa baseada em
simulação, com foco em:
1. Movimento contínuo em duas dimensões
1. Atualização de estado em laço principal
1. Colisão e reflexão
1. Controle por eventos (teclado)
1. Sincronização entre múltiplos objetos ativos

Diferentemente do Simon Diz (memória sequencial) e do Campo Minado (análise
discreta e espacial), o Pong introduz o aluno a um modelo de mundo em tempo
contínuo, no qual o estado do sistema evolui frame a frame.

**Competência centrais**

Do ponto de vista pedagógico, Pong permite avaliar:
1. Noção de estado global do jogo
1. Separação entre modelo (lógica) e visualização
1. Coordenação entre entrada do usuário, movimento automático e regras físicas simples
1. Pensamento algorítmico aplicado a sistemas dinâmicos

**Tópicos de aprendizagem explorados**
1. Variáveis que representam posição e velocidade
1. Atualização incremental (x = x + dx, y = y + dy)
1. Condicionais encadeadas
1. Eventos de teclado
1. Detecção de colisão
1. Reinicialização de estado

O Pong funciona como uma **ponte conceitual** entre jogos puramente lógicos e
jogos com comportamento físico, preparando o aluno para temas como animação,
jogos em tempo real e, posteriormente, simulações mais complexas.

[Versão do professor](pong_prof.py) | [Versão do aluno](pong.py)

## Exercícios propostos

### TODO 1 - Desenhar a segunda raquete

**Conceitos:** chamada de funções e parâmetros
**Racional:** força o aluno a identificar um padrão funcional existente e reproduzi-lo
**Avalia:** leitura e compreesão de código, reconhecimento de padrões

### Exercício 1 — Alterar cores do jogo

**Conceitos:** parâmetros gráficos, estado visual
**Racional:** pequenas mudanças visuais ajudam a localizar funções gráficas
**Avalia:** leitura e modificação de código existente

### Exercício 2 — Frame rate

**Conceitos:** tempo, ontimer, execução assíncrona
**Racional:** explicita que não há laço infinito, mas sim agendamento temporal
**Avalia:** compreensão de fluxo controlado por eventos

### Exercício 3 — Velocidade da bola

**Conceitos:** vetores, magnitude, aleatoriedade
**Racional:** conecta matemática simples ao comportamento do jogo
**Avalia:** manipulação de dados numéricos

### Exercício 4 — Tamanho das raquetes

**Conceitos:** parâmetros, colisão geométrica
**Racional:** mostra dependência entre visual e lógica
**Avalia:** coerência entre representação e regra do jogo

### Exercício 5 — Rebote nas paredes

**Conceitos:** condicionais, física simplificada
**Racional:** promove experimentação e raciocínio causal
**Avalia:** entendimento de controle de fluxo

**Exercício 6** — Jogador computador

**Conceitos:** automação, lógica condicional
**Racional:** introduz comportamento artificial simples
**Avalia:** decomposição de problema

### Exercício 7 — Segunda bola

**Conceitos:** listas, múltiplos estados, generalização
**Racional:** força o aluno a sair do código “hardcoded”
**Avalia:** abstração e escalabilidade

## Classificação por nível de dificuldade
🟢 Nível básico
1. Alterar as cores do jogo
- Envolve apenas parâmetros gráficos.
- Não interfere na lógica do jogo.

2. Alterar a velocidade da bola
- Modificação direta de valores numéricos.
- Efeito imediato e visualmente claro.

3. Alterar o tamanho das raquetes
- Mudança simples de parâmetros.
- Exige pequena atenção à coerência com a colisão.

🟡 Nível intermediário

4. Alterar o frame rate (velocidade do jogo)
- Introduz explicitamente o papel do tempo (ontimer).
- Exige compreender que não há laço while.

5. Modificar como a bola rebate nas paredes
- Envolve lógica condicional.
- Possibilita variações (ângulo, aceleração, imprevisibilidade).

🔴 Nível avançado

6. Adicionar um jogador controlado pelo computador
- Introduz automação e tomada de decisão.
- Exige leitura contínua do estado do jogo.

7. Adicionar uma segunda bola
- Exige refatoração do código.
- Introduz múltiplas entidades, listas e generalização da lógica.

