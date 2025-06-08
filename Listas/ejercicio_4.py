#Implementar un algoritmo que inserte un nodo en la i-ésima posición de una lista.
from typing import Any, Optional
from clase_lista import List

lista = List()
lista.extend([10, 20, 30, 40, 50])  # Agregamos algunos elementos a la lista

def insertar_nodo(lista: List, valor: Any, posicion: int) -> None:
    if posicion < 0 or posicion > len(lista): # Verificamos si la posición es válida
        print("Posición inválida")
        return
    lista.insert(posicion, valor) #  Insertamos el valor en la posición indicada

valor = input("Ingrese el valor a insertar: ")  # Solicitamos el valor al usuario
posicion = int(input("Ingrese la posición donde insertar el valor: "))  # Solicitamos la posición al usuario
insertar_nodo(lista, valor, posicion)  # Llamamos a la función para insertar el nodo

print("Lista original:", lista)  # Mostramos la lista original
print("lista con el nuevo nodo:", lista)  # Mostramos la lista con el nuevo nodo insertado
