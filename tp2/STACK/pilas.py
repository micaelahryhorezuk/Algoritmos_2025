#Pilas

pila = [1,2,3]

#Agrega elementos a la pila (el último elemento agregado es el primero en salir)
pila.append(4)
pila.append(5)

print(pila)
#Sacar elementos de la pila (el último elemento agregado es el primero en salir)
#Solo quita el ultimo elemento pero no te dice cual es 
#pila.pop ()

#Tambien se puede mostrar el elemento que quitamos
n = pila.pop()
print(f"Elemento que se quito es : {n}")
