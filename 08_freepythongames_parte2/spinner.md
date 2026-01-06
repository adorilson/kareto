# Spinner

Spinner funciona como um micro-laboratório de:
1. estado mutável e visível,
1. controle temporal explícito,
1. separação entre estado → desenho → interação.

Servindo como ponte natural entre jogos puramente reativos (ex.: Paint) e jogos com dinâmica contínua (ex.: Snake, Pong).

[Versão do professor](spinner_prof.py) | [Versão do aluno](spinner.py)

## Exercícios propostos

### TODO 1 - Fazer o terceiro braço do spinner

- **Conceitos:** comandos sequenciais, rotação relativa, repetição estrutural,
coordenadas relativas e simetria
- **Racional:** o aluno identifica e completa um padrão geométrico já existente no
código, reforçando leitura estrutural e compreensão da ordem de execução
- **Avalia:** reconhecimento de padrões, uso correto de rotações e comandos
gráficos
- **Nível:** básico

Este exercício funciona como um pré-requisito conceitual para:
- alterar o padrão visual do spinner,
- generalizar o desenho usando laços (for),
- compreender simetria e modularidade gráfica.

Ele também serve como diagnóstico rápido: alunos que não conseguem completá-lo
corretamente tendem a ter dificuldade nos exercícios intermediários de controle
de estado e tempo.


### Exercício 1 — Alterar o padrão do spinner

- **Conceitos:** decomposição visual, repetição, coordenadas relativas
- **Racional:** força o aluno a entender o desenho passo a passo
- **Avalia:** leitura de código e modificação estruturada
- **Nível:** básico

### Exercício 2 — Responder a cliques do mouse

- **Conceitos:** eventos, callbacks, entrada do usuário
- **Racional:** amplia o modelo de interação além do teclado
- **Avalia:** associação evento → função → alteração de estado
- **Nível:** intermediário

### Exercício 3 — Alterar a aceleração

- **Conceitos:** variáveis de controle, tempo, simulação física simples
- **Racional:** introduz noções de desaceleração e parâmetros dinâmicos
- **Avalia:** raciocínio quantitativo e ajuste fino de comportamento
- **Nível:** intermediário

### Exercício 4 — Giro para frente e para trás

- **Conceitos:** sinais, condicionais, estado bidirecional
- **Racional:** quebra a ideia de estado monotônico
- **Avalia:** controle lógico e previsibilidade do sistema
- **Nível:** avançado
