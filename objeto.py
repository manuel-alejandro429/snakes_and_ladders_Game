#POO 
#En la siguiente clase se establece el objeto tipo objeto.
#Estos hacen las veces de escalres o serpientes

class Objeto:

    id = str
    inicio = int
    final  = int 

    def __init__(self, id, inicio, final):
        
        self.id = id
        self.inicio = inicio
        self.final = final

    

