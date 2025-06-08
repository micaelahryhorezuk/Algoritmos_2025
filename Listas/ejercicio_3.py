#Dada una lista de números enteros, implementar un algoritmo para dividir dicha lista en dos,
#una que contenga los números pares y otra para los números impares.
from typing import Any, Optional
from clase_lista import List

lista_numeros = List()
lista_numeros.extend([10, 21, 32, 43, 54, 65, 76, 87, 98])

def divide_lista(lista: List) -> tuple[List, List]: # Función para dividir una lista en pares e impares
    lista_pares = List()
    lista_impares = List()

    for numero in lista:
        if numero % 2 == 0:
            lista_pares.append(numero) 
        else:
            lista_impares.append(numero)

    return lista_pares, lista_impares

pares, impares = divide_lista(lista_numeros)  # Llamamos a la función para dividir la lista

print("Lista de números:", lista_numeros)  # Mostramos la lista original
print("Lista de números pares:", pares)  # Mostramos la lista de números pares
print("Lista de números impares:", impares)  # Mostramos la lista de números impares