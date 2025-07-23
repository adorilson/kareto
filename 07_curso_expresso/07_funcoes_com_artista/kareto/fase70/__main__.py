import turtle

def desenhar_quadrado():
    for _ in range(4):
        artista.forward(100)
        artista.right(90)

artista = turtle.Turtle()

desenhar_quadrado()
artista.penup()
artista.backward(175)
artista.pendown()
desenhar_quadrado()

turtle.mainloop()

