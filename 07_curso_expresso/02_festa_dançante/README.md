# 🎉 Boas vindas à Festa Dançante do Python!

O módulo `turtle` foi originalmente criado para ensinar programação de forma
visual através de desenhos geométricos. Ele simula uma tartaruga robótica que
se move por uma folha de papel, desenhando conforme vai andando. Durante nossas
aulas anteriores, usamos esse módulo para criar figuras geométricas com
movimentos totalmente automáticos — uma vez iniciado o desenho, a tartaruga
seguia seu caminho sem interferência.

Mas e se a gente pudesse **interagir** com ela? E se a tartaruga pudesse
**responder a teclas pressionadas** ou ao **passar do tempo**? Agora chegou o
momento de dar mais vida (e ritmo!) à sua tartaruga.

## 🧠 Programar é criar

Ciência da computação tem tudo a ver com **criatividade**. Quando aprendemos a
programar, ganhamos a capacidade de transformar ideias em realidade — jogos,
aplicativos, robôs, animações… ou até uma festa dançante! A programação é como
uma superpoderosa ferramenta artística que nos permite imaginar e construir
coisas incríveis.

Nesta nova etapa, você vai usar seu conhecimento para programar uma tartaruga
que **dança**! (Ok, sem música de verdade — use sua imaginação 😉).

## 🧩 Módulos: caixas com nossos blocos de montar

Você já aprendeu que um **módulo** em Python é como uma caixinha de ferramentas
— ele reúne funções, classes e outras instruções que podem ser usadas em vários
programas. O módulo `turtle`, por exemplo, veio prontinho com o Python. Mas você
também pode criar seus próprios módulos, ou usar módulos feitos por outras
pessoas.

Para esta lição, preparamos um módulo especial chamado `festa_dançante`. Ele é
um arquivo `.py` que você deve deixar na mesma pasta que seus programas. Assim,
ao usar `import festa_dançante`, você poderá acessar funções e classes que vão
facilitar sua festa! Observe que o arquivo tem a extensão `.py`, mas no
`import`, não.

Mas por que criar esse novo módulo?

Embora o `turtle` seja ótimo para desenhar e ainda contenha recursos que nos
permitam ir além disso, ele foi pensado para uso **mais generalizado**. O
módulo  `festa_dançante`, por outro lado, foi feito **sob medida para o tipo
de problema que queremos resolver**: criar interações animadas com a tartaruga
e responder a eventos de maneira mais simples e divertida. Ele expande e
personaliza as funcionalidades do `turtle`, permitindo que você se concentre
no que realmente importa agora: colocar sua tartaruga para dançar! 💃🐢

## 🕹️ Hora de Interagir!

O novo conceito que vamos explorar agora é o de **eventos**.
Eventos são ações que acontecem — como apertar uma tecla, mover o mouse ou o
tempo passando — e seu programa pode **responder a esses eventos!**

Com isso, sua tartaruga poderá:

- Dançar quando uma tecla for pressionada.
- Fazer uma pose a cada intervalo de tempo.
- Reagir ao comando de iniciar ou parar a festa.

Essa é uma introdução ao que chamamos de **programação orientada a eventos**.
Ao invés de seguir uma sequência fixa de comandos, o seu programa agora ficará
atento ao que está acontecendo, pronto para agir de acordo com os sinais que
receber.

Que comece o show.


## 💃 Sua vez de praticar

1) Crie uma pasta onde você colocará todos seus exercícios.
1) Faça o download do módulo festa_dançante [clicando aqui](https://raw.githubusercontent.com/adorilson/kareto/refs/heads/main/07_curso_expresso/02_festa_dan%C3%A7ante/festa_dan%C3%A7ante.py) e salve nessa pasta com
o nome `festa_dançante.py`.
1) Copie o código inicial deste exercício, crie um novo arquivo no VS Code
e cole o código inicial nele.
1) Salve este arquivo na pasta criada.
1) Execute o arquivo e veja o seu palco com um contador de compassos.

![Palco da festa dançante](README.gif "Palco da festa dançante")

## 🧰 Caixa de ferramentas

`import turtle`

`import festa_dançante`

`turtle.mainloop()`


## 💻 Código inicial

```python
import turtle

import festa_dançante

# Seus códigos ficarão principalmente a partir daqui



turtle.mainloop()
```


[Próximo](02_cria_dançarino.md)