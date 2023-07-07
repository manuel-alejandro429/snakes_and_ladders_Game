@isTest
public class FuncionesTest {
    
    @isTest
    public static void testDadoAleatorio() {
        for (Integer i = 0; i < 3; i++) {
            Integer randomNumber = Funciones.dado();
            System.assert(randomNumber > 0 && randomNumber < 6);
        }
    }
    
    @isTest
    public static void testVerificarCasilla() {
        List<Objeto> serpientes = new List<Objeto>{
            new Objeto('serpiente1', 14, 4),
            new Objeto('serpiente2', 19, 8)
        };

        List<Objeto> escaleras = new List<Objeto>{
            new Objeto('Escalera1', 3, 11),
            new Objeto('Escalera2', 6, 17)
        };

        List<Object> resultado = Funciones.verificarCasilla(escaleras, serpientes, 6);
        System.assert((Boolean)resultado[0]);
        System.assert((Integer)resultado[1] == 17);

        resultado = Funciones.verificarCasilla(escaleras, serpientes, 19);
        System.assert((Boolean)resultado[0]);
        System.assert((Integer)resultado[1] == 8);

        resultado = Funciones.verificarCasilla(escaleras, serpientes, 15);
        System.assert(!(Boolean)resultado[0]);
        System.assert((Integer)resultado[1] == 0);
    }
    
    @isTest
    public static void testVerificarPosiciones() {
        List<Jugador> jugadores = new List<Jugador>{
            new Jugador('Jugador1', 10),
            new Jugador('Jugador2', 15),
            new Jugador('Jugador3', 20)
        };
        System.assert(Funciones.verificarPosiciones(jugadores));

        jugadores = new List<Jugador>{
            new Jugador('Jugador1', 10),
            new Jugador('Jugador2', 25),
            new Jugador('Jugador3', 20)
        };
        System.assert(!Funciones.verificarPosiciones(jugadores));

        jugadores = new List<Jugador>{
            new Jugador('Jugador1', 25),
            new Jugador('Jugador2', 25),
            new Jugador('Jugador3', 25)
        };
        System.assert(!Funciones.verificarPosiciones(jugadores));
    }
}