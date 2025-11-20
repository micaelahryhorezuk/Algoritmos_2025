#1. Generar un grafo con 15 vértices aleatorios no repetidos (con números de 1 a 100), luego agregar
#30 aristas –no repetidas– que conecten vértices de manera aleatoria, con etiquetas –también
#aleatorias– dentro del rango de 1 a 100, después resolver las siguientes actividades:
#a. primero eliminar los vértices que hayan quedado desconectados, es decir, que ningún otro
#vértice tenga una arista que lo apunte y que de él no salga ninguna arista;
#b. determinar el nodo con mayor cantidad de aristas que salen de él, puede ser más de uno;
#c. determinar el nodo con mayor cantidad de aristas que llegan a él, puede ser más de uno;
#d. indicar los vértices desde los cuales no se puede acceder a otro vértice;

#e. contar cuantos vértice componen el grafo, dado que se genera aleatoriamente y se elimi-
#nan los vértices que quedan desconectados;

#f. determinar cuántos vértices tienen un arista a sí mismo, es decir, un ciclo directo;
#g. determinar la arista más larga, indicando su origen, destino y valor –puede ser más de una.


import random
from graph import Graph

#generar un grafo aleatorio con las características solicitadas

def generar_grafo_aleatorio():
    g = Graph(is_directed=True)   # tu clase usa True = NO dirigido

    # 15 vértices aleatorios no repetidos
    vertices = random.sample(range(1, 101), 15)

    for v in vertices:
        g.insert_vertex(v, other_values={})

    # 30 aristas aleatorias no repetidas
    aristas_creadas = set()

    while len(aristas_creadas) < 30:
        origen = random.choice(vertices)
        destino = random.choice(vertices)
        peso = random.randint(1, 100)

        # Evitar aristas duplicadas exactas
        if (origen, destino) not in aristas_creadas:
            g.insert_edge(origen, destino, peso)
            aristas_creadas.add((origen, destino))

    return g

#a. Eliminar vértices desconectados

def eliminar_vertices_desconectados(g: Graph):
    desconectados = []

    for i in range(len(g)):
        vert = g[i]
        valor = vert.value

        # no salen aristas
        sin_salientes = len(vert.adjacents) == 0

        # no llegan aristas
        sin_entrantes = True
        for j in range(len(g)):
            otro = g[j]
            for ar in otro.adjacents:
                if ar.destination.value == valor:
                    sin_entrantes = False
                    break

        if sin_salientes and sin_entrantes:
            desconectados.append(valor)

    # eliminar después para no romper índices
    for v in desconectados:
        g.delete_vertex(v)

    return desconectados
#b. nodo con más aristas salientes

def nodos_mas_aristas_salientes(g: Graph):
    max_grado = -1
    resultado = []

    for i in range(len(g)):
        vert = g[i]
        grado = len(vert.adjacents)

        if grado > max_grado:
            max_grado = grado
            resultado = [vert.value]
        elif grado == max_grado:
            resultado.append(vert.value)

    return resultado, max_grado

#c. nodo con más aristas entrantes

def nodos_mas_aristas_entrantes(g: Graph):
    conteo = {g[i].value: 0 for i in range(len(g))}

    for i in range(len(g)):
        vert = g[i]
        for ar in vert.adjacents:
            destino = ar.destination.value
            conteo[destino] += 1

    max_ent = max(conteo.values())
    resultado = [n for n, c in conteo.items() if c == max_ent]

    return resultado, max_ent

#d. vértices sin salida
def vertices_sin_salida(g: Graph):
    resultado = []

    for i in range(len(g)):
        vert = g[i]
        if len(vert.adjacents) == 0:
            resultado.append(vert.value)

    return resultado

#e. contar vértices

def contar_vertices(g: Graph):
    return len(g)

#f. vértices con ciclo directo

def vertices_ciclo_directo(g: Graph):
    ciclos = []

    for i in range(len(g)):
        vert = g[i]
        for ar in vert.adjacents:
            if ar.destination.value == vert.value:
                ciclos.append(vert.value)

    return ciclos

#g. aristas más largas

def aristas_mas_largas(g: Graph):
    max_peso = -1
    resultado = []

    for i in range(len(g)):
        vert = g[i]
        for ar in vert.adjacents:
            if ar.weight > max_peso:
                max_peso = ar.weight
                resultado = [(vert.value, ar.destination.value, ar.weight)]
            elif ar.weight == max_peso:
                resultado.append((vert.value, ar.destination.value, ar.weight))

    return resultado, max_peso

# Ejecutar el código

if __name__ == "__main__":
    g = generar_grafo_aleatorio()

    print("\n=== A. Eliminando vértices desconectados ===")
    eliminados = eliminar_vertices_desconectados(g)
    print("Vértices eliminados:", eliminados)

    print("\n=== B. Nodos con más salientes ===")
    nodos_sal, grado_sal = nodos_mas_aristas_salientes(g)
    print("Nodos:", nodos_sal, " | Cantidad:", grado_sal)

    print("\n=== C. Nodos con más entrantes ===")
    nodos_ent, grado_ent = nodos_mas_aristas_entrantes(g)
    print("Nodos:", nodos_ent, " | Cantidad:", grado_ent)

    print("\n=== D. Vértices sin salida ===")
    print(vertices_sin_salida(g))

    print("\n=== E. Cantidad total de vértices ===")
    print(contar_vertices(g))

    print("\n=== F. Ciclos directos ===")
    print(vertices_ciclo_directo(g))

    print("\n=== G. Aristas más largas ===")
    print(aristas_mas_largas(g))
