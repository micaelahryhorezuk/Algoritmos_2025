from typing import Any, Optional # esto es para que no de error en el IDE, no es necesario en la terminal
from superheroes import superheroes # esto es para importar el módulo superheroes, que contiene la lista de superhéroes

class Queue:

    def __init__(self):                                  # constructor de la clase Queue
        self.__elements = []

    def arrive(self, value: Any) -> None:                # método para agregar un elemento a la cola
        self.__elements.append(value)

    def attention(self) -> Optional[Any]:                # método para eliminar el primer elemento de la cola y devolverlo
        return (
            self.__elements.pop(0)
            if self.__elements
            else None
        )

    def size(self) -> int:                               # método para obtener el tamaño de la cola
        return len(self.__elements)      
    
    def on_front(self) -> Optional[Any]:                 # método para obtener el primer elemento de la cola sin eliminarlo
        return (
            self.__elements[0]
            if self.__elements
            else None
        )

    def move_to_end(self) -> Optional[Any]:               # método para mover el primer elemento al final de la cola y devolverlo
        if self.__elements:
            value = self.attention() 
            self.arrive(value)
            return value
    
    def show(self): # método para mostrar los elementos de la cola
        for i in range(len(self.__elements)):
            print(self.move_to_end())

superheroes = Queue()                                    # creamos una instancia de la clase Queue
for personaje in superheroes:                            # recorremos la lista de superhéroes
    superheroes.arrive(personaje)                        # agregamos cada personaje a la cola

# a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
def nombre_LAsuperheroina(cola: Queue, nombre_heroe: str) -> None:  
    cola_aux = Queue()                                   #variable auxiliar para almacenar los personajes temporalmente
    encontrado = False 

    while cola.size() > 0:
        personaje = cola.attention()  #
        if personaje['nombre_heroe'] == nombre_heroe:
            print(f"El personaje de {nombre_heroe} es {personaje['nombre_real']}.")  #f hace formato de cadena
            encontrado = True
        cola_aux.arrive(personaje)                       #arriba el personaje a la cola auxiliar

    while cola_aux.size() > 0:
        cola.arrive(cola_aux.attention())  # devolvemos los personajes a la cola original

    if not encontrado:
        print(f"No se encontró a {nombre_heroe} en la cola.")

# b. Mostrar nombres de superhéroes femeninos
def mostrar_heroínas(cola: Queue) -> None: 
    cola_aux = Queue()  
    heroínas = [] 

    while cola.size() > 0:
        personaje = cola.attention()
        if personaje['genero'] == 'F':
            heroínas.append(personaje['nombre_heroe'])
        cola_aux.arrive(personaje)  

    while cola_aux.size() > 0:
        cola.arrive(cola_aux.attention())  

    if heroínas:
        print("Los nombres de superhéroes femeninos son:")
        for heroe in heroínas:
            print(heroe)
    else:
        print("No se encontraron superhéroes femeninos en la cola.")

# c. Mostrar nombres de personajes masculinos
def mostrar_heroes(cola: Queue) -> None:
    cola_aux = Queue()  
    heroes = []

    while cola.size() > 0:
        personaje = cola.attention()
        if personaje['genero'] == 'M':
            heroes.append(personaje['nombre_heroe'])
        cola_aux.arrive(personaje)  

    while cola_aux.size() > 0:
        cola.arrive(cola_aux.attention())  

    if heroes:
        print("Los nombres de superhéroes masculinos son:")
        for heroe in heroes:
            print(heroe)
    else:
        print("No se encontraron superhéroes masculinos en la cola.")

# d. Determinar el superhéroe de un personaje específico

def buscar_heroe_por_personaje(cola: Queue, nombre_personaje: str) -> None:
    cola_aux = Queue() 
    heroe = None

    while cola.size() > 0:
        personaje = cola.attention()
        if personaje['nombre_real'] == nombre_personaje:
            heroe = personaje['nombre_heroe']
            print(f"El superhéroe de {nombre_personaje} es {heroe}.")
        cola_aux.arrive(personaje) 

    while cola_aux.size() > 0:
        cola.arrive(cola_aux.attention())  

    if heroe is None:
        print(f"No se encontró al superhéroe de {nombre_personaje} en la cola.")

# e. Mostrar todos los datos de superhéroes o personajes que comienzan con S
def mostrar_nombres_con_S(cola: Queue) -> None:
    cola_aux = Queue()  
    encontrados = []

    while cola.size() > 0:
        personaje = cola.attention()
        if personaje['nombre_heroe'].startswith('S') or personaje['nombre_real'].startswith('S'): #startswith verifica si la cadena comienza con 'S'
            encontrados.append(personaje)
        cola_aux.arrive(personaje)  

    while cola_aux.size() > 0:
        cola.arrive(cola_aux.attention())  

    if encontrados:
        print("Los superhéroes o personajes que comienzan con 'S' son:")
        for p in encontrados:
            print(f"Nombre de héroe: {p['nombre_heroe']}, Nombre real: {p['nombre_real']}, Género: {p['genero']}")
    else:
        print("No se encontraron superhéroes o personajes que comiencen con 'S' en la cola.")

# f. Buscar si Carol Danvers está y mostrar su héroe
def buscar_carol_danvers(cola: Queue) -> None:
    cola_aux = Queue()  
    encontrado = False

    while cola.size() > 0:
        personaje = cola.attention()
        if personaje['nombre_real'] == 'Carol Danvers':
            print(f"El superhéroe de Carol Danvers es {personaje['nombre_heroe']}.")
            encontrado = True
        cola_aux.arrive(personaje)  

    while cola_aux.size() > 0:
        cola.arrive(cola_aux.attention())  

    if not encontrado:
        print("Carol Danvers no se encuentra en la cola.")

