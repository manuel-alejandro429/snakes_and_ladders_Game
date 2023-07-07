from funciones import inicio, dado, verificarPosiciones, verificarCasilla, flujoJuego
from objeto import Objeto

def test_verificar_casilla():
    # Defino algunas escaleras y serpientes
    serpientes = [
        Objeto("serpiente1", 14, 4),
        Objeto("serpiente2", 19, 8),
    ]

    escaleras = [
        Objeto("Escalera1", 3, 11),
        Objeto("Escalera2", 6, 17),
    ]

    # A continuación se prueba el caso en el que el jugador cae en una escalera
    resultado = verificarCasilla(escaleras, serpientes, 6)
    assert resultado[0] == True
    assert resultado[1] == 17

    # A continuación se prueba el caso en el que el jugador cae en una serpiente
    resultado = verificarCasilla(escaleras, serpientes, 19)
    assert resultado[0] == True
    assert resultado[1] == 8

    # A continuación se prueba el caso en el que el jugador cae en una casilla normal, sin objeto
    resultado = verificarCasilla(escaleras, serpientes, 15)
    assert resultado[0] == False
    assert resultado[1] == 0