from typing import Any, Optional # esto es para que no de error en el IDE, no es necesario en la terminal
from superheroes import lista_superheroes # esto es para importar el módulo superheroes, que contiene la lista de superhéroes

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

cola_superheroes = Queue()                                    # creamos una instancia de la clase Queue
for personaje in lista_superheroes:                            # recorremos la lista de superhéroes
    cola_superheroes.arrive(personaje)                        # agregamos cada personaje a la cola

# a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
def nombre_LAsuperheroina(cola: Queue,name: str) -> None:  
    cola_aux = Queue()                                   #variable auxiliar para almacenar los personajes temporalmente
    encontrado = False 

    while cola.size() > 0:
        personaje = cola.attention()  #
        if personaje['name'] == name:
            print(f"El personaje de {name} es {personaje['real_name']}.")  #f hace formato de cadena
            encontrado = True
        cola_aux.arrive(personaje)                       #arriba el personaje a la cola auxiliar

    while cola_aux.size() > 0:
        cola.arrive(cola_aux.attention())  # devolvemos los personajes a la cola original

    if not encontrado:
        print(f"No se encontró a {name} en la cola.")

# b. Mostrar nombres de superhéroes femeninos
def mostrar_heroínas(cola: Queue) -> None: 
    cola_aux = Queue()  
    heroínas = [] 

    while cola.size() > 0:
        personaje = cola.attention()
        if personaje['genero'] == 'F':
            heroínas.append(personaje['name'])
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
            heroes.append(personaje['name'])
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
        if personaje['real_name'] == nombre_personaje:
            heroe = personaje['name']
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
        if personaje['name'].startswith('S') or personaje['real_name'].startswith('S'): #startswith verifica si la cadena comienza con 'S'
            encontrados.append(personaje)
        cola_aux.arrive(personaje)  

    while cola_aux.size() > 0:
        cola.arrive(cola_aux.attention())  

    if encontrados:
        print("Los superhéroes o personajes que comienzan con 'S' son:")
        for p in encontrados:
            print(f"Nombre de héroe: {p['name']}, Nombre real: {p['real_name']}, Género: {p['genero']}")
    else:
        print("No se encontraron superhéroes o personajes que comiencen con 'S' en la cola.")

# f. Buscar si Carol Danvers está y mostrar su héroe
def buscar_carol_danvers(cola: Queue) -> None:
    cola_aux = Queue()  
    encontrado = False

    while cola.size() > 0:
        personaje = cola.attention()
        if personaje['real_name'] == 'Carol Danvers':
            print(f"El superhéroe de Carol Danvers es {personaje['name']}.")
            encontrado = True
        cola_aux.arrive(personaje)  

    while cola_aux.size() > 0:
        cola.arrive(cola_aux.attention())  

    if not encontrado:
        print("Carol Danvers no se encuentra en la cola.")

nombre_LAsuperheroina(cola_superheroes, "Captain Marvel")
mostrar_heroínas(cola_superheroes)
mostrar_heroes(cola_superheroes)
buscar_heroe_por_personaje(cola_superheroes, "Bruce Banner")
mostrar_nombres_con_S(cola_superheroes)
buscar_carol_danvers(cola_superheroes)