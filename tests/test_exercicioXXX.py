import turtle


def setup_function():
    turtle.mainloop = lambda: None
    turtle.setup(500, 500)


def teardown_function():
    turtle.clearscreen()


def test_exercicio001():
    turtle.Screen().title('Testando exercicio001')
    import exercicio001


def test_exercicio002():
    turtle.Screen().title('Testando exercicio002')
    import exercicio002


def test_exercicio003():
    turtle.Screen().title('Testando exercicio003')
    import exercicio003


def test_exercicio004():
    turtle.Screen().title('Testando exercicio004')
    import exercicio004


def test_exercicio005():
    turtle.Screen().title('Testando exercicio005')
    import exercicio005


def test_exercicio006():
    turtle.Screen().title('Testando exercicio006')
    import exercicio006


def test_exercicio007():
    turtle.Screen().title('Testando exercicio007')
    import exercicio007


def test_exercicio008():
    turtle.Screen().title('Testando exercicio008')
    import exercicio008


def test_exercicio009():
    turtle.Screen().title('Testando exercicio009')
    import exercicio009


def test_exercicio010():
    turtle.Screen().title('Testando exercicio010')
    import exercicio010
