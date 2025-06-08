# Diseñar un algoritmo que elimine todas las vocales que se encuentren en una lista de caracteres.

from typing import Any, Optional  

from clase_lista import List  

lista = List()
lista.extend(['a', 'b', 'c', 'e', 'i', 'o', 'u'])

print("Lista original:", lista)  

vocales = ['a', 'e', 'i', 'o', 'u']
for vocal in vocales:
    lista.delete_value(vocal)

print("Lista sin vocales:", lista)  
print(lista)

