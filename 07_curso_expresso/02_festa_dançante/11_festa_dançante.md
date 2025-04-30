# 🌟 A Grande Festa Final

Chegou a hora de brilhar no palco principal!

Você já aprendeu como criar dançarinas, mudar o palco, reagir a eventos do
teclado, responder à passagem do tempo e controlar várias propriedades para
personalizar cada detalhe da sua coreografia.

Agora, é o seu momento de juntar tudo o que aprendeu e criar sua própria Festa
Dançante! Pode ser uma coreografia com um grupo inteiro, uma dança interativa
com teclas, ou um espetáculo que muda sozinho conforme o tempo passa.

Não existe resposta certa aqui.
Só existe **sua criatividade**.

Use os blocos que exploramos ao longo do caminho e solte sua imaginação:
🎶 Uma luz que pisca a cada compasso?
🩰 Dançarinas sincronizadas com as setas do teclado?
🌈 Um palco que muda de cor no meio da apresentação?

Você é o coreógrafo, a plateia está pronta — o palco é seu!


## 🧰 Caixa de Ferramentas da Festa Final

Aqui estão todos os blocos, funções e comandos que você pode usar, organizados
por tipo e espaço de nomes, o local onde estão definidos.

Se o espaço de nomes for `turtle` significa que você poderá usar em qualquer
programa com o módulo `turtle`, se `Turtle` significa que poderá usar com 
qualquer tartaruga, não só com as dançarinas. Se ele estiver com letra
minúscula, significa que é o módulo e você deve escrever exatamente como está,
se estiver com letra maiúscula é a classe e você deve substituir pelo nome do
objeto que você definiu.

A maioria você já viu/usou, outros podem ser novos:


### Módulos

- `import turtle`

- `import festa_dançante`


### Palco

- `turtle.bgcolor(cor)` - define a cor de fundo da tela.

- `festa_dançante.muda_palco()` - muda a cor de fundo do palco aleatoriamente.


### Dançarina e outras tartarugas

#### Criação das dançarinas

- `dançarina = festa_dançante.Dançarina()` - cria uma nova dançarina acessando
diretamente sua classe. Neste caso, ela estará no centro e seu tipo será 
`"Principal"`.

- `festa_dançante.cria_dançarina(nome, posição)` - cria uma nova dançarina.
    Exemplos de locais: `"Centro"`, `"Esquerda"`, `"Direita"`.

- `festa_dançante.cria_dançarinos_apoio(qtd, nome, local)` - cria um grupo de
dançarinas de apoio.

- `dançarina = festa_dançante.escolhe_uma_dançarina()` - não cria uma dançarina, mas
escolhe aleatoriamente uma para você.

#### Movimentação

- `Turtle.goto(x, y)` - a tartaruga vai para a posição `x, y`.

- `festa_dançante.move_uma()` - aleatoriamente, uma dançarina começa (ou para)
sua movimentação pelo palco,

- `Dançarina.aleatório()` - a dançarina faz uma ação aleatória.

- `Dançarina.anda_direita()` - a dançarina move-se para a direita da tela.

- `Dançarina.anda_esquerda()` - a dançarina move-se para a esquerda da tela.

- `Dançarina.balança()` - liga/desliga o balanço da dançarina.

- `Dançarina.mexe_direita()` - a dançarina vira 5 graus para a direita.

- `Dançarina.mexe_esquerda()` - a dançarina vira 5 graus para a esquerda.

- `Dançarina.faz_rodopio()` - a dançarina faz um rodopio.

- `Dançarina.rodopia()` - liga/desliga os rodopios da dançarina.

- `Dançarina.move()` - liga/desliga a movimentação aleatória da dançarina.

- `Dançarina.para_tudo()` - a dançarina para todos seus movimentos (balanço,
   rodopio e movimentação).

#### Propriedades

##### Movimentação e orientação.

- `Turtle.setposition(x, y)` - define a posição da tartaruga nas coordenadas `x, y`.

- `Turtle.setx(x)` - define a coordenada `x` da tartaruga.

- `Turtle.sety(y)` - define a coordenada `y` da tartaruga.

- `Turtle.setheading(ângulo)` - define para onde a tartaruga vai "olhar".

- `Turtle.speed(velocidade)` - define a velocidade da tartaruga.

##### Aparência da tartaruga

- `Turtle.color(cor)` - define a cor da tartaruga.

- `Turtle.fillcolor(cor)` - define a cor de preenchimento (corpo) da tartaruga.

- `Turtle.pencolor(cor)` - define a cor da borda da tartaruga (e da sua caneta).

- `Turtle.shape(formato)` - define o formato da tartaruga.

- `Turtle.shapesize(tamanho)` - define o tamanho da tartaruga.

- `festa_dançante.defina(nome, propriedade, valor)` - define uma propriedade de
forma coletiva, usando o nome do grupo.

- `Dançarina.muda_cor()` - muda a cor da dançarina para uma cor aleatória.


### Eventos

- `turtle.ontimer(função, ms)` - executa a `função` após passados `ms`
milissegundos.

- `turtle.onkey(fun, tecla)` - executa a `função` sempre a `tecla` é
pressionada. Exemplos de teclas: `"Right"`, `"Left"`, `"a"`, `"space"`, `"A"`.

- `festa_dançante.a_cada_compasso(função, compasso)` - executa `função` a cada
`compasso` compassos.

# Código inicial

```python

# Não tem código inicial. É sua vez de brilhar.

```


[Anterior](10_a_cada_compasso.md)
