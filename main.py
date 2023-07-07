from funciones import inicio, flujoJuego
#from jugador import Jugador
from objeto import Objeto

if __name__ == "__main__":

    #Estableciendo las Serpientes existentes en el tablero de juego 

    snake1 = Objeto("serpiente1", 14, 4)
    snake2 = Objeto("serpiente2", 19, 8)
    snake3 = Objeto("serpiente3", 22, 20)
    snake4 = Objeto("serpiente4", 24, 16)

    snakes = [snake1, snake2, snake3, snake4]
    
    #Estableciendo las Escaleras existentes en el tablero de juego 
    
    stair1 = Objeto("Escalera1", 3, 11)
    stair2 = Objeto("Escalera2", 6, 17)
    stair3 = Objeto("Escalera3", 9, 18)
    stair4 = Objeto("Escalera4", 10, 12)

    stairs = [ stair1, stair2, stair3, stair4]
    
    #---------------------------------------------------------------
    #A continuación las funciones son invocadas y se inicia el flujo del juego 

    jugadoresPartida = inicio()
    flujoJuego(jugadoresPartida, stairs, snakes)