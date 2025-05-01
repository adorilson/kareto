# Dois dançarinos!

É hora de uma dança!


## Sua vez de praticar

Programe cada dançarino para se mover quando você
pressionar teclas diferentes. Escolha seu movimento favorito para cada
dançarino ou até mesmo `aleatório()` (um novo método) para fazer algo
totalmente imprevisível!

![Dois dançarinos](04_dois_dançarinos.gif "Dois dançarinos")


## O nada também é importante

Quando você abrir o código inicial, verá uma linha assim:

```python
turtle.onkey(None, "Down")
```

Essa linha traz uma palavra-reservada do Python: `None`.

Em Python, `None` representa a **ausência de valor**. É como dizer:
"não tem nada aqui... ainda".

Neste exemplo, usamos `None` para dizer que **nenhuma ação está associada à
tecla `"Down"`**. Se não colocássemos nada ali, o Python daria um erro de
sintaxe. `None` funciona como um marcador de "sem ação definida".

Você também verá o `None` em outras situações — por exemplo, quando uma função
ou método **não retorna nada**. Muitos comandos do `turtle`, como `forward`,
**fazem algo**, mas **não entregam um valor de volta**. Veja só no
interpretador interativo:

```python
>>> import python
>>> t = turtle.Turtle()
>>> x = t.forward(100)
>>> print(x)
None
```

Ou seja: o Python está dizendo "Missão cumprida, mas não tenho nenhum valor
para te entregar"


## Caixa de ferramentas

`import festa_dançante`

`dançarino = festa_dançante.cria_dançarino("Principal", "Centro")`

`dançarino.anda_direita()`

`dançarino.anda_esquerda()`

`dançarino.aleatório()`

`dançarino.balança()`

`dançarino.rodopia()`

`dançarino.move()`

`turtle.onkey(???, ???)`


## Código inicial

```python
import turtle
import festa_dançante

dançarino_um = festa_dançante.cria_dançarino("Um", "Direita")
dançarino_dois = festa_dançante.cria_dançarino("Dois", "Esquerda") 

turtle.onkey(dançarino_um.aleatório, "Up") 
turtle.onkey(None, "Down")

turtle.mainloop()
```


[Anterior](03_eventos.md) | [Próximo](05_compassos.md)
