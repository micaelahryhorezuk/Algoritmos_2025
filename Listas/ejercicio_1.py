#Diseñar un algoritmo que permita contar la cantidad de nodos de una lista.

from typing import Any, Optional # Importamos Any y Optional para tipos de datos
from clase_lista import List  # Importamos la clase List desde el archivo clase_lista.py

lista = List() 
lista.extend([10, 20, 30, 40, 4, 2, 1])  # Agregamos algunos elementos a la lista

print("Cantidad de nodos:", lista.count_nodes())  

print("Elementos de la lista:", lista)  # Mostramos los elementos de la lista
