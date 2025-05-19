#. Dada una pila con nombres de los personajes de la saga de Star Wars, implemente una función
#que permita determinar si Leia Organa o Boba Fett están en dicha pila sin perder los datos.

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
    
def buscar_personajes(pila):  # función que busca los personajes
    pila_aux = Pila()
    encontrados = []  # Lista para almacenar los personajes encontrados
    while not pila.esta_vacia(): #mientras la pila no esté vacía
        dato = pila.desapilar()  # saca el último elemento
        if dato == "Leia Organa" or dato == "Boba Fett":
            encontrados.append(dato)  # Agrega el personaje encontrado a la lista
        pila_aux.apilar(dato)  # apila en la pila auxiliar
    while not pila_aux.esta_vacia():
        pila.apilar(pila_aux.desapilar())
    return encontrados  # Devuelve la lista de personajes encontrados

#Programa principal para el 
pila_star_wars = Pila()

print("Ingresá nombres de personajes de Star Wars (escribí 'fin' para terminar):")
while True:
    nombre = input("Nombre del personaje: ")
    if nombre.lower() == "fin":
        break
    pila_star_wars.apilar(nombre)

resultados = buscar_personajes(pila_star_wars)

if resultados:  # Si la lista no está vacía
    print("Se encontraron en la pila:", ", ".join(resultados)) #el .join une los elementos de la lista en una cadena
else:
    print("No se encontró ni a Leia Organa ni a Boba Fett.")