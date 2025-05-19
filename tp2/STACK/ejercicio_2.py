#Eliminar de una pila todos los elementos impares, es decir que en la misma solo queden números pares.


class Pila:
    def __init__(self): #Inicializa la pila vacía
        self.items = []

    def apilar(self, item): 
        self.items.append(item) #agrega un elemento a la pila

    def desapilar(self): 
        if not self.esta_vacia(): 
            return self.items.pop() #elimina y devuelve el elemento en la cima de la pila
        return None

    def esta_vacia(self):
        return len(self.items) == 0 

    def ver_items(self): #devuelve todos los elementos de la pila
        return self.items

def eliminar_impares(pila):
    pila_aux = Pila()
    while not pila.esta_vacia():
        dato = pila.desapilar() #saca el último elemento
        if dato % 2 == 0:
            pila_aux.apilar(dato) #si el número es par lo apila en la pila auxiliar
    while not pila_aux.esta_vacia():
        pila.apilar(pila_aux.desapilar())

mi_pila = Pila()
print("Ingresá números a la pila (escribí 'fin' para terminar):")
while True:
    entrada = input("Numero: ")
    if entrada.lower() == "fin":
        break
    try:
        numero = int(entrada)
        mi_pila.apilar(numero)
    except ValueError:
        print("Por favor, ingresá solo números o 'fin'.")

# ---- Eliminar impares ----
eliminar_impares(mi_pila)

print("Pila final (solo números pares):", mi_pila.ver_items())

