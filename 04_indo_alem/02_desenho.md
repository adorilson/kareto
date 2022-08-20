# Desenho

Como já visto e praticado, com poucas instruções e algum conhecimento de
geometria, é possível fazer figuras geométricas com o movimento da
tartaruga. 

Que tal desenhar uma círculo? Os babilônios dividiram o círculo em 360 partes 
iguais, pois acreditavam que essa era a quantidade de dias referentes ao 
período de um ano e porque seu sistema de numeração era de base sessenta ou
sexagesimal. Assim, para desenharmos um círculo, basta fazermos 360 execucões
sucessivas aos métodos ```forward```, para a tartaruga andar, e ```right```
(ou ```left```) para a tartaruga virar um pouquinho a cada passo.

Experimente.

```python
>>> for _ in range(360):
...     turtle.forward(1)
...     turtle.left(1)
```

Se por um lado fazer círculos é uma tarefa bastante comum, por outro você
pode querer personalizar, como definir o tamanho do raio, se quer um círculo
completo ou um semicírculo, ou ainda a quantidade de pontos do círculo.
Por isso, ```turtle``` provê um método para desenhar círculos onde isso pode
ser configurado.

- ```circle(radius, extent=None, steps=None)```

Para desenhar um círculo com raio de 100 pixels, basta fazer:
```python
>>> turtle.circle(100)
```

Ou se quiser um semicirculo, basta indicar quantos graus a tartatura deve 
percorrer. Informe o parâmetro ```extent``` com valor 180.

```python
>>> turtle.circle(radius=100, extent=180)
```

E, se quiser um círculo fazendo menos passos, o que vai deixá-com "dentes",
pode definir um valor para o parâmetro ```steps```, que por padrão é ```None```, mas poderia ser 360. Tem o mesmo efeito.

```python
>>> turtle.circle(radius=100, steps=100)
```

Explore esses parâmetros.

**Desafio** Você consegue fazer um quadrado ou um triângulo com o método 
```circle```?

**Desafio** Como seriam os códigos para desenhar essas figuras sem o uso desse método?

**Desafio** Crie um novo arquivo Python e defina funções para desenhar uma reta, 
um quadrado, um triângulo, um retângulo e uma estrela.

## Referências

[Grau (Geometria)](https://pt.wikipedia.org/wiki/Grau_(geometria))

[Anterior](01_movimentacao.md) | [Próximo](03_caneta.md)
