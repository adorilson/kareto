import turtle


def muda_palco():
    import random

    cores = ("lightyellow", "lightblue", "lightcyan",  "lightgray",
             "lightcoral",  "lightpink", "lightsalmon", "lightgreen")
    cor = random.choice(cores)

    palco = turtle.Screen()
    palco.bgcolor(cor)


## Configuracao da escritora ## 
# Inicializa a tartaruga escritora
escritora = turtle.Turtle()
escritora.goto(-400, 400)
escritora.tempo = 0
escritora.write('Contagem ainda não começou.', font=('Arial', 20, 'bold'))

# Define função que irá contar a passagem do tempo e
# escrever esse tempo na tela
def atualiza_tempo():
    escritora.clear()
    escritora.write(f'Compasso: {escritora.tempo}', font=('Arial', 20, 'bold'))
    escritora.tempo = escritora.tempo + 1
    turtle.ontimer(atualiza_tempo, 1000)

# Registra que a função atualiza_tempo será chamada após 1000 milissegundos
turtle.ontimer(atualiza_tempo, 1000)

## Fim da configuração da escritora ## 

## Configuração da dançarina ##

# Inicializa a tartaruga dançarina
dançarina = turtle.Turtle()
dançarina.shape('turtle')
dançarina.shapesize(5)
dançarina.setheading(90)

def movimenta():
    import random

    posicoes = -200, -100, 0, 100, 200
    novo_x = random.choice(posicoes)  
    novo_y = random.choice(posicoes)  
    dançarina.goto(novo_x, novo_y)       

    turtle.ontimer(movimenta, 2000)

## Fim da configuração da dançarina ##

## Configuração da dançarina de apoio ##

# Inicializa a dançarina de apoio
apoio = turtle.Turtle()
apoio.shape('turtle')
apoio.setheading(90)
apoio.setx(100)

## Fim da configuração da dançarina ##

# Funções que em conjunto fazem as dançarinas dançarem
def mexe_direita():
    dançarina.setheading(95)
    apoio.setheading(95)
    muda_palco()
    turtle.ontimer(mexe_esquerda, 200)    


def mexe_esquerda():
    dançarina.setheading(85)
    apoio.setheading(85)
    muda_palco()
    turtle.ontimer(mexe_direita, 200)


def move_direita():
    dançarina.setx(10)
    apoio.setx(10)
    turtle.ontimer(move_esquerda, 200)    


def move_esquerda():
    dançarina.setx(-10)
    apoio.setx(-10)
    turtle.ontimer(move_direita, 200)


turtle.ontimer(mexe_esquerda, 4000)
turtle.ontimer(move_esquerda, 6000)
turtle.ontimer(movimenta, 2000)

# Fim das funções que em conjunto fazem as dançarinas dançarem


turtle.mainloop()
