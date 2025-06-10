#Dado una lista simple de python (array) de 15 superheroes realizar dos funciones recursivas:
#a.funcion recursiva  para buscar, determinar si Capitan America esta en la lista.
#b. funcion recursiva para listar los superheroes de la lista.

from Lista_Superheroes import superheroes

# a. Función recursiva para buscar si Capitan America está en la lista

superheroes.sort()  # Ordenar la lista de superhéroes alfabéticamente
#busqueda binaria 
def bus_bin_rec(array, value, first, last): 
    if first > last:
        return -1
    middle = (first + last) // 2
    if array[middle] == value:
        return middle
    elif array[middle] > value:
        return bus_bin_rec(array, value, first, middle - 1)
    else:
        return bus_bin_rec(array, value, middle + 1, last)

value = "Capitán América"
if bus_bin_rec(superheroes, value, 0, len(superheroes) - 1) != -1:
    print(value, "está en la lista de superhéroes.", "\n")
else:
    print(value, "no está en la lista de superhéroes.")

# b. Función recursiva para listar los superhéroes de la lista
def listar_superheroes(array, index=0):
    if index < len(array):
        print(array[index])
        listar_superheroes(array, index + 1)
print("Lista de superhéroes:", superheroes)

