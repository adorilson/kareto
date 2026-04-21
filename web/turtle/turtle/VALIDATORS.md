# Turtle validators

Este documento descreve o formato de `test_cases` usado pelo editor Turtle e lista os tipos de validacao disponiveis. O foco aqui e o conteudo que vai no campo de teste (inserido na plataforma web), nao o HTML.

## Indice

- [Como o `test_cases` e lido](#como-o-test_cases-e-lido)
- [Diretorio `_validators`](#diretorio-_validators)
- [Tipos principais](#tipos-principais)
  - [`turtle_shape` (formas geometricas)](#turtle_shape-formas-geometricas)
  - [`turtle_rules` (DSL leve de regras)](#turtle_rules-dsl-leve-de-regras)
- [Tipos especificos existentes](#tipos-especificos-existentes)
- [Presets para formas comuns](#presets-para-formas-comuns)
- [Modo legado: `outerHTML`](#modo-legado-outerhtml)
- [Exemplos historicos (movidos do HTML)](#exemplos-historicos-movidos-do-html)
  - [1.12 - Triangulo 2](#112---triangulo-2---150-pixels-pra-cima)
  - [1.11 - Hexagono irregular](#111---hexagono-irregular-sem-definicao-das-dimensoes)
  - [1.9 - Plaquinha](#19---plaquinha-modo-legado-outerhtml)
  - [1.8 - Retangulo](#18---retangulo-modo-legado-outerhtml)
  - [1.6 - Triangulo](#16---triangulo-modo-legado-outerhtml-desenhe-um-triangulo-cada-lado-do-triangulo-possui-100-pixels-e-120-graus-nos-angulos-a-rotacao-deve-ser-para-a-esquerda-o-triangulo-deve-ser-formado-por-um-lado-horizontal-e-dois-lados-inclinados-para-baixo-como-um-v-invertido)
  - [1.5 - Quadrado](#15---quadrado-modo-legado-outerhtml---vamos-agora-completar-o-quadrado-cada-lado-deve-medir-100-pixels-e-todos-os-angulos-sao-de-90-graus)
  - [1.3 - L invertido](#13---l-invertido-modo-legado-outerhtml---a-partir-do-codigo-inicial-escreva-as-instrucoes-necessarias-para-que-a-artista-desenhe-um-l-invertido-cada-lado-tem-100-pixels-de-comprimento-sendo-a-rotacao-para-a-direita-o-l-deve-ser-formado-por-um-lado-horizontal-e-outro-lado-vertical-para-baixo)
  - [2.7 - Oculos](#27---oculos)
  - [2.6 - Ops... envelope errado](#26---ops-envelope-errado)
  - [2.5 - Envelope vermelho](#25---envelope-vermelho)
  - [2.4 - Triangulo colorido](#24---triangulo-colorido)
  - [2.3 - Dois quadrados coloridos](#23---dois-quadrados-coloridos)
  - [2.2 - Quadrado vermelho](#22---quadrado-vermelho)
  - [2.1 - Quadrangulo](#21---quadrangulo---valida-apenas-o-final)

## Como o `test_cases` e lido

- O conteudo do elemento `data#test-cases` e lido como texto e convertido via `ast.literal_eval`.
- O formato aceito e:
  - Um dicionario unico (ex.: `{ 'type': 'turtle_shape', ... }`), ou
  - Uma lista de dicionarios (modo legado com `selector` + `outerHTML`).

Observacao: em HTML, operadores como `>` e `<` podem virar `&gt;` e `&lt;`. O validador de regras ja normaliza esses escapes.

## Diretorio `_validators`

Este diretorio concentra a logica de validacao, separada por responsabilidade. O arquivo `validators.py` atua como dispatcher e delega para esses modulos.

- `_validators/__init__.py`: ponto de entrada que expoe `run()` e orquestra validacoes comuns.
- `_validators/rules.py`: implementa `turtle_rules`, calculo de metricas e avaliacao das regras.
- `_validators/shapes.py`: validacoes geometricas (poligonos, triangulos, hexagonos) e helpers de segmentos/pontos.
- `_validators/parser.py`: validacoes baseadas em AST do codigo (configuracoes, sequencias, listas de cores) e helpers privados para analise de codigo.

## Tipos principais

### `turtle_shape` (formas geometricas)

Valida apenas a forma, com tolerancias. Ideal para quadrado, triangulo, hexagono etc.

Campos:
- `type`: `turtle_shape`
- `shape`: apenas `polygon` (por enquanto)
- `sides`: numero de lados (obrigatorio)
- `side`: tamanho do lado (opcional)
- `sideTol`: tolerancia de lado
- `equalSides`: `True` para lados iguais
- `ratio`: usado quando `equalSides` esta ativo (max/min <= ratio)
- `closeEps`: tolerancia de fechamento
- `pointEps`: tolerancia para juntar pontos (default = `closeEps`)
- `turnMean`: media dos angulos internos esperados (opcional)
- `turnTol`: tolerancia para `turnMean`
- `strict`: `True` exige exatamente `sides` segmentos (nada antes/depois)
- `lastN`: pega apenas os ultimos N segmentos
- `nonZeroOnly`: ignora segmentos de comprimento ~0 (default `True`)
- `minLen`: limite de comprimento para ignorar segmentos (default `0.5`)
- `msg`: mensagem de erro

### `turtle_rules` (DSL leve de regras)

Permite definir regras por metricas. Mais flexivel, menos específico.

Campos:
- `type`: `turtle_rules`
- `rules`: lista de regras
- `codeRules`: regras aplicadas ao codigo (AST), avaliadas no `parser.py`, com metricas `code*`
- `closeEps`: tolerancia para considerar fechado (distância entre ultimo e primeiro ponto)
- `pointEps`: tolerancia para juntar pontos próximos (default = `closeEps`)
- `nonZeroOnly`: ignora segmentos de comprimento ~0 (default `True`)
- `minLen`: limite de comprimento para ignorar segmentos (default `0.5`)
- `lastN`: usa apenas os últimos N segmentos para calcular as metricas
- `strictSegments`: exige exatamente N segmentos
- `msg`: mensagem de erro

Formato de regra:
```python
{ 'metric': 'segments', 'op': '>=', 'value': 4 }
```

Operadores suportados:
- Comparacao: `==`, `!=`, `>`, `>=`, `<`, `<=`
- Aproximacao: `approx` (usa `tol`)
- Intervalo: `between` (usa `min` e `max`)

Métricas disponíveis:
- `segments`: quantidade de segmentos de linha considerados.
- `uniquePoints`: quantidade de pontos distintos (apos juntar por tolerancia).
- `closed`: `True` se o ponto final esta dentro de `closeEps` do ponto inicial.
- `sideMean`: media dos comprimentos dos segmentos.
- `sideMin`: menor comprimento de segmento.
- `sideMax`: maior comprimento de segmento.
- `sideStd`: desvio padrao dos comprimentos dos segmentos.
- `bboxWidth`: largura do retangulo envolvente (minX -> maxX).
- `bboxHeight`: altura do retangulo envolvente (minY -> maxY).
- `bboxRatio`: proporção largura/altura do bbox.
- `turnMean`: media dos angulos entre segmentos consecutivos (em graus).
- `turnMin`: menor ângulo entre segmentos consecutivos.
- `turnMax`: maior ângulo entre segmentos consecutivos.
- `turnMeanSigned`: media dos angulos com sinal (positivo = direita, negativo = esquerda).
- `turnMinSigned`: menor angulo com sinal entre segmentos.
- `turnMaxSigned`: maior angulo com sinal entre segmentos.
- `turnDir`: direcao media da curva (`right`, `left` ou `none`).
- `codeForwardCount`: quantidade de chamadas a `forward()`/`fd()` no codigo.
- `codeForwardLiteralCount`: quantidade de `forward()` com numero literal.
- `codeForwardUnique`: quantidade de valores literais distintos em `forward()`.
- `codeRightCount`: quantidade de chamadas a `right()`.
- `codeRightLiteralCount`: quantidade de `right()` com numero literal.
- `codeLeftCount`: quantidade de chamadas a `left()`.
- `codeLeftLiteralCount`: quantidade de `left()` com numero literal.
- `codeTurnCount`: total de chamadas de curva (`right()` + `left()`).

Exemplo com `codeRules` + `rules` (retangulo, curva a direita):
```python
{
  'type': 'turtle_rules',
  'closeEps': 5,
  'codeRules': [
    { 'metric': 'codeForwardCount', 'op': '==', 'value': 4 }
  ],
  'rules': [
    { 'metric': 'segments', 'op': '==', 'value': 4 },
    { 'metric': 'closed', 'op': '==', 'value': True },
    { 'metric': 'turnMean', 'op': 'approx', 'value': 90, 'tol': 10 },
    { 'metric': 'turnDir', 'op': '==', 'value': 'right' },
    { 'metric': 'bboxRatio', 'op': '>=', 'value': 1.2 }
  ],
  'msg': 'Desenhe um retangulo com curva a direita.'
}
```

## Tipos específicos existentes

- `hexagon`: hexagono irregular (2 lados maiores)
- `triangle`: triangulo com base horizontal e ponta para cima
- `polygon`: poligono generico (lados e fechamento)
- `turtle_config`: valida configuracoes no codigo (cor, shape, tamanho)
- `turtle_sequence`: valida sequencias especificas (cores, pensize, 2 quadrados)
- `turtle_random_colors_triangle`: valida lista de cores + triangulo
- `turtle_envelope`: valida envelope (tamanho, cores, aba)
- `turtle_glasses`: valida oculos (2 lentes, gap)
- `text_answer`: valida respostas textuais (ex.: multipla escolha)
- Legado (lista): `selector` + `outerHTML`

## Presets para formas comuns

### Quadrado (estrito)

Pode ser usado em exercícios para desenhar um quadrados sem definições de dimensões. Mas exigem que sejam apenas 4 linhas.

`turtle_shape`:
```python
{
  'type': 'turtle_shape',
  'shape': 'polygon',
  'sides': 4,
  'strict': True,
  'equalSides': True,
  'closeEps': 5,
  'turnMean': 90,
  'turnTol': 8,
  'msg': 'Desenhe um quadrado.'
}
```

`turtle_rules`:
#TODO: essas regras parecem não funcionar 100%
```python
{
  'type': 'turtle_rules',
  'strictSegments': 4,
  'closeEps': 5,
  'rules': [
    { 'metric': 'segments', 'op': '==', 'value': 4 },
    { 'metric': 'closed', 'op': '==', 'value': True },
    { 'metric': 'turnMean', 'op': 'approx', 'value': 90, 'tol': 8 },
    { 'metric': 'sideStd', 'op': '<=', 'value': 5 }
  ],
  'msg': 'Desenhe um quadrado.'
}


{
  'type': 'turtle_rules',
  'closeEps': 5,
  'rules': [
    {'metric': 'segments', 'op': '>=', 'value': 4},
    {'metric': 'closed', 'op': '==', 'value': True},
    {'metric': 'turnMean', 'op': 'approx', 'value': 90, 'tol': 8}
  ],
  'msg': 'Desenhe um quadrado.'
}

```

#### Código inicial

```python
# Pode ser do zero.
```

#### Solução

```python
import turtle

artista = turtle.Turtle()
artista.shape('turtle')

for x in range(4):
    artista.forward(20)
    artista.left(90)

# Instrução necessária para que a janela não se feche
turtle.done()
```

### Retangulo (estrito)

`turtle_rules` (lado maior e menor diferentes):
```python
{
  'type': 'turtle_rules',
  'strictSegments': 4,
  'closeEps': 5,
  'rules': [
    { 'metric': 'segments', 'op': '==', 'value': 4 },
    { 'metric': 'closed', 'op': '==', 'value': True },
    { 'metric': 'turnMean', 'op': 'approx', 'value': 90, 'tol': 8 },
    { 'metric': 'sideMax', 'op': '>=', 'value': 150 },
    { 'metric': 'sideMin', 'op': '<=', 'value': 110 }
  ],
  'msg': 'Desenhe um retangulo.'
}
```

### Triangulo equilatero (estrito)

`turtle_shape`:
```python
{
  'type': 'turtle_shape',
  'shape': 'polygon',
  'sides': 3,
  'strict': True,
  'equalSides': True,
  'closeEps': 5,
  'turnMean': 60,
  'turnTol': 8,
  'msg': 'Desenhe um triangulo equilatero.'
}
```

### Triangulo isosceles (base horizontal)

`turtle_shape` (base horizontal e ponta para cima nao e verificada aqui):
```python
{
    'type': 'triangle',
    'side': 150,
    'sideTol': 8,
    'closeEps': 5,
    'baseEps': 6,
    'minHeightRatio': 0.5,
    'msg': 'Desenhe um triângulo equilatero com lado de 150 pixels.'
  }
```

### Pentagono regular (estrito)

`turtle_shape`:
```python
{
  'type': 'turtle_shape',
  'shape': 'polygon',
  'sides': 5,
  'strict': True,
  'equalSides': True,
  'closeEps': 5,
  'turnMean': 108,
  'turnTol': 8,
  'msg': 'Desenhe um pentagono regular.'
}
```

### Hexagono regular (estrito)

`turtle_shape`:
```python
{
  'type': 'turtle_shape',
  'shape': 'polygon',
  'sides': 6,
  'strict': True,
  'equalSides': True,
  'closeEps': 5,
  'turnMean': 120,
  'turnTol': 8,
  'msg': 'Desenhe um hexagono regular.'
}
```

### Losango (lado igual, angulo livre)

`turtle_rules`:
```python
{
  'type': 'turtle_rules',
  'strictSegments': 4,
  'closeEps': 5,
  'rules': [
    { 'metric': 'segments', 'op': '==', 'value': 4 },
    { 'metric': 'closed', 'op': '==', 'value': True },
    { 'metric': 'sideStd', 'op': '<=', 'value': 5 }
  ],
  'msg': 'Desenhe um losango.'
}
```

## Modo legado: `outerHTML`

Se `test_cases` for uma lista, o validador usa `selector` + `outerHTML` e compara o SVG de forma exata. Isso e rigido e sensivel a pequenas variacoes.

## Exemplos historicos (movidos do HTML)

Abaixo estao exemplos antigos que ficavam em `turtle.html` para referencia. Eles nao precisam estar no servidor.


### 1.13 - Previsão

Olhe atentamente para o código abaixo.
O que acontece se ele for executado.

O que acontece se ele for executado?

A) A artista desenhará um triângulo com três lados iguais.

B) O artista desenhará uma única linha.

C) O artista desenhará um quadrado.

D) O artista desenhará um retângulo.

Use o código inicial para enviar sua resposta.

#### Código para análise

```python
import turtle

artista = turtle.Turtle()
artista.shape('turtle')

artista.forward(200)
artista.right(90)

artista.forward(100)
artista.right(90)

artista.forward(200)
artista.right(90)

artista.forward(100)
artista.right(90)

turtle.done()
```

#### Código inicial

```
import turtle

artista = turtle.Turtle()

resposta = 'Sua resposta aqui' # Cuidado para não apagar as aspas
artista.write(resposta)

turtle.done()
```

#### Solução

```
import turtle

artista = turtle.Turtle()

resposta = 'D' # Cuidado para não apagar as aspas
artista.write(resposta)

turtle.done()
```

#### Casos de teste

```python
{
  'type': 'text_answer',
  'varName': 'resposta',
  'value': 'D',
  'caseInsensitive': True,
  'msg': 'Resposta incorreta.'
}
```



### 1.12 - Triangulo 2 - 150 pixels, pra cima.

```python
{
  'type': 'triangle',
  'side': 150,
  'sideTol': 8,
  'closeEps': 5,
  'baseEps': 6,
  'minHeightRatio': 0.5,
  'msg': 'A tartaruga deve ter desenhado um triangulo. Todos os lados devem ter 150 pixels de comprimento, sendo a ponta do triangulo apontando para cima.'
}
```

#### Código inicial
```python
## Este é todo com você. ##
```

#### Solução

```python
import turtle

t = turtle.Turtle()

t.forward(150)
t.left(120)
t.forward(150)
t.left(120)
t.forward(150)
t.left(120)

turtle.done()
```

### 1.11 - Hexagono irregular sem definicao das dimensoes

```python
{
  'type': 'hexagon',
  'ratio': 1.3,
  'closeEps': 5,
  'msg': 'A tartaruga deve ter desenhado um hexagono irregular. Os lados maiores devem ser pelo menos 1.3 vezes os lados menores. A figura deve estar fechada, ou seja, o ponto final do desenho deve estar no ponto inicial.'
}
```

#### Código inicial

```python
## Esse é todo com você. ##
```

#### Solução
```
import turtle

t = turtle.Turtle()

for _ in range(2):
    t.forward(100)
    t.left(60)
    t.forward(50)
    t.left(60)
    t.forward(50)
    t.left(60)

turtle.done()
```

### 1.9 - Plaquinha (modo legado, outerHTML)

```python
[
  { # vira 45 graus
    'selector': '#turtle-canvas g:nth-child(5) polygon:nth-child(2) animateTransform:nth-child(9)',
    'outerHTML': '<animateTransform attributeName="transform" id="animation_frame11" type="rotate" from="-90.0,0,0" to="-45.0,0,0" begin="animation_frame10.end" dur=" 0.042s" fill="freeze"></animateTransform>',
    'msg': 'A tartaruga deve virar 45 graus para a direita antes de desenhar.'
  },
  { # anda 200 pixels
    'selector': '#turtle-canvas g:nth-child(3) line:nth-child(4)',
    'outerHTML': '<line x1="0" y1="0" x2="0" y2="0" style="stroke: black; stroke-width: 1;"><animate id="animation_frame12" attributeName="x2" attributeType="XML" from="0" to="141.4213562373095" dur=" 1.070s" fill="freeze" begin="animation_frame11.end"></animate><animate attributeName="y2" attributeType="XML" begin="animation_frame11.end" from="0" to="141.4213562373095" dur=" 1.070s" fill="freeze"></animate></line>',
    'msg': 'A tartaruga deve ter avancado 200 pixels para frente.'
  },
  {
    'selector': '#turtle-canvas g:nth-child(5) polygon:nth-child(2) animateTransform:nth-child(13)',
    'outerHTML': '<animateTransform attributeName="transform" id="animation_frame13" type="rotate" from="-45.0,0,0" to="45.0,0,0" begin="animation_frame12.end" dur=" 0.083s" fill="freeze"></animateTransform>',
    'msg': 'A tartaruga deve virar 90 graus para a direita.'
  },
  {
    'selector': '#turtle-canvas g:nth-child(3) line:nth-child(5)',
    'outerHTML': '<line x1="141.4213562373095" y1="141.4213562373095" x2="141.4213562373095" y2="141.4213562373095" style="stroke: black; stroke-width: 1;"><animate id="animation_frame14" attributeName="x2" attributeType="XML" from="141.4213562373095" to="0" dur=" 1.070s" fill="freeze" begin="animation_frame13.end"></animate><animate attributeName="y2" attributeType="XML" begin="animation_frame13.end" from="141.4213562373095" to="282.842712474619" dur=" 1.070s" fill="freeze"></animate></line>',
    'msg': 'Depois de virar, a tartaruga deve ter avancado 200 pixels para frente.'
  },
  {
    'selector': '#turtle-canvas g:nth-child(5) polygon:nth-child(2) animateTransform:nth-child(17)',
    'outerHTML': '<animateTransform attributeName="transform" id="animation_frame15" type="rotate" from="45.0,0,0" to="135.0,0,0" begin="animation_frame14.end" dur=" 0.083s" fill="freeze"></animateTransform>',
    'msg': 'A tartaruga deve virar 90 graus para a direita.'
  },
  {
    'selector': '#turtle-canvas g:nth-child(3) line:nth-child(6)',
    'outerHTML': '<line x1="0" y1="282.842712474619" x2="0" y2="282.842712474619" style="stroke: black; stroke-width: 1;"><animate id="animation_frame16" attributeName="x2" attributeType="XML" from="0" to="-141.4213562373095" dur=" 1.070s" fill="freeze" begin="animation_frame15.end"></animate><animate attributeName="y2" attributeType="XML" begin="animation_frame15.end" from="282.842712474619" to="141.4213562373095" dur=" 1.070s" fill="freeze"></animate></line>',
    'msg': 'Depois de virar, a tartaruga deve ter avancado 200 pixels para frente.'
  },
  {
    'selector': '#turtle-canvas g:nth-child(5) polygon:nth-child(2) animateTransform:nth-child(21)',
    'outerHTML': '<animateTransform attributeName="transform" id="animation_frame17" type="rotate" from="135.0,0,0" to="225.0,0,0" begin="animation_frame16.end" dur=" 0.083s" fill="freeze"></animateTransform>',
    'msg': 'A tartaruga deve virar 90 graus para a direita.'
  },
  {
    'selector': '#turtle-canvas g:nth-child(3) line:nth-child(7)',
    'outerHTML': '<line x1="-141.4213562373095" y1="141.4213562373095" x2="-141.4213562373095" y2="141.4213562373095" style="stroke: black; stroke-width: 1;"><animate id="animation_frame18" attributeName="x2" attributeType="XML" from="-141.4213562373095" to="0" dur=" 1.070s" fill="freeze" begin="animation_frame17.end"></animate><animate attributeName="y2" attributeType="XML" begin="animation_frame17.end" from="141.4213562373095" to="0" dur=" 1.070s" fill="freeze"></animate></line>',
    'msg': 'Depois de virar, a tartaruga deve ter avancado 200 pixels para frente.'
  },
]
```

### 1.8 - Retangulo (modo legado, outerHTML)

```python
[
  { # topo
    'selector': '#turtle-canvas g:nth-child(3) line:nth-child(4)',
    'outerHTML': '<line x1="0" y1="0" x2="0" y2="0" style="stroke: black; stroke-width: 1;"><animate id="animation_frame11" attributeName="x2" attributeType="XML" from="0" to="200" dur=" 1.070s" fill="freeze" begin="animation_frame10.end"></animate><animate attributeName="y2" attributeType="XML" begin="animation_frame10.end" from="0" to="0" dur=" 1.070s" fill="freeze"></animate></line>',
    'msg': 'A tartaruga deve ter avancado 200 pixels para frente.'
  },
  {
    'selector': '#turtle-canvas g:nth-child(5) polygon:nth-child(2) animateTransform:nth-child(11)',
    'outerHTML': '<animateTransform attributeName="transform" id="animation_frame12" type="rotate" from="-90.0,0,0" to="0.0,0,0" begin="animation_frame11.end" dur=" 0.083s" fill="freeze"></animateTransform>',
    'msg': 'A tartaruga deve virar 90 graus para a direita.'
  },
  { # lado direito
    'selector': '#turtle-canvas g:nth-child(3) line:nth-child(5)',
    'outerHTML': '<line x1="200" y1="0" x2="200" y2="0" style="stroke: black; stroke-width: 1;"><animate id="animation_frame13" attributeName="x2" attributeType="XML" from="200" to="200" dur=" 0.535s" fill="freeze" begin="animation_frame12.end"></animate><animate attributeName="y2" attributeType="XML" begin="animation_frame12.end" from="0" to="100" dur=" 0.535s" fill="freeze"></animate></line>',
    'msg': 'Depois de virar, a tartaruga deve ter avancado 100 pixels para frente.'
  },
  {
    'selector': '#turtle-canvas g:nth-child(5) polygon:nth-child(2) animateTransform:nth-child(15)',
    'outerHTML': '<animateTransform attributeName="transform" id="animation_frame14" type="rotate" from="0.0,0,0" to="90.0,0,0" begin="animation_frame13.end" dur=" 0.083s" fill="freeze"></animateTransform>',
    'msg': 'A tartaruga deve virar 90 graus para a direita.'
  },
  { # lado inferior
    'selector': '#turtle-canvas g:nth-child(3) line:nth-child(6)',
    'outerHTML': '<line x1="200" y1="100" x2="200" y2="100" style="stroke: black; stroke-width: 1;"><animate id="animation_frame15" attributeName="x2" attributeType="XML" from="200" to="0" dur=" 1.070s" fill="freeze" begin="animation_frame14.end"></animate><animate attributeName="y2" attributeType="XML" begin="animation_frame14.end" from="100" to="100" dur=" 1.070s" fill="freeze"></animate></line>',
    'msg': 'Depois de virar, a tartaruga deve ter avancado 200 pixels para frente.'
  },
  {
    'selector': '#turtle-canvas g:nth-child(5) polygon:nth-child(2) animateTransform:nth-child(19)',
    'outerHTML': '<animateTransform attributeName="transform" id="animation_frame16" type="rotate" from="90.0,0,0" to="180.0,0,0" begin="animation_frame15.end" dur=" 0.083s" fill="freeze"></animateTransform>',
    'msg': 'A tartaruga deve virar 90 graus para a direita.'
  },
  { # lado esquerdo
    'selector': '#turtle-canvas g:nth-child(3) line:nth-child(7)',
    'outerHTML': '<line x1="0" y1="100" x2="0" y2="100" style="stroke: black; stroke-width: 1;"><animate id="animation_frame17" attributeName="x2" attributeType="XML" from="0" to="0" dur=" 0.535s" fill="freeze" begin="animation_frame16.end"></animate><animate attributeName="y2" attributeType="XML" begin="animation_frame16.end" from="100" to="0" dur=" 0.535s" fill="freeze"></animate></line>',
    'msg': 'Depois de virar, a tartaruga deve ter avancado 100 pixels para frente.'
  },
]
```

### 1.6 - Triangulo (modo legado, outerHTML) Desenhe um triângulo. Cada lado do triângulo possui 100 pixels e 120 graus nos ângulos. A rotação deve ser para a esquerda. O triângulo deve ser formado por um lado horizontal e dois lados inclinados para baixo, como um "V" invertido.

```python
[
  { # base
    'selector': '#turtle-canvas g:nth-child(3) line:nth-child(4)',
    'outerHTML': '<line x1="0" y1="0" x2="0" y2="0" style="stroke: black; stroke-width: 1;"><animate id="animation_frame11" attributeName="x2" attributeType="XML" from="0" to="100" dur=" 0.535s" fill="freeze" begin="animation_frame10.end"></animate><animate attributeName="y2" attributeType="XML" begin="animation_frame10.end" from="0" to="0" dur=" 0.535s" fill="freeze"></animate></line>',
    'msg': 'A tartaruga deve ter avancado 100 pixels para frente.',
  },
  {
    'selector': '#turtle-canvas g:nth-child(5) polygon:nth-child(2) animateTransform:nth-child(11)',
    'outerHTML': '<animateTransform attributeName="transform" id="animation_frame12" type="rotate" from="-90.0,0,0" to="-210.0,0,0" begin="animation_frame11.end" dur=" 0.111s" fill="freeze"></animateTransform>',
    'msg': 'A tartaruga deve virar 120 graus para a esquerda.',
  },
  { # lado subindo
    'selector': '#turtle-canvas g:nth-child(3) line:nth-child(5)',
    'outerHTML': '<line x1="100" y1="0" x2="100" y2="0" style="stroke: black; stroke-width: 1;"><animate id="animation_frame13" attributeName="x2" attributeType="XML" from="100" to="50.00000000000002" dur=" 0.535s" fill="freeze" begin="animation_frame12.end"></animate><animate attributeName="y2" attributeType="XML" begin="animation_frame12.end" from="0" to="-86.60254037844388" dur=" 0.535s" fill="freeze"></animate></line>',
    'msg': 'Depois de virar, a tartaruga deve ter avancado 100 pixels para frente.',
  },
  {
    'selector': '#turtle-canvas g:nth-child(5) polygon:nth-child(2) animateTransform:nth-child(15)',
    'outerHTML': '<animatetransform attributename="transform" begin="animation_frame13.end" dur="0.111s" fill="freeze" from="-210.0,0,0" id="animation_frame14" to="-330.0,0,0" type="rotate"></animatetransform>',
    'msg': 'A tartaruga deve virar 120 graus para a esquerda.',
  },
  { # lado descendo
    'selector': '#turtle-canvas g:nth-child(3) line:nth-child(6)',
    'outerHTML': '<line x1="50.00000000000002" y1="-86.60254037844388" x2="50.00000000000002" y2="-86.60254037844388" style="stroke: black; stroke-width: 1;"><animate id="animation_frame15" attributeName="x2" attributeType="XML" from="50.00000000000002" to="-2.1316282072803006e-14" dur=" 0.535s" fill="freeze" begin="animation_frame14.end"></animate><animate attributeName="y2" attributeType="XML" begin="animation_frame14.end" from="-86.60254037844388" to="-4.263256414560601e-14" dur=" 0.535s" fill="freeze"></animate></line>',
    'msg': 'Depois de virar, a tartaruga deve ter avancado 100 pixels para frente.'
  },
]
```

### 1.5 - Quadrado (modo legado, outerHTML) - Vamos agora completar o quadrado. Cada lado deve medir 100 pixels e todos os ângulos são de 90 graus.

```python
[
  {
    'selector': '#turtle-canvas g:nth-child(3) line:nth-child(4)',
    'outerHTML': '<line x1="0" y1="0" x2="0" y2="0" style="stroke: black; stroke-width: 1;"><animate id="animation_frame11" attributeName="x2" attributeType="XML" from="0" to="100" dur=" 0.535s" fill="freeze" begin="animation_frame10.end"></animate><animate attributeName="y2" attributeType="XML" begin="animation_frame10.end" from="0" to="0" dur=" 0.535s" fill="freeze"></animate></line>',
    'msg': 'A tartaruga deve ter avancado 100 pixels para frente.'
  },
  {
    'selector': '#turtle-canvas g:nth-child(5) polygon:nth-child(2) animateTransform:nth-child(11)',
    'outerHTML': '<animateTransform attributeName="transform" id="animation_frame12" type="rotate" from="-90.0,0,0" to="0.0,0,0" begin="animation_frame11.end" dur=" 0.083s" fill="freeze"></animateTransform>',
    'msg': 'A tartaruga deve virar 90 graus para a direita.'
  },
  {
    'selector': '#turtle-canvas g:nth-child(3) line:nth-child(5)',
    'outerHTML': '<line x1="100" y1="0" x2="100" y2="0" style="stroke: black; stroke-width: 1;"><animate id="animation_frame13" attributeName="x2" attributeType="XML" from="100" to="100" dur=" 0.535s" fill="freeze" begin="animation_frame12.end"></animate><animate attributeName="y2" attributeType="XML" begin="animation_frame12.end" from="0" to="100" dur=" 0.535s" fill="freeze"></animate></line>',
    'msg': 'Depois de virar, a tartaruga deve avancar 100 pixels para frente.'
  },
  {
    'selector': '#turtle-canvas g:nth-child(5) polygon:nth-child(2) animateTransform:nth-child(15)',
    'outerHTML': '<animateTransform attributeName="transform" id="animation_frame14" type="rotate" from="0.0,0,0" to="90.0,0,0" begin="animation_frame13.end" dur=" 0.083s" fill="freeze"></animateTransform>',
    'msg': 'A tartaruga deve virar 90 graus para a direita.'
  },
  {
    'selector': '#turtle-canvas g:nth-child(3) line:nth-child(6)',
    'outerHTML': '<line x1="100" y1="100" x2="100" y2="100" style="stroke: black; stroke-width: 1;"><animate id="animation_frame15" attributeName="x2" attributeType="XML" from="100" to="0" dur=" 0.535s" fill="freeze" begin="animation_frame14.end"></animate><animate attributeName="y2" attributeType="XML" begin="animation_frame14.end" from="100" to="100.00000000000001" dur=" 0.535s" fill="freeze"></animate></line>',
    'msg': 'Depois de virar, a tartaruga deve avancar 100 pixels para frente.'
  },
  {
    'selector': '#turtle-canvas g:nth-child(5) polygon:nth-child(2) animateTransform:nth-child(19)',
    'outerHTML': '<animateTransform attributeName="transform" id="animation_frame16" type="rotate" from="90.0,0,0" to="180.0,0,0" begin="animation_frame15.end" dur=" 0.083s" fill="freeze"></animateTransform>',
    'msg': 'A tartaruga deve virar 90 graus para a direita.'
  },
  {
    'selector': '#turtle-canvas g:nth-child(3) line:nth-child(7)',
    'outerHTML': '<line x1="0" y1="100.00000000000001" x2="0" y2="100.00000000000001" style="stroke: black; stroke-width: 1;"><animate id="animation_frame17" attributeName="x2" attributeType="XML" from="0" to="-1.8369701987210297e-14" dur=" 0.535s" fill="freeze" begin="animation_frame16.end"></animate><animate attributeName="y2" attributeType="XML" begin="animation_frame16.end" from="100.00000000000001" to="1.4210854715202004e-14" dur=" 0.535s" fill="freeze"></animate></line>',
    'msg': 'Depois de virar, a tartaruga deve avancar 100 pixels para frente.'
  },
]
```

### 1.3 - L invertido (modo legado, outerHTML) - A partir do código inicial, escreva as instruções necessárias para que a artista desenhe um L invertido. Cada lado tem 100 pixels de comprimento. Sendo a rotação para a direita, o L deve ser formado por um lado horizontal e outro lado vertical para baixo.

```python
[
  {
    'selector': '#turtle-canvas g:nth-child(3) line:nth-child(4)',
    'outerHTML': '<line x1="0" y1="0" x2="0" y2="0" style="stroke: black; stroke-width: 1;"><animate id="animation_frame11" attributeName="x2" attributeType="XML" from="0" to="100" dur=" 0.535s" fill="freeze" begin="animation_frame10.end"></animate><animate attributeName="y2" attributeType="XML" begin="animation_frame10.end" from="0" to="0" dur=" 0.535s" fill="freeze"></animate></line>',
    'msg': 'A tartaruga deve ter avancado 100 pixels para frente.'
  },
  {
    'selector': '#turtle-canvas g:nth-child(5) polygon:nth-child(2) animateTransform:nth-child(11)',
    'outerHTML': '<animateTransform attributeName="transform" id="animation_frame12" type="rotate" from="-90.0,0,0" to="0.0,0,0" begin="animation_frame11.end" dur=" 0.083s" fill="freeze"></animateTransform>',
    'msg': 'A tartaruga deve ter virado 90 graus para a direita.'
  },
  {
    'selector': '#turtle-canvas g:nth-child(3) line:nth-child(5)',
    'outerHTML': '<line x1="100" y1="0" x2="100" y2="0" style="stroke: black; stroke-width: 1;"><animate id="animation_frame13" attributeName="x2" attributeType="XML" from="100" to="100" dur=" 0.535s" fill="freeze" begin="animation_frame12.end"></animate><animate attributeName="y2" attributeType="XML" begin="animation_frame12.end" from="0" to="100" dur=" 0.535s" fill="freeze"></animate></line>',
    'msg': 'Depois de virar, a tartaruga deve ter avancado 100 pixels para frente.'
  },
]
```

### 2.7 - Oculos

```python
{
  'type': 'turtle_glasses',
  'size': 100,
  'sizeTol': 8,
  'gap': 50,
  'gapTol': 3,
  'minGap': 10,
  'maxGap': 500,
  'gapAxis': 'edge',
  'splitTol': 1,
  'requireGapChange': True,
  'msgLensSize': 'O tamanho das lentes deve ser diferente do original.',
  'msgLensGap': 'A distancia entre as lentes deve ser diferente da original.'
}
```

#### Código inicial

```python

import turtle

michelangelo = turtle.Turtle()
michelangelo.color('green')

michelangelo.left(90)
michelangelo.backward(100)
michelangelo.left(90)
michelangelo.backward(100)
michelangelo.left(90)
michelangelo.backward(100)
michelangelo.left(90)
michelangelo.backward(100)

michelangelo.backward(50)

michelangelo.backward(100)
michelangelo.right(90)
michelangelo.forward(100)
michelangelo.left(90)
michelangelo.forward(100)
michelangelo.left(90)
michelangelo.forward(100)
michelangelo.left(90)

```

#### Solução

```python
import turtle

michelangelo = turtle.Turtle()
michelangelo.color('green')

michelangelo.left(90)
michelangelo.backward(50)
michelangelo.left(90)
michelangelo.backward(50)
michelangelo.left(90)
michelangelo.backward(50)
michelangelo.left(90)
michelangelo.backward(50)

michelangelo.backward(30)

michelangelo.backward(50)
michelangelo.right(90)
michelangelo.forward(50)
michelangelo.left(90)
michelangelo.forward(50)
michelangelo.left(90)
michelangelo.forward(50)
michelangelo.left(90)

turtle.done()
```


### 2.6 - Ops... envelope errado

Ops...

Era para ser um envelope. Mas saiu errado. Corrija.

```python
{
  'type': 'turtle_envelope',
  'requireSize': False,
  'requireShape': False,
  'requireColor': False,
  'requireFlapRatio': False,
  'requireOrientation': False,
  'msgFlap': 'A aba do envelope deve estar alinhada com a parte superior.'
}
```

#### Código inicial

```python
import turtle

donatello = turtle.Turtle()
donatello.color('green')

donatello.forward(100)
donatello.right(120)
donatello.forward(100)
donatello.right(120)
donatello.forward(100)
donatello.right(120)

donatello.left(90)
donatello.forward(100)
donatello.left(90)
donatello.forward(100)
donatello.left(90)
donatello.forward(100)
donatello.left(90)
donatello.forward(100)


turtle.done()
```

#### Solução
```python
import turtle

donatello = turtle.Turtle()
donatello.color('green')

donatello.forward(100)
donatello.right(120)
donatello.forward(100)
donatello.right(120)
donatello.forward(100)
donatello.right(120)

donatello.forward(100)
donatello.right(90)
donatello.forward(100)
donatello.right(90)
donatello.forward(100)
donatello.right(90)
donatello.forward(100)


turtle.done()
```

### 2.5 - Envelope vermelho

Exercícios 

1) Aumente o tamanho do envelope
2) Use formas diferentes da tartaruga enquanto faz a aba e enquanto faz o corpo
3) Deixe o envelope colorido
4) Reduza o aba do envelope


### Casos de teste
```python
{
  'type': 'turtle_envelope',
  'minScale': 1.05,
  'flapRatio': 0.9,
  'msgSize': 'O envelope deve ser maior do que o original.',
  'msgShape': 'Use formas diferentes para a aba e o corpo.',
  'msgColor': 'O envelope deve ser colorido.',
  'msgFlap': 'A aba do envelope deve ser menor que o corpo.'
}
```

#### Código inicial

```python
import turtle

bowser = turtle.Turtle()
bowser.color('red')

bowser.forward(100)
bowser.right(120)
bowser.forward(100)
bowser.right(120)
bowser.forward(100)
bowser.right(120)

bowser.forward(100)
bowser.right(90)
bowser.forward(100)
bowser.right(90)
bowser.forward(100)
bowser.right(90)
bowser.forward(100)
bowser.right(90)

turtle.done()
```

#### Solução


```python
import turtle

bowser = turtle.Turtle()

# Aba (menor)
bowser.shape('turtle')
bowser.color('red')
bowser.forward(200)
bowser.goto(100, -80)
bowser.goto(0, 0)

# Corpo (maior)
bowser.shape('square')
bowser.color('blue')
bowser.setheading(0)
bowser.forward(200)
bowser.right(90)
bowser.forward(120)
bowser.right(90)
bowser.forward(200)
bowser.right(90)
bowser.forward(120)
bowser.right(90)

turtle.done()
```


### 2.4 - Triangulo colorido

```python
{
  'type': 'turtle_random_colors_triangle',
  'minColors': 5,
  'forbidColors': ['red'],
  'colorsVar': 'cores',
  'msgColors': 'A lista de cores deve ter ao menos 5 cores e nao pode incluir vermelho.',
  'msgPensize': 'A largura da linha deve ser alterada.',
  'msgTriangle': 'O triangulo deve apontar para cima.'
}
```

#### Código inicial

```python
import turtle
import random

kame = turtle.Turtle()
cores = 'red', 'purple', 'blue'

cor = random.choice(cores)
kame.color(cor)
kame.forward(100)
kame.right(120)

cor = random.choice(cores)
kame.color(cor)
kame.forward(100)
kame.right(120)

cor = random.choice(cores)
kame.color(cor)
kame.forward(100)
kame.right(120)

turtle.done()


```

#### Solução

```python
import turtle
import random

kame = turtle.Turtle()
kame.pensize(4)
cores = 'purple', 'blue', 'yellow', 'magenta', 'pink'

cor = random.choice(cores)
kame.color(cor)
kame.forward(100)
kame.left(120)

cor = random.choice(cores)
kame.color(cor)
kame.forward(100)
kame.left(120)

cor = random.choice(cores)
kame.color(cor)
kame.forward(100)
kame.left(120)

turtle.done()
```

### 2.3 - Dois quadrados coloridos

A partir do código inicial, execute os seguintes exercícios:

1) Mude/defina a forma da tartaruga
2) Mude a ordem das cores
3) Mude a largura da linha
4) Faça a tartaruga desenhar dois quadrados. Os quadrados devem estar horizontalmente alinhados.

```python
{
  'type': 'turtle_sequence',
  'msgShape': 'A forma da tartaruga deve ser diferente do padrao classic.',
  'msgColors': 'A ordem das cores deve ser diferente da original.',
  'msgPensize': 'A largura da linha deve ser diferente de 5.',
  'msgSquares': 'A tartaruga deve desenhar dois quadrados.'
}
```

#### Código inicial
```python
import turtle

oogway = turtle.Turtle()
oogway.pensize(5)

oogway.color('blue')
oogway.forward(100)
oogway.right(90)

oogway.color('black')
oogway.forward(100)
oogway.right(90)

oogway.color('red')
oogway.forward(100)
oogway.right(90)

oogway.color('pink')
oogway.forward(100)
oogway.right(90)

turtle.done()
```

#### Solução
```python
import turtle

oogway = turtle.Turtle()
oogway.shape('turtle')
oogway.pensize(3)

oogway.color('black')
oogway.forward(100)
oogway.right(90)

oogway.color('red')
oogway.forward(100)
oogway.right(90)

oogway.color('blue')
oogway.forward(100)
oogway.right(90)

oogway.color('pink')
oogway.forward(100)
oogway.right(90)

oogway.penup()
oogway.backward(200)
oogway.pendown()

oogway.color('black')
oogway.forward(100)
oogway.right(90)

oogway.color('red')
oogway.forward(100)
oogway.right(90)

oogway.color('blue')
oogway.forward(100)
oogway.right(90)

oogway.color('pink')
oogway.forward(100)
oogway.right(90)

turtle.done()

```

### 2.2 - Quadrado vermelho

```python
{
  'type': 'turtle_config',
  'requireColorChange': True,
  'requireShapeChange': True,
  'requireSquareSizeChange': True,
  'msgColor': 'A cor da linha deve ser diferente de vermelho.',
  'msgShape': 'O formato da tartaruga deve ser diferente do padrao classic.',
  'msgSize': 'O tamanho do quadrado deve ser diferente de 100.'
}
```

#### Código inicial
```python
import turtle

touche = turtle.Turtle()
touche.color('red')

touche.forward(100)
touche.left(90)

touche.forward(100)
touche.left(90)

touche.forward(100)
touche.left(90)

touche.forward(100)

turtle.done()

```

#### Uma resposta válida
```python
import turtle

touche = turtle.Turtle()
touche.shape('turtle')
touche.color('yellow')

touche.forward(10)
touche.left(90)

touche.forward(10)
touche.left(90)

touche.forward(10)
touche.left(90)

touche.forward(10)

turtle.done()
```


### 2.1 - Quadrangulo - valida apenas o final
A partir do código inicial, execute os seguintes exercícios:

1) Reduza as duas linhas com forward para apenas uma, mas que faça a mesma
coisa que as atuais
2) Faça a tartaruga virar para a direita
3) Altere o comprimento dos lados do quadrado
4) Transforme o quadrado em um retângulo

```python
# não valida a direção
{
  'type': 'rectangle',
  'sides': 4,
  'ratio': 1.2,
  'closeEps': 5,
  'msg': 'Tarefa nao realizada.'
}
```

Exemplo completo (turtle_rules, valida direcao e so o final):
```python
{
  'type': 'turtle_rules',
  'closeEps': 5,
  'lastN': 4,
  'codeRules': [
    { 'metric': 'codeForwardCount', 'op': '==', 'value': 4 }
  ],
  'rules': [
    { 'metric': 'segments', 'op': '==', 'value': 4 },
    { 'metric': 'closed', 'op': '==', 'value': True },
    { 'metric': 'turnMean', 'op': 'approx', 'value': 90, 'tol': 10 },
    { 'metric': 'turnDir', 'op': '==', 'value': 'right' },
    { 'metric': 'bboxRatio', 'op': '>=', 'value': 1.2 }
  ],
  'msg': 'Tarefa não realizada.'
}
```

#### Código inicial
```python
import turtle

crush = turtle.Turtle()
crush.shape('turtle')

crush.forward(100)
crush.forward(100)
crush.left(90)

crush.forward(100)
crush.forward(100)
crush.left(90)

crush.forward(100)
crush.forward(100)
crush.left(90)

crush.forward(100)
crush.forward(100)
crush.left(90)

turtle.done()

```

#### Solução
```python
import turtle

crush = turtle.Turtle()
crush.shape('turtle')

crush.forward(20)
crush.right(90)

crush.forward(40)
crush.right(90)

crush.forward(20)
crush.right(90)

crush.forward(40)
crush.right(90)

turtle.done()

```