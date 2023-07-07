-----------------------------------------EJECUCIÓN DEL JUEGO ESCALERAS Y SERPIENTE ----------------------

Pasos:

1.activar el Enviroment por consola ubicandose en la siguiente dirección: 

	PS C:\Users\manue\Desktop\serpientes y escaleras project\env\Scripts\activate 

una vez de enter debera aparecer dentro del enviroment: env) 



2.Una vez este activado, ubcarse en la carpeta general y ejecutar: Python main.py


3. Siga el flujo del juego, pueden ser 1,2,3 ... jugadores. 


-----------------------------------------PRUEBAS CON PYTEST ----------------------------------------------

1. Una vez este con el enviroment activado y estando en la dirección de la carpeta principal,
   puede ejecutar el siguiente comando: 

	pytest -v -s

   como las pruebas estan en un orden especifico, si desea hacerlas correctamente ha de hacer lo siguiente:
	
   1er TEST ---->  Escribir "a" luego un número de jugadores  y sus nombres.
   2do TEST ---->  Escribir la letra "b" para simular que el usuario desea salir.
   3er TEST ---->  Escribir cualquier opcion que no este en el menú, por ejemplo "j" y luego escribir "b" para salir
    
   .... El resto de tests se realizan solos, en total han de ejecutarse 7 Tests correctos. 

