# Simon Diz

Este jogo funciona como um micro-laboratório de programação imperativa, no qual
o aluno precisa dominar:
1. Estado mutável e memória (o padrão cresce e precisa ser lembrado)
1. Sequência de execução controlada por eventos
1. Comparação entre entrada do usuário e estado interno
1. Tempo como elemento lógico do programa
1. Integração entre lógica, interação e visualização

Simon Diz enfatiza memória sequencial, repetição e sincronização temporal.

[Versão do professor](simondiz_prof.py) | [Versão do aluno](simondiz.py)

## Exercícios propostos

### 1 — Acelerar a taxa de piscada dos azulejos

**Enunciado** Altere o tempo de espera usado na função piscar para tornar o
jogo mais rápido.

**Conceitos envolvidos**
1. Funções
1. Uso de constantes
1. Tempo (sleep)
1. Sequência de execução

**Racional pedagógico**
O aluno aprende que o tempo também é **um parâmetro de controle lógico**, e não
apenas um detalhe estético. A atividade mostra como pequenas alterações podem
impactar significativamente a jogabilidade.

**Avalia**
1. Capacidade de identificar parâmetros implícitos
1. Compreensão da relação entre código e experiência do usuário

### 2 — Adicionar mais azulejos ao jogo

**Enunciado**
Adicione novos azulejos ao tabuleiro, expandindo o dicionário azulejos.

**Conceitos envolvidos**
1. Dicionários
1. Abstração
1. Escalabilidade
1. Generalização de código

**Racional pedagógico**
Este exercício evidencia que o jogo foi estruturado para ser extensível.
O aluno percebe que decisões de modelagem (uso de dicionário) facilitam
crescimento sem reescrita da lógica.

**Avalia**
1. Capacidade de trabalhar com estruturas de dados
1. Entendimento de separação entre dados e lógica

## 3 — TODO Desenhar a grade inicial

Local no código
```python
def grade():
    # TODO: Percorra o dicionário azulejos
```

**Enunciado**
Implemente a função que desenha todos os azulejos do tabuleiro usando suas
cores escuras.

**Conceitos envolvidos**
1. Laços
1. Dicionários
1. Funções
1. Visualização de estado

**Racional pedagógico**
O aluno aprende que o estado inicial do programa precisa ser explicitamente
representado. A grade não “existe” até que seja desenhada a partir dos dados.

**Avalia**
1. Uso correto de laços
1. Leitura de estruturas de dados
1. Relação entre estado interno e interface


### 4 — TODO Implementar o efeito de piscar
Local no código
```python
def piscar(pos):
    # TODO: desenhar claro, esperar, desenhar escuro
```

**Enunciado**
Implemente o efeito de piscar de um azulejo, alternando cores com pausas.

**Conceitos envolvidos**
1. Sequência de instruções
1. Tempo (sleep)
1. Funções
1. Atualização da tela

**Racional pedagógico**
Este TODO introduz explicitamente o tempo como parte da lógica do programa,
reforçando que a ordem das instruções é essencial para o efeito desejado.

**Avalia**
1. Compreensão de execução sequencial
1. Capacidade de coordenar efeitos visuais e temporais

### ~~5 — TODO Verificar o clique do jogador~~
Local no código
```python
def clique(x, y):
    ...
    # TODO:
    # Verifique se o azulejo clicado é o correto.
    # Se for errado, finalize o jogo.
    # Se for correto:
    #   - adicione aos palpites
    #   - pisque o azulejo
    #   - verifique se a sequência terminou
    pass
```

**Enunciado**
Implemente a verificação do clique do jogador, comparando com o padrão esperado
e reagindo a erros.

**Conceitos envolvidos**
1. Condicionais
1. Listas
1. Eventos
1. Fluxo de controle

**Racional pedagógico**
O aluno conecta entrada do usuário a estado interno e aprende a tratar
explicitamente situações de erro, um aspecto central da programação imperativa.

**Avalia**
1. Raciocínio lógico
1. Uso correto de listas e índices
1. Compreensão de eventos como gatilhos de execução