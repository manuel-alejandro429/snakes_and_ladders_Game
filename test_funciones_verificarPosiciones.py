from funciones import inicio, dado, verificarPosiciones, verificarCasilla, flujoJuego
from jugador import Jugador

#A continuación se harán los tests necesarios para probar la función verificarPosiciones( )

def test_verificar_posiciones():
    # En el primer caso, se da como entrada un grupo de jugadores, con posiciones diferentes a 25 
    jugadores = [
        Jugador("Jugador1", 10),
        Jugador("Jugador2", 15),
        Jugador("Jugador3", 20)
    ]
    assert verificarPosiciones(jugadores) == True

    #En el segundo caso, se da como entrada un grupo de jugadores, uno de ellos con posicioón igual a 25 
    jugadores = [
        Jugador("Jugador1", 10),
        Jugador("Jugador2", 25),
        Jugador("Jugador3", 20)
    ]
    assert verificarPosiciones(jugadores) == False

    #En el caso final, todos los jugadores tienen una posición igual a 25
    jugadores = [
        Jugador("Jugador1", 25),
        Jugador("Jugador2", 25),
        Jugador("Jugador3", 25)
    ]
    assert verificarPosiciones(jugadores) == False
