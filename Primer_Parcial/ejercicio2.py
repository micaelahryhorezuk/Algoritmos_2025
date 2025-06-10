# Dada una lista de personajes de marvel (la desarrollada en clases) debe tener 100 o mas, resolver:
#a. Listado ordenado de manera ascendente por nombre de los personajes.
#b. Determinar en que posicion esta The Thing y Rocket Raccoon.
#c. Listar todos los villanos de la lista.
#d. Poner todos los villanos en una cola para determinar luego cuales aparecieron antes de 1980.
#e. Listar los superheores que comienzan con  Bl, G, My, y W.
#f. Listado de personajes ordenado por nombre real de manera ascendente de los personajes.
#g. Listado de superheroes ordenados por fecha de aparación.
#h. Modificar el nombre real de Ant Man a Scott Lang.
#i. Mostrar los personajes que en su biografia incluyan la palabra time-traveling o suit.
#j. Eliminar a Electro y Baron Zemo de la lista y mostrar su información si estaba en la lista.

from typing import Any, Optional
from clase_lista import List
from Lista_data_superheroes import superheroes
from clase_cola import Queue

class Superhero:
    def __init__(self, nombre: str, nombre_real: str, fecha_aparicion: str, biografia: str, villano: bool):
        self.nombre = nombre
        self.nombre_real = nombre_real
        self.fecha_aparicion = fecha_aparicion
        self.biografia = biografia
        self.villano = villano

    def __str__(self):
        return (str(self.nombre) + "  " + str(self.nombre_real) + "  " + str(self.fecha_aparicion) + "  " + str(self.biografia) + "  Villano: " + str(self.villano))
       #converti todo a string para que no falle al imprimir

def ordenar_por_nombre(item):
    return item.nombre
lista_superheroes = List()
lista_superheroes.add_criterion("nombre", ordenar_por_nombre)
#Convertir cada héroe en un objeto Superhero
for heroe in superheroes:
    heroe_obj = Superhero(
        nombre=heroe['name'],
        nombre_real=heroe['real_name'],
        fecha_aparicion=heroe['first_appearance'],
        biografia=heroe['short_bio'],
        villano=heroe['is_villain']
    )
    lista_superheroes.append(heroe_obj)

print("\n#a. Listado ordenado de manera ascendente por nombre de los personajes.\n")
#a. Listado ordenado de manera ascendente por nombre de los personajes.
# Agregar criterio de ordenación por nombre
lista_superheroes.sort_by_criterion("nombre")
print("Listado de personajes ordenado por nombre:")
lista_superheroes.show()  # Mostrar la lista de personajes ordenados por nombre de manera ascendente

print("\n#b. Determinar en qué posición está The Thing y Rocket Raccoon.\n")
#b. Determinar en qué posición está The Thing y Rocket Raccoon.
def buscar_personaje(nombre: str):
    indice = lista_superheroes.search(nombre, "nombre")
    if indice is not None:
        return (nombre, "encontrado en la posicion", indice) 
    else:
        return (nombre, "no encontrado")
print(buscar_personaje("The Thing"))
print(buscar_personaje("Rocket Raccoon"))

print("\n#c. Listar todos los villanos de la lista.\n")
#c. Listar todos los villanos de la lista.
for heroe in lista_superheroes:
    if heroe.villano:
        print("Villano:", heroe)

print("\n#d. Poner todos los villanos en una cola para determinar luego cuáles aparecieron antes de 1980.\n")
#d. Poner todos los villanos en una cola para determinar luego cuáles aparecieron antes de 1980.
cola_villanos = Queue()
for heroe in lista_superheroes:
    if heroe.villano and heroe.fecha_aparicion < 1980:  # Asumiendo que la fecha de aparición está en formato "YYYY-MM-DD"
        cola_villanos.arrive(heroe)

print("Cola de villanos: ")
cola_villanos.show()

print("\n#e. Listar los superhéroes que comienzan con Bl, G, My, y W.\n")
#e. Listar los superhéroes que comienzan con Bl, G, My, y W.
for heroe in lista_superheroes:
    if heroe.nombre.startswith(("Bl", "G", "My", "W")):
        print("Superhéroe que comienza con Bl, G, My o W:", heroe)

print("\n#f. Listado de personajes ordenado por nombre real de manera ascendente de los personajes.\n")
#f. Listado de personajes ordenado por nombre real de manera ascendente de los personajes.
def ordenar_por_nombre_real(item):
    return str(item.nombre_real)
# Convertimos todos los valores a string ya que hay algunos que son nulos y entonces falla al ejecutar

lista_superheroes.add_criterion("nombre_real", ordenar_por_nombre_real)  # Agregar criterio de ordenación por nombre real
lista_superheroes.sort_by_criterion("nombre_real")
print("Listado de personajes ordenado por nombre real:")
lista_superheroes.show()  

print("\n#g. Listado de superhéroes ordenados por fecha de aparición.\n")
#g. Listado de superhéroes ordenados por fecha de aparición.
def ordenar_por_fecha_aparicion(item):
    return item.fecha_aparicion
lista_superheroes.add_criterion("fecha_aparicion", ordenar_por_fecha_aparicion) 
lista_superheroes.sort_by_criterion("fecha_aparicion")
print("Listado de superhéroes ordenados por fecha de aparición:")
lista_superheroes.show()

print("\n#h. Modificar el nombre real de Ant Man a Scott Lang.\n")
#h. Modificar el nombre real de Ant Man a Scott Lang.
for heroe in lista_superheroes:
    if heroe.nombre == "Ant Man":
        heroe.nombre_real = "Scott Lang"
        print("Nombre real de Ant Man cambiado a Scott Lang")
        break
else:
    print("Ant Man no encontrado")


print("\n#i. Mostrar los personajes que en su biografía incluyan la palabra time-traveling o suit.\n")
#i. Mostrar los personajes que en su biografía incluyan la palabra time-traveling o suit.
for heroe in lista_superheroes:
    if "time-traveling" in heroe.biografia or "suit" in heroe.biografia:
        print("Personaje con 'time-traveling' o 'suit' en su biografía:", heroe)

print("\n#j. Eliminar a Electro y Baron Zemo de la lista y mostrar su información si estaba en la lista.\n")
#j. Eliminar a Electro y Baron Zemo de la lista y mostrar su información si estaba en la lista.
print(lista_superheroes.delete_value("Electro", key_value="nombre"))  # Eliminar Electro
print(lista_superheroes.delete_value("Baron Zemo", key_value="nombre"))  # Eliminar Baron Zemo