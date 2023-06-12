import ticket 
import precio
import pelicula
print(pelicula.menu())
nombre = input("Ingresa tu nombre: ")
pelicula = input("Ingresa la pelicula que desees ver: ")
asientos = int(input("Ingresa el numero de asientos: "))
print("----------------------------------------------------------")
print(precio.precio(asientos))
print("----------------------------------------------------------")
print(ticket.ticekt(nombre,pelicula,asientos))
print("----------------------------------------------------------")

