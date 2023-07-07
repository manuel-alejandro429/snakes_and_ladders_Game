public class Funciones {
    public static List<Jugador> inicio() {
        List<Jugador> jugadores = new List<Jugador>();
        Boolean seleccionStatus = false;
        
        String seleccion = System.readLine("""

                        SERPIENTES Y ESCALERAS
        
        Escribe la letra de la opción que deseas ejecutar.
        
        a) Crear partida
        b) Salir 
        
        :_""");
        
        while (!seleccionStatus) {
            if (seleccion.equals('a')) {
                seleccionStatus = true;
                Integer participantes = Integer.valueOf(System.readLine("""

                        NUEVA PARTIDA CREADA
        
        Escribe el número de jugadores (consejo: de 2 a 4 jugadores) 
        :_"""));
                
                for (Integer num = 0; num < participantes; num++) {
                    String name = System.readLine("""

        Escibe el nombre del participante número {}
        : _""".format(String.valueOf(num + 1)));
                    
                    jugadores.add(new Jugador(name));
                }
            } else if (seleccion.equals('b')) {
                seleccionStatus = true;
                
                System.debug("""
                        VUELVE PRONTO - SERPIENTES Y ESCALERAS
                """);
                
                jugadores = new List<Jugador>();
                System.exit(0);
            } else {
                seleccion = System.readLine("""

        Opción incorrecta, elige una que sí esté dentro de las opciones del menú.
        
        a) Crear partida
        b) Salir 
        
        :_""");
            }
        }
        
        return jugadores;
    }
    
    public static Integer dado() {
        Integer NumberAleatorio = Math.round(Math.random() * 5) + 1;
        return NumberAleatorio;
    }
    
    public static Boolean verificarPosiciones(List<Jugador> jugadores) {
        Boolean estado = true;
        
        for (Jugador jugador : jugadores) {
            if (jugador.posicion == 25) {
                estado = false;
                break;
            }
        }
        
        return estado;
    }
    
    public static List<Object> verificarCasilla(List<Objeto> escaleras, List<Objeto> serpientes, Integer individuoPosicion) {
        Boolean especial = false;
        List<Object> resultado = new List<Object>();
        
        for (Objeto objeto : escaleras) {
            if (objeto.inicio == individuoPosicion) {
                String mensaje = 'Caiste en una ESCALERA, te moveras hasta la casilla ' + String.valueOf(objeto.final) + ', FELICITACIONES!';                
                resultado.add(true);
                resultado.add(objeto.final);
                resultado.add(mensaje);
                especial = true;
                break;
            }
        }
        
        if (!especial) {
            for (Objeto objeto : serpientes) {
                if (objeto.inicio == individuoPosicion) {
                    String mensaje = 'LO SIENTO, caiste en una SERPIENTE, te moveras hasta la casilla ' + String.valueOf(objeto.final) + '!';                    
                    resultado.add(true);
                    resultado.add(objeto.final);
                    resultado.add(mensaje);
                    especial = true;
                    break;
                }
            }
        }
        
        if (!especial) {
            resultado.add(false);
            resultado.add(0);
            resultado.add(0);
        }
        
        return resultado;
    }
    
    public static void flujoJuego(List<Jugador> jugadores, List<Objeto> escaleras, List<Objeto> serpientes) {
        List<Jugador> jugadoresOrdenados = new List<Jugador>();
        jugadoresOrdenados.addAll(jugadores);
        
        // Aquí puedes utilizar el método de Apex para ordenar la lista jugadoresOrdenados
        
        System.debug("""

        Se BARAJARON los puestos. El jugador que inicia es {}.
        """.format(jugadoresOrdenados[0].nombre));
        
        Boolean estadoJuego = true;
        String ganadorName = 'POR DEFINIR';
        
        while (estadoJuego) {
            for (Jugador individuo : jugadoresOrdenados) {
                estadoJuego = verificarPosiciones(jugadoresOrdenados);
                
                if (estadoJuego) {
                    String accion = System.readLine("""

        {} Desea lanzar? Escriba 'si':
        :_
                    """.format(individuo.nombre));
                    
                    if (accion.equals('si')) {
                        Integer lanzamiento = dado();
                        
                        if (individuo.posicion + lanzamiento <= 25) {
                            List<Object> casillaTipo = verificarCasilla(escaleras, serpientes, individuo.posicion + lanzamiento);
                            
                            if ((Boolean)casillaTipo[0]) {
                                System.debug("""

        Sacaste con el dado el número {}""".format(lanzamiento));
                                individuo.posicion = (Integer)casillaTipo[1];
                                ganadorName = individuo.nombre;
                                System.debug((String)casillaTipo[2]);
                            } else {
                                individuo.posicion += lanzamiento;
                                ganadorName = individuo.nombre;
                                System.debug("""

        Te moveras {} posiciones. Quedas en la casilla {}""".format(lanzamiento, individuo.posicion));
                            }
                        } else {
                            System.debug("""

        No podrás moverte {} posiciones. Supera el límite del tablero. Espera otroturno.""".format(lanzamiento));
                        }
                    }
                }
            }
            
            estadoJuego = verificarPosiciones(jugadoresOrdenados);
        }
        
        System.debug("""
        FELICITACIONES {} ERES EL GANADOR DE ESTA PARTIDA !
                        Vuelve pronto
                    ESCALERAS Y SERPIENTES
        ....................................................
        """.format(ganadorName));
    }
}