# Campo minado

Este jogo permite trabalhar vários conceitos, funcionando como um
micro-laboratório de programação imperativa, no qual o aluno precisa dominar:
1. O estado do programa é distribuído em múltiplas estruturas mutáveis
(tabuleiro, bombas, células reveladas e contagens)
1. A representação de um problema espacial por meio de estruturas de dados
(uso de dicionários para mapear coordenadas em uma grade)
1. A relação entre regra do jogo e lógica do algoritmo
(posicionamento de bombas, contagem de vizinhos e condições de fim de jogo)
1. O uso integrado de laços aninhados e condicionais para percorrer e analisar vizinhanças
1. Eventos e interação como disparadores da lógica do programa
(o clique do jogador determina o fluxo de execução)
1. Propagação de efeitos lógicos
(revelação automática de células quando não há bombas adjacentes)
1. A importância de invariantes e validações de estado
(evitar sobreposição de bombas e acessos inválidos ao tabuleiro)

[Versão do professor](campo_minado_prof.py) [Versão do aluno](campo_minado.py)

## Exercícios propostos

### 1 - Controle da aleatoriedade com seed

- **Enunciado**
O que faz a chamada da função `seed(0)`?

- **Conceitos**
1. Geração de números pseudoaleatórios
1. Função `seed` do módulo `random`
1. Reprodutibilidade de resultados
1. Depuração e testes

- **Racional pedagógico**
Este exercício introduz a ideia de que “aleatoriedade” em programação é, na
prática, **pseudoaleatoriedade controlável**. Ao observar que o tabuleiro
gerado é sempre o mesmo quando `seed(0)` está presente, o aluno passa a compreender que:
- o comportamento do jogo pode ser reproduzido;
- isso é útil para testes, depuração e ensino.

É um conceito sofisticado, mas apresentado de forma concreta e visual, alinhado ao perfil do projeto.

- **Avalia**
1. Compreensão conceitual de aleatoriedade controlada
1. Capacidade de relacionar uma chamada de função ao comportamento global do sistema
1. Leitura crítica de código existente

### 2 - Alteração da quantidade de bombas

- **Enunciado**
Como alterar a quantidade de bombas no tabuleiro?

- **Conceitos envolvidos**
1. Laços de repetição (for)
1. Uso de variáveis como parâmetros de configuração
1. Relação entre lógica de jogo e dificuldade
1. Leitura e modificação de código existente

- **Racional pedagógico**

O exercício leva o aluno a identificar **onde a regra do jogo está codificada**
(o for _ in range(8)), promovendo:
- entendimento de que valores “mágicos” controlam o comportamento do sistema;
- percepção de que pequenas alterações podem ter impacto significativo na
jogabilidade.

Além disso, abre espaço para discutir boas práticas, como substituir constantes
por variáveis nomeadas.

- **Avalia**
1. Capacidade de localizar e interpretar um trecho relevante do código
1. Entendimento do papel de laços na lógica do jogo
1. Autonomia para modificar parâmetros sem quebrar o funcionamento geral

### 3 - Alteração do tamanho do tabuleiro

- **Enunciado**
Como alterar o tamanho do tabuleiro?

- **Conceitos envolvidos**
1. Intervalos em range
1. Sistema de coordenadas
1. Representação espacial em grade
1. Coerência entre lógica e interface gráfica

- **Racional pedagógico**

Este exercício exige uma leitura **mais global** do código, pois o tamanho do
tabuleiro não está definido em um único ponto. O aluno precisa perceber que:
- os `range` em inicializar, desenhar_tabuleiro e fim_de_jogo precisam ser coerentes;
- há uma relação direta entre dimensões do tabuleiro e área da janela (`setup`).

Isso promove pensamento sistêmico e atenção à consistência interna do programa.

- **Avalia**
1. Capacidade de identificar dependências entre diferentes partes do código
1. Entendimento da representação de estruturas bidimensionais
1. Cuidado com coerência e efeitos colaterais de mudanças

### 4 - Substituição do símbolo por imagem (bomba)

- **Enunciado**
Como exibir a imagem de uma bomba no lugar do X?

- **Conceitos envolvidos**
- Uso de imagens (ou Unicode/emoji) no turtle
- Separação entre lógica e apresentação
- Funções gráficas
- Customização visual do jogo

- **Racional pedagógico**
Aqui o foco deixa de ser apenas lógico e passa para a interface visual,
reforçando que:

- o jogo tem uma camada de apresentação independente da lógica;
- símbolos textuais podem ser substituídos por representações gráficas mais
ricas.

É um exercício motivador, que aproxima o aluno de práticas reais de
desenvolvimento de jogos.

- **Avalia**
1. Capacidade de explorar documentação e exemplos
1. Compreensão da camada gráfica do programa
1. Criatividade aplicada com controle técnico

### Exercício 5 - Evitar sobreposição de bombas

- **Enunciado**
Como evitar sobreposição de bombas?

- **Conceitos envolvidos**
1. Estruturas de dados (dicionários)
1. Condições (if)
1. Controle de estado
1. Lógica de validação

- **Racional pedagógico**

Este é um exercício de **refinamento lógico**. O jogo funciona mesmo com
sobreposição, mas o aluno é levado a perceber que:
- nem todo erro gera uma falha visível;
- regras implícitas do jogo precisam ser garantidas pelo código.

É uma introdução importante à ideia de invariantes e validações em sistemas
interativos.

- **Avalia**
1. Raciocínio lógico
1. Capacidade de antecipar problemas de estado
1. Uso adequado de estruturas de dados para verificação

## Exercício 6 - Configuração do número de bombas pelo jogador

- **Enunciado**
Como permitir que o jogador configure o número de bombas?

- **Conceitos envolvidos**
1. Entrada de dados (variáveis de configuração)
1. Parametrização de funções
1. Separação entre configuração e execução
1. Usabilidade básica

- **Racional pedagógico**

Este exercício consolida a ideia de que programas não precisam ser rígidos. Ele
estimula o aluno a:
- transformar valores fixos em parâmetros;
- pensar no usuário como agente ativo;
- reorganizar o código para torná-lo mais flexível.

Didaticamente, é um excelente fechamento, pois exige reorganização, não apenas edição pontual.

- **Avalia**
1. Capacidade de abstração
1. Organização de código
1. Visão de software como sistema configurável

## Exercício 7 - Implementação do fim de jogo

- **Enunciado**
Implemente a função que revela todas as bombas quando o jogador perde.

- **Conceitos envolvidos**
1. Varredura completa de estruturas de dados
1. Condicionais
1. Separação de responsabilidades (detecção × reação)

- **Racional pedagógico**
Este exercício reforça que eventos de erro (derrota) precisam ser tratados
explicitamente. O aluno aprende a responder a uma condição global a partir de
estados locais.

- **Avalia**
1. Laços aninhados
1. Funções
1. Separação entre lógica e apresentação
1. Reutilização de funções (carimbar)

## Exercício 8 - Integração do fim de jogo ao clique

- **Enunciado**
Complete o tratamento do clique em uma bomba, chamando a função de fim de jogo.

- **Conceitos envolvidos**
1. Eventos
1. Chamadas de função
1. Fluxo de execução
1. Condições de parada

- **Racional pedagógico**
Este TODO conecta detecção de estado com resposta do sistema. Ele evidencia a
diferença entre identificar uma condição e agir sobre ela.

- **Avalia**
1. Entendimento de eventos como gatilhos
1. Capacidade de encadear funções
1. Controle explícito do fluxo do programa


## Melhorias esperadas por nível de dificuldade

- **Nível básico**
1. O que faz a chamada `seed(0)`?
1. Alterar a quantidade de bombas

- **Nível intermediário**
1. Alterar o tamanho do tabuleiro
1. Implementar o fim de jogo
1. Integrar o fim de jogo ao clique

- **Nível avançado**
1. Evitar sobreposição de bombas
1. Exibir imagem de bomba no lugar do X
1. Permitir que o jogador configure o número de bombas
