# Maia, a abelhinha

<div style="display: flex; align-items: center;">
    <img src="atores/abelha_leste.gif" alt="Sou a Maia"
            style="width:50px; margin-right:10px;">
    <p>Neste mundo, ajudaremos <strong>Maia</strong>, a abelhinha, a coletar
        néctar e a fazer mel.
    </p>
</div>

Mas antes, vamos conhecer outro conceito do Python: **pacotes**.


## Pacotes

Anteriormente, vimos o conceito de **módulos**, que servem para organizar
elementos de código e reutilizá-los em outros programas. Mas e se tivermos
muitos módulos? Como eles são organizados?

Os módulos são organizados em **pacotes**. Se módulos são arquivos Python,
pacotes são **pastas** (diretórios) que contêm esses módulos, além de outros
arquivos úteis, como imagens, sons ou dados.

Um pacote pode conter **outros pacotes** dentro dele. Chamamos isso de
**subpacotes**.

Por exemplo:

```
meu_projeto/
├── atores/
│   ├── atores.py
│   └── mundo.py
└── fase01/
    └── fase01.py
```

Neste exemplo:

- `atores` e `fase01` são pacotes. Diretórios dentro deles seriam subpacotes.
- `atores.py`, `mundo.py` e `fase01.py` são módulos
- Podemos importar assim:

```python
from fase01.fase01 import Abelha
from atores import atores
```

**Por que usar pacotes?**

- Para **organizar melhor** seu código.
- Para **evitar nomes repetidos** entre módulos.
- Para **separar responsabilidades** em partes reutilizáveis 

As suas soluções para os desafios deste mundo deverão se colocados no diretório
raiz do pacote, dessa forma (os nomes são ilustrativos):

```
meu_projeto/
├── atores/
│   ├── atores.py
│   └── mundo.py
└── fase01/
│   ├── fase01.py
│   └── codigo_inicial.py
├──solucao_fase01.py
├──solucao_fase02.py
└──solucao_fase**.py
```

Agora avance você para a fase 1 para começar a praticar.


[Próximo](fase01/README.md)

