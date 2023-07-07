public class MainExecution {
    public static void main(String[] args) {
        // Estableciendo las Serpientes existentes en el tablero de juego
        Objeto snake1 = new Objeto('serpiente1', 14, 4);
        Objeto snake2 = new Objeto('serpiente2', 19, 8);
        Objeto snake3 = new Objeto('serpiente3', 22, 20);
        Objeto snake4 = new Objeto('serpiente4', 24, 16);
        
        List<Objeto> snakes = new List<Objeto>();
        snakes.add(snake1);
        snakes.add(snake2);
        snakes.add(snake3);
        snakes.add(snake4);
        
        // Estableciendo las Escaleras existentes en el tablero de juego
        Objeto stair1 = new Objeto('Escalera1', 3, 11);
        Objeto stair2 = new Objeto('Escalera2', 6, 17);
        Objeto stair3 = new Objeto('Escalera3', 9, 18);
        Objeto stair4 = new Objeto('Escalera4', 10, 12);
        
        List<Objeto> stairs = new List<Objeto>();
        stairs.add(stair1);
        stairs.add(stair2);
        stairs.add(stair3);
        stairs.add(stair4);
        
        // ---------------------------------------------------------------
        // A continuación, se invocan las funciones y se inicia el flujo del juego
        
        List<Jugador> jugadoresPartida = Funciones.inicio();
        Funciones.flujoJuego(jugadoresPartida, stairs, snakes);
    }
}
