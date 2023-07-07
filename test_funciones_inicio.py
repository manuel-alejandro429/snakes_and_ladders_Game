from funciones import inicio, dado, verificarPosiciones, verificarCasilla, flujoJuego
import pytest
from unittest.mock import patch


#Tests que prueban la función  inicio ( )
#
#

def test_inicio_creates_game():
    # Prueba que verifica si se crea una partida correctamente.
    # Se debe elejir la opción "a" y escribir el número de jugadores. 
    # De esta manera permite verificar que la función inicio ( ) devuelva una lista de jugadores no vacía.
    assert inicio() != []

def test_inicio_exits_game():
    # Prueba que verifica si se sale del juego correctamente.
    # Para ello elige la opción "b" y así verifica que la función termine la ejecución del programa.
    with pytest.raises(SystemExit):
        inicio()

def test_inicio_invalid_option():
    # Prueba que verifica el manejo de una opción inválida.
    # Proporciona una opción inválida y verifica que la función solicite una opción válida.
    seleccion = "c"
    with pytest.raises(SystemExit):
        inicio()


def test_inicio_adds_players():
    # Prueba que verifica si los jugadores se agregan correctamente.
    # Elige la opción "a", proporciona el número de jugadores y sus nombres.
    # Verifica que la función devuelva una lista de jugadores con los nombres correctos.
    #CUIDADO ...internamente este test hace todo, escoge la opción "a", asigna 3 jugadores y por ultimo les da nombres

    expected_players = ["Alice", "Bob", "Charlie"]
    user_input = [
        "a",
        str(len(expected_players)),
        *expected_players
    ]
    input_values = iter(user_input)

    #Lo siguiente es una función simulada
    def mock_input(prompt):
        return next(input_values)

    # Reemplazar la función input por una función simulada que devuelve los valores en input_values
    # Esto se hace utilizando el contexto de la función patch de pytest.
    with patch("builtins.input", mock_input):
        players = inicio()

    assert len(players) == len(expected_players)
    assert [player.nombre for player in players] == expected_players

