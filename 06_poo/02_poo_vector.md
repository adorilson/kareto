# Reconstruindo a classe vector

No tópico sobre a biblioteca `freegames`, tomamos conhecimento sobre a classe
`vector`. Criamos objetos dessa classe e executamos vários métodos. Iremos
agora fazer uma reconstrução de uma versão simplificada dessa classe.

A forma mais simples para definir uma classe é a seguinte:

```python
class vector:
    pass
```

Crie um novo arquivo com este código e salve com o nome `vectors.py`. No caso
de Python, o nome do arquivo é arbitrário, não havendo nenhum relação sintática 
definida pela linguagem. Escolhemos este nome para indicar que ele contém código
relacionado a manipulação de vetores.

Com isso, já podemos criar objetos dessa classe:

```python
>>> from vectors import vector
>>> v = vector()
>>> v
<vectors.vector object at 0x7fdbf6feb490>
>>> type(v)
<class 'vectors.vector'>
```

Para que o `import` funcione corretamente é necessário que o interpretador Python
seja executado a partir do diretório que contém o arquivo. Após criar o objeto `v`,
podemos ver a sua representação textual digitando isso no interpretador e 
pressionando a tecla `enter`. Como resultado, temos a informação que `v` é um 
objeto da classe `vector` e a que a classe veio do módulo `vectors`, e qual o 
endereço de memória `v` está. A classe do objeto também pode ser obtida com a
função embutida `type`.

Observamos na chamada a `vector()` não passamos nenhum argumento. Veja o que aconteceria se fizesse isso:

```python
>>> v = vector(3, 4)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: vector() takes no arguments
```

E vamos indo...



