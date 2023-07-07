import sys
import random as r

from jugador import Jugador
    
#La función inicio() permite inicializar el juego, es el primer menú con el que el usuario puede interactuar
def inicio():

    #Aquí se almacenan los nombres/instancias del objeto jugador.
    jugadores = []
    seleccionStatus = False

    #menu de inicio: Crear partida o salir
    seleccion = input(  
""" 

                        SERPIENTES Y ESCALERAS

        
        Escribe la letra de la opción que deseas ejecutar.

        a) Crear partida
        b) Salir 

        :_""")

    #El siguiente while es para condicionar la elección del usuario.
    #Se queda dentro del while hasta que el jugador selección la opción a o b.
    while seleccionStatus == False:

        if seleccion == "a":

            seleccionStatus = True
            participantes = int(input("""

                        NUEVA PARTIDA CREADA

        
        Escribe el número de jugadores (consejo: de 2 a 4 jugadores) 
        :_"""))

            for num in range(participantes):
                name = input("""
                
        Escibe el nombre del participante número {}
        : _""".format(num+1))
                
                jugadores.append(Jugador(name))


        elif seleccion == "b":  
          seleccionStatus = True

          print("""
                        VUELVE PRONTO - SERPIENTES Y ESCALERAS
          """)
          jugadores = []
          sys.exit()

        else: 
            seleccion = input("""
        
        Opción incorrecta, elige una que si este dentro de las opciones del menú.

        a) Crear partida
        b) Salir 

        :_""")
    return (jugadores)

#La función dado() hace el comportamiento aleatório de tirar un dado de 6 caras
def dado ():
    NumberAleatorio = r.randrange(1,6)
    return NumberAleatorio

#Por cada iteración del juego, se verifica si ya existe un ganador, si es así, esta función lo alerta!
def verificarPosiciones (jugadores):
    estado = True
    for x in range (len(jugadores)):
        numero = jugadores[x].posicion
        if numero == 25:  #Este número es el que condicionará la longitud de nuestro tablero
            estado = False
    return estado 

#La función verificarCasilla( ) es la encargada de validar si donde cayó el jugador existe algun objeto especial (Serpiente o Escalera).
#Una vez valida lo anterior, efectua la acción de dicho objeto, adelantar o retrasar al jugador. 
def verificarCasilla(escaleras, serpientes, individuoPosicion):
    
    especial = False

    for objeto in escaleras:
        if (objeto.inicio) == individuoPosicion:
            mensaje = """

        Caiste en una ESCALERA, te moveras hasta la casilla {}, FELICITACIONES!""".format(objeto.final)
            especial = True
            return (True, objeto.final, mensaje)
        
    for objeto in serpientes:
        if (objeto.inicio) == individuoPosicion:
            mensaje = """
        LO SIENTO caiste en una SERPIENTE, te moveras hasta la casilla {} !""".format(objeto.final)
            especial = True
            return (True, objeto.final, mensaje)
        
    if especial == False:
        return (False, 0, 0)
        


#La función flujoJuego( ) como lo indica su nombre, permite todo el flujo y la iteración
#Acoge lanzar los dados, avanzar, entre otro. 
def flujoJuego(jugadores, escaleras, serpientes):

    #print(jugadores[0].nombre)

    jugadoresOrdenados = r.sample(jugadores,len(jugadores))

    #print(jugadoresOrdenados[0].nombre)

    print("""

        Se BARAJARON los puestos. El jugador que inicia es {}.
    """.format(jugadoresOrdenados[0].nombre))

    estadoJuego = True

    ganadorName = "POR DEFINIR"

    while estadoJuego:

        for individuo in jugadoresOrdenados:
            estadoJuego = verificarPosiciones(jugadoresOrdenados)
            if estadoJuego == True:
                accion = input (""" 

        {} Desea lanzar ? Esciba (si)
        :_
            """.format(individuo.nombre))

                if accion == "si":
                    lanzamiento = dado()
                    if (individuo.posicion + lanzamiento) <= 25: 
                        casillaTipo = verificarCasilla(escaleras, serpientes, (individuo.posicion + lanzamiento))
                        if casillaTipo[0] == True:
                            print("""
        Sacaste con el dado el número {}""".format(lanzamiento))
                            individuo.posicion = casillaTipo[1]
                            ganadorName = individuo.nombre
                            print(casillaTipo[2])
                        else:      
                            individuo.posicion = individuo.posicion + lanzamiento
                            ganadorName = individuo.nombre
                            print(""" 
        Te moveras {} posiciones. Quedas en la casilla {}""".format(lanzamiento, individuo.posicion))
                    else:
                        print(""" 
        No podras moverte { } posiciones. Supera el límite del tablero. Espera otro turno.""".format(lanzamiento))
       
        estadoJuego = verificarPosiciones(jugadoresOrdenados)

    print(""" 
        FELICITACIONES {} ERES EL GANADOR DE ESTA PARTIDA !

                        Vuelve pronto
                    ESCALERAS Y SERPIENTES

        ....................................................
    """.format(ganadorName))
