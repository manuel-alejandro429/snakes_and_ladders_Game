from funciones import inicio, dado, verificarPosiciones, verificarCasilla, flujoJuego

#Me permite probar que el número que me proporciona la función dado( ) si esta en el rango
#EL dado va de 1 a 6

def test_dado_aleatorio():
    #este ciclo es para hacerlo un par de veces.
    for x in range(3):
        randomNumber  = dado()
        assert randomNumber>0 and randomNumber<6