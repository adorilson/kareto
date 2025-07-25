# Criando suas próprias funções

Você viu na fase anterior que a palavra reservado do Python para criar funções é o `def`,
e a definição de uma função tem o seguinte formato geral:

``` python
def nome_da_função():
    <instruções>
```

Você pode colocar na função o nome que quiser, desde que não seja uma palavra
reservada do Python, e obedeça as regras de identificados (por exemplo, não
pode começar com um número).

`<instruções>` você vai substituir pelas ações que a função deve executar,
podendo aninhar quaisquer comandos Python. 

Assim como os blocos `for`, `if`, `while` e outros, o conteúdo da função também
deve estar **indentado** (com espaços à frente).
Se esquecer disso, o Python vai avisar com uma mensagem de erro parecida com esta:

```
IndentationError: expected an indented block
```

A função acaba quando não há mais blocos indentados. Tome cuidado com isso.

## 🐝 Sua vez de praticar

O código inicial tem o seguinte esqueleto de função:

```python
def desenhe_estrela():
    pass
```

`pass` é uma palavra reservada do Python que não faz nada, mas usamos quando a sintaxe exige uma instrução.
Sem ela, ocorreria um erro de sintaxe. Remova-a e implemente a função para desenhar a estrela.
 

![Estrela](cenario_72.png "Estrela")


- Cada braço da estrela tem 25 pixels de comprimento
- Você vai precisar girar 45 graus para obter 8 braços
- Não há problema em ir para frente e para trás no mesmo braço


## 🧰 Caixa de ferramentas

### Mundo (turtle)
- `import turtle`

- `turtle.mainloop()`

- `artista.forward(???)`

- `artista.right(???)`

- `artista.left(???)`

### Kareto
- `from kareto.fase72 import Artista`

- `artista = Artista()`

### Python
- `def desenhe_estrela():`

- `for _ in range(???):`

- `pass`


## 💻 Código inicial

```python
import turtle
from kareto.fase72 import Artista


# definição da função
def desenhe_estrela():
    pass


artista = Artista()
desenhe_estrela()


turtle.mainloop()
```

[Anterior](../fase71/README.md) | [Próximo](../fase73/README.md)
