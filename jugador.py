#POO 
#En la siguiente clase se establece el objeto tipo Jugador.
class Jugador: 
    
    nombre = str
    posicion = int

    def __init__(self, nombre, posicion = 0):

        self.nombre  = nombre
        self.posicion = posicion
        