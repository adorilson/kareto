# Palco que brilha

O nosso palco está muito sem vida. Vamos acrescentar cores.

A função abaixo é capaz de selecionar aleatoriamente uma cor dentre
uma lista de opções e depois atribui esta cor ao palco.

```python 
def muda_palco():
    import random

    cores = ["lightyellow", "lightblue", "lightcyan",  "lightgray",
             "lightcoral",  "lightpink", "lightsalmon", "lightgreen"]
    cor = random.choice(cores)

    palco = turtle.Screen()
    palco.bgcolor(cor)
```

Você deverá implementá-la no código do exercício anterior e depois deverá
chama-lá para que de fato o palco brilhe. És capaz de fazer isso?
Dica: o palco deve mudar sempre que a tartaruga dança.

## Resultado esperado
![Um palco que brilha](04_palco_brilha.gif "Um palco que brilha")

## Banco de instruções

```muda_palco```

```turtle.ontimer(???, ???)```


[Anterior](03_dancarina.md) [Próxima](05_???.md)
