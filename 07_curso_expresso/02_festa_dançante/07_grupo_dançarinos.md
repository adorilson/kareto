# 👯‍♂️ Grupo de Dançarinos


Quer deixar a sua festa ainda mais animada? Hora de colocar um **grupo 
inteiro** para dançar junto!

Use o novo bloco mágico:

```python
festa_dançante.cria_dançarinos_apoio(10, 'Apoio', 'Circulo')
```

- O primeiro argumento (`10`) indica **quantos dançarinos** você quer criar.
- O segundo (`'Apoio'`) é o **nome do grupo**.
- o terceiro (`'Circulo'`) é a **formação inicial** dos dançarinos.

Assim, de uma vez só, você solta um grupo inteiro na pista — prontos para
seguir seu dançarino principal ou arrasar em coreografias próprias!

Com ele, você cria **vários dançarinos de apoio** ao redor do seu dançarino
principal no centro da pista. 🎶

E não para por aí: também adicionamos uma forma de mudar o visual da festa!

Com o bloco:

```python
festa_dançante.muda_palco()
```

você muda automaticamente o fundo do palco para uma nova cor aleatória! 🌈✨
Basta chamar essa função sempre que quiser dar uma renovada no clima do seu show.

Agora com dançarinos de apoio e cenários que mudam de cor, sua festa vai ser um espetáculo completo! 🚀🎶


![Grupo de dançarinos](07_grupo_dançarinos.gif "Grupo de dançarinos")


## Caixa de ferramentas

`dançarino = festa_dançante.cria_dançarino('Principal', 'Centro')`

`festa_dançante.cria_dançarinos_apoio(10, 'Apoio', 'Circulo')`

`festa_dançante.muda_palco()`


## Código inicial

```python
import turtle

import festa_dançante

festa_dançante.muda_palco()



turtle.mainloop()

```


[Anterior](06_vamos_curtir.md) | [Próximo](08_propriedades.md)
