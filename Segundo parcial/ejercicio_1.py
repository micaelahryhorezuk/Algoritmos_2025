#Ejercicio 1: Se tiene los datos de Pokémons de las 9 generaciones cargados de manera aleatoria (1025 en total) 
#de los cuales se conoce su nombre, número, tipo/tipos, debilidad frente a tipo/tipos, si tiene mega evolucion (bool) 
#y si tiene forma gigamax (bool) para el cual debemos construir tres árboles para acceder de manera eficiente a los datos 
#contemplando lo siguiente:
#los índices de cada uno de los árboles deben ser nombre, número y tipo;
#mostrar todos los datos de un Pokémon a partir de su número y nombre –para este último, la búsqueda debe ser por proximidad, 
#es decir si busco “bul” se deben mostrar todos los Pokémons cuyos nombres comiencen o contengan dichos caracteres–;
#mostrar todos los nombres de los Pokémons de un determinado tipo: fantasma, fuego, acero y eléctrico;
#realizar un listado en orden ascendente por número y nombre de Pokémon, y además un listado por nivel por nombre;
#mostrar todos los Pokémons que son débiles frente a Jolteon, Lycanroc y Tyrantrum;
#mostrar todos los tipos de Pokémons y cuántos hay de cada tipo;
#determinar cuantos Pokémons tienen megaevolucion.
#determinar cuantos Pokémons tiene forma gigamax.

from  typing import Any, Optional
from tree import BinaryTree
from queue_ import Queue

# lista de datos de Pokémons de ejemplo
datos_pokemon = [
    {"nombre": "Bulbasaur", "numero": 1, "tipos": ["Planta", "Veneno"], "debilidades": ["Fuego", "Hielo", "Volador", "Psíquico"], "tiene_mega_evolucion": False, "tiene_forma_gigamax": False},
    {"nombre": "Charizard", "numero": 6, "tipos": ["Fuego", "Volador"], "debilidades": ["Agua", "Eléctrico", "Roca"], "tiene_mega_evolucion": True, "tiene_forma_gigamax": True},
    {"nombre": "Pikachu", "numero": 25, "tipos": ["Eléctrico"], "debilidades": ["Tierra"], "tiene_mega_evolucion": False, "tiene_forma_gigamax": True},
    {"nombre": "Gyarados", "numero": 130, "tipos": ["Agua", "Volador"], "debilidades": ["Eléctrico", "Roca"], "tiene_mega_evolucion": True, "tiene_forma_gigamax": False},
    {"nombre": "Eevee", "numero": 133, "tipos": ["Normal"], "debilidades": ["Lucha"], "tiene_mega_evolucion": False, "tiene_forma_gigamax": True},
    {"nombre": "Mewtwo", "numero": 150, "tipos": ["Psíquico"], "debilidades": ["Bicho", "Fantasma", "Siniestro"], "tiene_mega_evolucion": True, "tiene_forma_gigamax": False},
    {"nombre": "Lucario", "numero": 448, "tipos": ["Lucha", "Acero"], "debilidades": ["Fuego", "Lucha", "Tierra"], "tiene_mega_evolucion": True, "tiene_forma_gigamax": False},
    {"nombre": "Garchomp", "numero": 445, "tipos": ["Dragón", "Tierra"], "debilidades": ["Hielo", "Hada", "Dragón"], "tiene_mega_evolucion": True, "tiene_forma_gigamax": False},
    {"nombre": "Greninja", "numero": 658, "tipos": ["Agua", "Siniestro"], "debilidades": ["Eléctrico", "Planta", "Bicho", "Hada", "Lucha"], "tiene_mega_evolucion": False, "tiene_forma_gigamax": False},
    {"nombre": "Snorlax", "numero": 143, "tipos": ["Normal"], "debilidades": ["Lucha"], "tiene_mega_evolucion": False, "tiene_forma_gigamax": True},
    {"nombre": "Gardevoir", "numero": 282, "tipos": ["Psíquico", "Hada"], "debilidades": ["Veneno", "Acero", "Fantasma", "Siniestro"], "tiene_mega_evolucion": True, "tiene_forma_gigamax": False},
    {"nombre": "Tyranitar", "numero": 248, "tipos": ["Roca", "Siniestro"], "debilidades": ["Agua", "Planta", "Lucha", "Tierra", "Bicho", "Acero", "Hada"], "tiene_mega_evolucion": True, "tiene_forma_gigamax": False},
    {"nombre": "Blaziken", "numero": 257, "tipos": ["Fuego", "Lucha"], "debilidades": ["Agua", "Volador", "Psíquico", "Tierra"], "tiene_mega_evolucion": True, "tiene_forma_gigamax": False},
    {"nombre": "Sceptile", "numero": 254, "tipos": ["Planta"], "debilidades": ["Fuego", "Hielo", "Veneno", "Volador", "Bicho"], "tiene_mega_evolucion": True, "tiene_forma_gigamax": False},
    {"nombre": "Swampert", "numero": 260, "tipos": ["Agua", "Tierra"], "debilidades": ["Planta"], "tiene_mega_evolucion": True, "tiene_forma_gigamax": False},
    {"nombre": "Rayquaza", "numero": 384, "tipos": ["Dragón", "Volador"], "debilidades": ["Hielo", "Roca", "Dragón", "Hada"], "tiene_mega_evolucion": True, "tiene_forma_gigamax": False},
    {"nombre": "Gengar", "numero": 94, "tipos": ["Fantasma", "Veneno"], "debilidades": ["Fantasma", "Siniestro", "Psíquico", "Tierra"], "tiene_mega_evolucion": True, "tiene_forma_gigamax": True},
    {"nombre": "Machamp", "numero": 68, "tipos": ["Lucha"], "debilidades": ["Volador", "Psíquico", "Hada"], "tiene_mega_evolucion": False, "tiene_forma_gigamax": True},
    {"nombre": "Dragonite", "numero": 149, "tipos": ["Dragón", "Volador"], "debilidades": ["Hielo", "Roca", "Dragón", "Hada"], "tiene_mega_evolucion": False, "tiene_forma_gigamax": False},
    {"nombre": "Scizor", "numero": 212, "tipos": ["Bicho", "Acero"], "debilidades": ["Fuego"], "tiene_mega_evolucion": True, "tiene_forma_gigamax": False}
]

#los 3 arboles serian:
# 1. Arbol por nombre
# 2. Arbol por numero
# 3. Arbol por tipo

#creo los arboles
tree_by_name = BinaryTree
tree_by_number = BinaryTree
tree_by_type = BinaryTree


#Cargo los datos en los arboles

for pokemon in datos_pokemon:
    tree_by_name.insert(pokemon["nombre"], pokemon)
    tree_by_number.insert(pokemon["numero"], pokemon)
    for tipo in pokemon["tipos"]:
        tree_by_type.insert(tipo, pokemon)
print("Árbol cargado")

#mostrar todos los datos de un Pokémon a partir de su número y nombre

print("Buscar Pokémon por numero:")
numero_buscar = 25
pokemon_encontrado = tree_by_number.search(numero_buscar)
if pokemon_encontrado:
    print(pokemon_encontrado)
else:
    print("Pokémon no encontrado")  

print("Buscar Pokémon por nombre (búsqueda por proximidad):")
nombre_parcial = "char"
resultados_proximidad = tree_by_name.search_by_proximity(nombre_parcial)
for resultado in resultados_proximidad:
    print(resultado)        

#mostrar todos los nombres de los Pokémons de un determinado tipo: fantasma, fuego, acero y eléctrico;
tipos_a_buscar = ["Fantasma", "Fuego", "Acero", "Eléctrico"]
for tipo in tipos_a_buscar:
    print(f"Pokémons de tipo {tipo}:")
    pokemons_tipo = tree_by_type.search(tipo)
    for pokemon in pokemons_tipo:
        print(pokemon["nombre"])

#realizar un listado en orden ascendente por número y nombre de Pokémon, y además un listado por nivel por nombre;
print("Listado ascendente por número:")
listado_por_numero = tree_by_number.in_order_traversal()
for pokemon in listado_por_numero:
    print(pokemon)

print("Listado ascendente por nombre:")
listado_por_nombre = tree_by_name.in_order_traversal()
for pokemon in listado_por_nombre:
    print(pokemon)


#mostrar todos los Pokémons que son débiles frente a Jolteon, Lycanroc y Tyrantrum;
pokemons_a_consultar = ["Jolteon", "Lycanroc", "Tyrantrum"]
for nombre in pokemons_a_consultar:
    pokemon = tree_by_name.search(nombre)
    if pokemon:
        debilidades = pokemon["debilidades"]
        print(f"Pokémons débiles frente a {nombre}:")
        for debilidad in debilidades:
            pokemons_debiles = tree_by_type.search(debilidad)
            for p in pokemons_debiles:
                print(p["nombre"])
    else:
        print(f"Pokémon {nombre} no encontrado")    

#mostrar todos los tipos de Pokémons y cuántos hay de cada tipo;
tipos_contador = 0
for pokemon in datos_pokemon:
    for tipo in pokemon["tipos"]:
        if tipo in tipos_contador:
            tipos_contador[tipo] += 1
        else:
            tipos_contador[tipo] = 1
for tipo, contador in tipos_contador.items():
    print(f"Tipo: {tipo}, Cantidad: {contador}")

#determinar cuantos Pokémons tienen megaevolucion.
contador_mega_evolucion = 0 
for pokemon in datos_pokemon:
    if pokemon["tiene_mega_evolucion"]:
        contador_mega_evolucion += 1
print(f"Cantidad de Pokémons con megaevolución: {contador_mega_evolucion}")

#determinar cuantos Pokémons tiene forma gigamax.
contador_forma_gigamax = 0
for pokemon in datos_pokemon:
    if pokemon["tiene_forma_gigamax"]:
        contador_forma_gigamax += 1
print(f"Cantidad de Pokémons con forma Gigamax: {contador_forma_gigamax}")  

