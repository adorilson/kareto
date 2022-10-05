# Encapsulamento

Um dos pilares da programação orientada a objetos é o encapsulamento.

**Encapsulamento** refere-se ao empacotamento de dados com os métodos que irão
manipular esses dados. Também é usada para esconder valores ou estados das 
estruturas de dados em um objeto, prevenindo acesso direto a eles, de forma
a esconder detalhes de implementação ou violar invariâncias de estados mantidas
pelo métodos.

Considere as operações de adição e movimentação de vetores que implementamos 
anteriormente. Caso não existisse o mecanismo de encapsulamento, implementado
nos métodos `__add__` e `move`, a operação teria que ser realizada pelo mesmo
código que criou o objeto. Veja como seria a operação de adição:

```python
>>> v1 = vector(9, 4)
>>> v2 = vector(4, 2)
>>> x3 = v1.x + v2.x
>>> y3 = v1.y + v2.y
>>> v3 = vector(x3, y3) 
```

Por sua vez, observe como ficaria a operação de mover um vetor:

```python
>>> v1 = vector(9, 4)
>>> direta = vector(1, 0)
>>> y1.x = v1.x + direta.x
>>> y1.y = v1.y + direta.y
```

Agora compare quando os métodos são utilizados.

```python
>>> v1 = vector(9, 4)
>>> v2 = vector(4, 2)
>>> v3 = v1 + v2 # soma de vetores
>>> direta = vector(1, 0)
>>> v1.move(direita) # movimento de vetor
```

Perceba que as operações matemáticas que estavam **encapsuladas** nos métodos 
foram expostas e a leitura e compreensão do código ficou mais complexa. É muito
mais simples para nós humanos assimilarmos que estamos somando dois vetores com 
`v3 = v1 + v2` do que com:

```python
>>> x3 = v1.x + v2.x
>>> y3 = v1.y + v2.y
>>> v3 = vector(x3, y3) 
```

Da mesma forma, a movimentação de um vetor. Muito mais simples entender que 
estamos movendo um vetor para a direita com `v1.move(direita)` do que com:

```python
>>> y1.x = v1.x + direta.x
>>> y1.y = v1.y + direta.y
```

Essa simplificação se dá não só pela diminuição de passos, mas também pela
semântica dos nomes dos métodos. Não raro, encontraremos classes com métodos
que possuem apenas uma linha de código, mas estarão encapsulando operações
e provendo semântica.

Embora as linguagens de programação ofereçam os recursos sintáticos necessários 
para implementação de encapsulamento, o encapsulamento não é um recurso 
sintático por si, sendo totalmente dependente de como a pessoa desenvolvedora
organiza o código de suas classes.

É comum vermos sistemas que, embora utilizem classes e objetos, a programação 
não é orientada a objetos. Os trechos acima onde as operações de adição e 
movimentação não foram feitas nos métodos é um exemplo disso.

Portanto, assim como a programação de forma geral, dominar a programação 
orientada a objetos é algo que demanda tempo e estudo. Complemente a classe 
`vector` com algumas operações mais descritas na seção seguinte. 

[Anterior](02_poo_vector.md) | [Próximo](04_poo_vector2.md)
