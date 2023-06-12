def ticekt(nombre,asientos, pelicula):
    archivo = open('ticket.txt', 'w')
    nombre = f"A nombre de {nombre} para la peli de {asientos}, Con asientos de: {pelicula} "
    archivo.write(nombre)
    archivo.close()
    print("Archivo en txt")
    
    leer = open('ticket.txt', 'r')
    leerarchivo = leer.read()
    print(leerarchivo)
    print("Gracias por su compra!")




    
    

