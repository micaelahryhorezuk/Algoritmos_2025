##Ejercicio 2: Dado un grafo no dirigido con personajes de la saga Star Wars, implementar los algoritmos necesarios para resolver las siguientes tareas:
#cada vértice debe almacenar el nombre de un personaje, las aristas representan la cantidad de episodios en los que aparecieron juntos ambos personajes que se relacionan;
#hallar el árbol de expansión mínimo desde el vértice que contiene a: C-3PO, Yoda y Leia;
#determinar cuál es el número máximo de episodio que comparten dos personajes, e indicar todos los pares de personajes que coinciden con dicho número;
#cargue al menos los siguientes personajes: Luke Skywalker, Darth Vader, Yoda, Boba Fett, C-3PO, Leia, Rey, Kylo Ren, Chewbacca, Han Solo, R2-D2, BB-8;
#calcule el camino mas ccorto desde: C-3PO a R2-D2 y desde Yoda a Darth Vader;
#indicar qué personajes aparecieron en los nueve episodios de la saga.

import math
from graph import Graph
from typing import Dict, Any

def mostrar_camino_minimo(grafo: Graph, inicio: str, fin: str):
    """
    Calcula y muestra el camino mas corto entre dos nodos usando Dijkstra
    """
    print(f"\nCalculando camino mas corto: {inicio} -> {fin}")
    
    # Obtener resultados del algoritmo de Dijkstra
    pila_ruta = grafo.dijkstra(inicio)
    
    # Reconstruir el camino desde el destino hasta el origen
    ruta_final = []
    costo_acumulado = None
    nodo_actual = fin

    # Reconstruccion inversa del camino
    while pila_ruta.tamano() > 0:
        elemento = pila_ruta.pop()
        
        if elemento[0] == nodo_actual:
            if costo_acumulado is None:
                costo_acumulado = elemento[1]
            
            ruta_final.append(elemento[0])
            nodo_actual = elemento[2]

    # Invertir para mostrar en orden correcto
    ruta_final.reverse()

    # Mostrar resultados
    if costo_acumulado is not None:
        print(f"Camino encontrado: {' -> '.join(ruta_final)}")
        print(f"Costo total: {costo_acumulado}")
    else:
        print(f"No se encontro un camino de {inicio} a {fin}")


# Implementacion del grafo no dirigido con personajes de Star Wars

print("Inicializando grafo de personajes Star Wars")

# Crear grafo no dirigido para relaciones bidireccionales
grafo_personajes = Graph(es_dirigido=False)

# Datos de personajes
lista_personajes = [
    ("Luke Skywalker", False),
    ("Darth Vader", False),
    ("Yoda", False),
    ("Boba Fett", False),
    ("C-3PO", True),
    ("Princesa Leia", False),
    ("Rey", False),
    ("Kylo Ren", False),
    ("Chewbacca", False),
    ("Han Solo", False),
    ("R2-D2", True),
    ("BB-8", False)
]

# Insertar personajes como vertices en el grafo
for nombre_personaje, en_nueve_episodios in lista_personajes:
    grafo_personajes.insertar_vertice(nombre_personaje, {"en_nueve": en_nueve_episodios})
    print(f"Nodo agregado: {nombre_personaje}")

# Conexiones entre personajes
print("\nEstableciendo conexiones entre personajes")

conexiones = [
    # Conexiones de Luke Skywalker
    ("Luke Skywalker", "Darth Vader", 4),
    ("Luke Skywalker", "Princesa Leia", 6),
    ("Luke Skywalker", "Han Solo", 4),
    ("Luke Skywalker", "Chewbacca", 6),
    ("Luke Skywalker", "C-3PO", 6),
    ("Luke Skywalker", "R2-D2", 6),
    ("Luke Skywalker", "Yoda", 4),
    
    # Conexiones de Darth Vader
    ("Darth Vader", "Boba Fett", 2),
    ("Darth Vader", "C-3PO", 4),
    ("Darth Vader", "Yoda", 3),
    
    # Conexiones de Han Solo
    ("Han Solo", "Chewbacca", 5),
    ("Han Solo", "Princesa Leia", 5),
    ("Han Solo", "C-3PO", 5),
    
    # Conexiones de Leia
    ("Princesa Leia", "C-3PO", 7),
    ("Princesa Leia", "R2-D2", 7),
    
    # Conexiones de droides
    ("C-3PO", "R2-D2", 9),
    ("C-3PO", "BB-8", 3),
    
    # Conexiones nueva trilogia
    ("Rey", "Kylo Ren", 3),
    ("Rey", "BB-8", 3),
    ("Rey", "Han Solo", 2),
    ("Rey", "Chewbacca", 3),
    
    # Conexiones secundarias
    ("Boba Fett", "Han Solo", 2)
]

# Insertar todas las conexiones como aristas
for origen, destino, peso in conexiones:
    grafo_personajes.insertar_arista(origen, destino, peso)
    print(f"Conexion agregada: {origen} <-> {destino} (Episodios: {peso})")

# Analisis del grafo

# 1. Arbol de expansion minima
print("\nCalculando Arbol de Expansion Minima con Kruskal")

arbol_minimo = grafo_personajes.kruskal('C-3PO')

if arbol_minimo:
    costo_total_arbol = 0
    conexiones_arbol = arbol_minimo.split(';')
    
    print("Conexiones del Arbol de Expansion Minima:")
    
    for conexion in conexiones_arbol:
        partes = conexion.split('-')
        if len(partes) == 3:
            nodo_a, nodo_b, costo_str = partes
            costo = int(costo_str)
            costo_total_arbol += costo
            print(f"  {nodo_a} <-> {nodo_b} (Costo: {costo})")
            
    print(f"Costo total del MST: {costo_total_arbol}")
else:
    print("No se pudo generar el arbol de expansion")

# 2. Pares con maximas coincidencias
print("\nBuscando pares con maximo de episodios compartidos")

max_episodios_compartidos = -1
pares_maximos = []
pares_procesados = set()

for vertice in grafo_personajes:
    for arista in vertice.aristas:
        par_ordenado = tuple(sorted((vertice.valor, arista.valor)))
        
        if par_ordenado not in pares_procesados:
            if arista.peso > max_episodios_compartidos:
                max_episodios_compartidos = arista.peso
                pares_maximos = [par_ordenado]
            elif arista.peso == max_episodios_compartidos:
                pares_maximos.append(par_ordenado)
            
            pares_procesados.add(par_ordenado)

if max_episodios_compartidos != -1:
    print(f"Maximo de episodios compartidos: {max_episodios_compartidos}")
    print("Pares con este maximo:")
    for personaje_a, personaje_b in pares_maximos:
        print(f"  {personaje_a} y {personaje_b}")
else:
    print("No se encontraron conexiones en el grafo")

# 3. Calculo de rutas minimas
mostrar_camino_minimo(grafo_personajes, 'C-3PO', 'R2-D2')
mostrar_camino_minimo(grafo_personajes, 'Yoda', 'Darth Vader')

# 4. Personajes en los 9 episodios
print("\nPersonajes que aparecieron en los 9 episodios")

personajes_en_nueve = []
for vertice in grafo_personajes:
    if (vertice.otros_valores and 
        vertice.otros_valores.get("en_nueve") is True):
        personajes_en_nueve.append(vertice.valor)

if personajes_en_nueve:
    print("Personajes en todos los episodios:")
    for personaje in personajes_en_nueve:
        print(f"  {personaje}")
else:
    print("No hay personajes en todos los episodios")

print("\nAnalisis completado")