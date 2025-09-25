#Se dispone de una lista de todos los Jedi, de cada uno de estos se conoce su nombre, maestros,
#colores de sable de luz usados y especie. implementar las funciones necesarias para resolver las
#actividades enumeradas a continuación:
#a. listado ordenado por nombre y por especie;
#b. mostrar toda la información de Ahsoka Tano y Kit Fisto;
#c. mostrar todos los padawan de Yoda y Luke Skywalker, es decir sus aprendices;
#d. mostrar los Jedi de especie humana y twi'lek;
#e. listar todos los Jedi que comienzan con A;
#f. mostrar los Jedi que usaron sable de luz de más de un color;
#g. indicar los Jedi que utilizaron sable de luz amarillo o violeta;
#h. indicar los nombre de los padawans de Qui-Gon Jin y Mace Windu, si los tuvieron.

from typing import Any, Optional
from clase_lista import List
from lista_jedis import jedis

class Jedi: 
    def __init__(self, nombre: str, maestros: list, colores_sable: list, especie: str):
        self.nombre = nombre
        self.maestros = maestros
        self.colores_sable = colores_sable
        self.especie = especie

    def __str__(self):
        return f"{self.nombre} - Maestros: {', '.join(self.maestros) if self.maestros else 'Ninguno'} - Colores de sable: {', '.join(self.colores_sable)} - Especie: {self.especie}"

#a. listado ordenado por nombre y por especie;

def ordenar_por_nombre(item) :
    return item.nombre

def ordenar_por_especie(item) :
    return item.especie
list_jedis = List()
list_jedis.add_criterion("nombre", ordenar_por_nombre)  # Agregar criterio de ordenación por nombre
list_jedis.add_criterion("especie", ordenar_por_especie)  # Agregar criterio de ordenación por especie

for jedi in jedis:
    # Convertir cada Jedi en un objeto Jedi
    jedi_obj = Jedi(
        nombre=jedi['nombre'],
        maestros=jedi['maestros'],
        colores_sable=jedi['colores_sable'],
        especie=jedi['especie']
    )
    list_jedis.append(jedi_obj) #agregamos el objeto a la lista

#b. mostrar toda la información de Ahsoka Tano y Kit Fisto;

indice = list_jedis.search("Ahsoka Tano", key_value="nombre")
if indice is not None:
    print("Información de Ahsoka Tano:")
    print(list_jedis.get_element(indice))
else:
    print("Ahsoka Tano no encontrada.")
indice = list_jedis.search("Kit Fisto", key_value="nombre")
if indice is not None:
    print("Información de Kit Fisto:")
    print(list_jedis.get_element(indice))
else:
    print("Kit Fisto no encontrado.")

#c. mostrar todos los padawan de Yoda y Luke Skywalker, es decir sus aprendices;

print("Padawans de Yoda:")
for jedi in list_jedis:
    if "Yoda" in jedi.maestros:
        print(jedi.nombre)
print("Padawans de Luke Skywalker:")
for jedi in list_jedis:
    if "Luke Skywalker" in jedi.maestros:
        print(jedi.nombre)

#d. mostrar los Jedi de especie humana y twi'lek;
print("Jedi de especie humana:")
for jedi in list_jedis:
    if jedi.especie.lower() == "humano":
        print(jedi.nombre)
print("Jedi de especie twi'lek:")
for jedi in list_jedis:
    if jedi.especie.lower() == "twi'lek":
        print(jedi.nombre)

#e. listar todos los Jedi que comienzan con A;

print("Jedi que comienzan con A:")
for jedi in list_jedis:
    if jedi.nombre.startswith("A"):
        print(jedi.nombre)

#f. mostrar los Jedi que usaron sable de luz de más de un color;
print("Jedi que usaron sable de luz de más de un color:")
for jedi in list_jedis:
    if len(jedi.colores_sable) > 1:
        print(jedi.nombre)

#g. indicar los Jedi que utilizaron sable de luz amarillo o violeta;
print("Jedi que utilizaron sable de luz amarillo o violeta:")
for jedi in list_jedis:
    if "amarillo" in jedi.colores_sable or "violeta" in jedi.colores_sable:
        print(jedi.nombre)

#h. indicar los nombre de los padawans de Qui-Gon Jin y Mace Windu, si los tuvieron.
print("Padawans de Qui-Gon Jin:")
for jedi in list_jedis:
    if "Qui-Gon Jinn" in jedi.maestros:
        print(jedi.nombre)
print("Padawans de Mace Windu:")
for jedi in list_jedis:
    if "Mace Windu" in jedi.maestros:
        print(jedi.nombre)
print("No se encontraron padawans de Mace Windu.")
