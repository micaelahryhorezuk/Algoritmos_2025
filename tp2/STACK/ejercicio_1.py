#1. Determinar el número de ocurrencias de un determinado elemento en una pila.
#cuántas veces aparece un determinado elemento dentro de la pila.

class Pila:
    def __init__(self):  # Inicializa la pila vacía
        self.items = []  

    def apilar(self, item):  # Agrega un elemento a la pila
        self.items.append(item) 

    def desapilar(self):  # Elimina y devuelve el elemento en la cima de la pila
        if not self.esta_vacia(): 
            return self.items.pop() 
        else:
            return None

    def esta_vacia(self):  # Verifica si la pila está vacía
        return len(self.items) == 0

    def contar_ocurrencias(self, elemento):  # Cuenta cuántas veces aparece un elemento en la pila
        contador = 0
        for item in self.items: 
            if item == elemento:
                contador += 1
        return contador


mi_pila = Pila()  # Crear una instancia de la clase Pila

print("Ingresá elementos a la pila (escribí 'fin' para terminar):")
while True:
    entrada = input("Elemento: ") 
    if entrada.lower() == "fin":
        break
    mi_pila.apilar(entrada)

buscar = input("¿Qué elemento querés buscar?: ")
ocurrencias = mi_pila.contar_ocurrencias(buscar) #guarda el elemento que buscamos
print(f"El elemento '{buscar}' aparece {ocurrencias} veces en la pila.")
