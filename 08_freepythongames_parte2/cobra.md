# Cobra

Esse jogo permite trabalhar vários conceitos, funcionando como um micro-laboratório de programação
imperativo, no qual o aluno precisa dominar: 
1. O **estado** do programa é mutável e visível
1. Erros lógicos geram comportamentos claros
1. Trabalha listas, funções eventos e condicionais de forma integrada
1. Sequência de execução
1. Tempo como variável de controle

[Versão do professor](cobra_prof.py) [Versão do aluno](cobra.py)

## Exercícios propostos

### 1 - Controlando a velocidade da cobra

- **Enunciado**
Altere o valor do temporizador para deixar a cobra mais rápida e depois mais lenta.

- **Conceitos**
1. Parâmetros
1. Tempo de execução
1. Relação causa-efeito visível

- **Racional pedagógico**
O aluno percebe imediatamente o impacto de um número no comportamento do programa.

- **Avalia**
1. Interpretação de parâmetros
1. Noção de tempo discreto
1. Controle indireto de fluxo

É um bom gancho para discutir:
`Velocidade não é movimento maior, é atualização mais frequente`

### 2 - Cobra atravessando as bordas

- **Enunciado**
Modifique a função `dentro_limites` (ou a lógica do movimento) para que a cobra
reapareça do outro lado da tela ao sair dos limites.

- **Conceitos**
1. Condicionais
1. Coordenadas
1. Regras de jogo

- **Racional**
Introduz a ideia de regra alternativa sem alterar a estrutura geral do programa.

- **Avalia**
1. Expressões booleanas
1. Operadores lógicos
1. Uso de função que retorna booleano
1. Teste de pertencimento (`in`)

- **Erro comum**
1. Testar colisão depois de alterar a lista
1. Não entender por que `cabeca in cobra` funciona

### 3 - Comida em movimento

- **Enunciado**
Faça a comida mudar de posição automaticamente a cada certo tempo.

- **Conceitos**
1. Variáveis
1. Funções
1. Temporização
1. Aleatoriedade

- **Racional**
Mostra que não só o jogador, mas o próprio jogo pode ter comportamento ativo.

### 4 - Controle por mouse

- **Enunciado**
Altere o jogo para que a direção da cobra seja definida pela posição do clique do mouse.

- **Conceitos**
1. Eventos
1. Coordenadas do mouse
1. Mapeamento de entrada → ação

- **Racional**
Expande o repertório de interação sem exigir novos conteúdos sintáticos complexos.

### 5 - Crescimento da cobra

- **Avalia**
1. Relação entre append e pop
1. Lógica de crescimento condicionado
1. Diferença entre lista fixa e lista dinâmica

Esse trecho contribui para o raciocínio algorítmico.

## Melhorias esperadas por nível de dificuldade

- **Nível básico**
1. Jogo funcional
1. Cobra cresce
1. Controle por teclado

- **Nível intermediário**
1. Ajuste dinâmico de velocidade
1. Bordas atravessáveis
1. Comida móvel

- **Nível avançado**
1. Controle por mouse
1. Pontuação
1. Regras alternativas
