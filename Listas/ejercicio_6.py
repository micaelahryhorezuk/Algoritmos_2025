#Dada una lista de superhéroes de comics, de los cuales se conoce su nombre, año aparición,

#casa de comic a la que pertenece (Marvel o DC) y biografía, implementar la funciones necesa- 
# rias para poder realizar las siguientes actividades:

    #a. eliminar el nodo que contiene la información de Linterna Verde;
    # b. mostrar el año de aparición de Wolverine;
    # c. cambiar la casa de Dr. Strange a Marvel;
    # d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra
    # “traje” o “armadura”;
    # e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición
    # sea anterrior a 1963;
    # f. mostra la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
    # g. mostrar toda la información de Flash y Star-Lord;
    # h. listar los superhéroes que comienzan con la letra B, M y S;
    # i. determinar cuántos superhéroes hay de cada casa de comic.
from typing import Any, Optional
from clase_lista import List
from listaSuperheroes import superheroes

class SuperHeroe:
    def __init__(self, nombre: str, alias: str, anio: int, casa: str, short_bio: str, villano: bool):
        self.nombre = nombre
        self.alias = alias
        self.anio = anio
        self.casa = casa
        self.short_bio = short_bio
        self.villano = villano
    def __str__(self):
        return f"{self.nombre} ({self.alias}) - {self.anio} - {self.casa} - {self.short_bio} - Villano: {self.villano}"

def ordenar_por_nombre(item) :
    return item.nombre
list_superheroes = List()
list_superheroes.add_criterion("nombre", ordenar_por_nombre)  # Agregar criterio de ordenación por nombre


for heroe in superheroes:
    # Convertir cada héroe en un objeto SuperHeroe
    heroe_obj = SuperHeroe(
        nombre=heroe['nombre'],
        alias=heroe.get('alias', ''),
        anio=heroe['anio'],
        casa=heroe['casa'],
        short_bio=heroe['bio'],
        villano=False  # Asumimos que no es villano por defecto
    )
    list_superheroes.append(heroe_obj) #agregamos el objeto a la lista



#a. eliminar el nodo que contiene la información de Linterna Verde;
print(list_superheroes.delete_value("Linterna Verde", key_value="nombre"))  # Eliminar Linterna Verde

print("Lista después de eliminar Linterna Verde:")
list_superheroes.show()  # Mostrar la lista después de eliminar Linterna Verde

# b. mostrar el año de aparición de Wolverine;
indice = list_superheroes.search("Wolverine", key_value="nombre")
if indice is not None:
    print("Año de aparicion de Wolverine ",list_superheroes[indice].anio )
else:
    print("Wolverine no encontrado")

# c. cambiar la casa de Dr. Strange a Marvel;
indice = list_superheroes.search("Dr. Strange", key_value="nombre")
if indice is not None:
    list_superheroes[indice].casa = "Marvel"
    print("Casa de Dr. Strange cambiada a Marvel")
else:
    print("Dr. Strange no encontrado")

# d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra “traje” o “armadura”;
print("Superhéroes con 'traje' o 'armadura' en su biografía:")
for heroe in list_superheroes:
    if "traje" in heroe.short_bio.lower() or "armadura" in heroe.short_bio.lower():
        print(heroe.nombre)

# e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición sea anterior a 1963;
print("Superhéroes anteriores a 1963:")
for heroe in list_superheroes:
    if heroe.anio < 1963:
        print(heroe.nombre, "-", heroe.casa)

# f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
print("Casas de Capitana Marvel y Mujer Maravilla:")
for heroe in list_superheroes:
    if heroe.nombre in ["Capitana Marvel", "Mujer Maravilla"]:
        print(heroe.nombre, "-", heroe.casa)

# g. mostrar toda la información de Flash y Star-Lord;
print("Información de Flash y Star-Lord:")
for heroe in list_superheroes:
    if heroe.nombre in ["Flash", "Star-Lord"]:
        print(heroe)
# h. listar los superhéroes que comienzan con la letra B, M y S;
print("Superhéroes que comienzan con B, M y S:")
for heroe in list_superheroes:
    if heroe.nombre[0] in ['B', 'M', 'S']:
        print(heroe.nombre)
# i. determinar cuántos superhéroes hay de cada casa de comic.
casa_count = {}
for heroe in list_superheroes:
    if heroe.casa not in casa_count:
        casa_count[heroe.casa] = 0
    casa_count[heroe.casa] += 1
print("Cantidad de superhéroes por casa de cómic:", casa_count)
