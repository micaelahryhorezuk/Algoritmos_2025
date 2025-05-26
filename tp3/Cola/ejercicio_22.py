# Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), de los cuales se 
# conoce el nombre del personaje, el nombre del superhéroe y su género (Masculino M y Femenino

# F) –por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, {Natasha Ro-
# manoff, Black Widow, F}, etc., desarrollar un algoritmo que resuelva las siguientes actividades:

# a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
# b. mostrar los nombre de los superhéroes femeninos;
# c. mostrar los nombres de los personajes masculinos;
# d. determinar el nombre del superhéroe del personaje Scott Lang;
# e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan
# con la letra S;
# f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre
# de superhéroes.


class Personaje:
    def __init__(self, nombre_real, nombre_heroe, genero):
        self.nombre_real = nombre_real
        self.nombre_heroe = nombre_heroe
        self.genero = genero

    def __str__(self):
        return f"{self.nombre_real} - {self.nombre_heroe} - {self.genero}"


class Cola:
    def __init__(self):
        self.items = []

    def encolar(self, item):
        self.items.append(item)

    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop(0)

    def esta_vacia(self):
        return len(self.items) == 0

    def tamano(self):
        return len(self.items)

    def ver_primero(self):
        if not self.esta_vacia():
            return self.items[0]



# a. Determinar el nombre del personaje de la superhéroe Capitana Marvel


def buscar_personaje_por_heroe(cola_original, nombre_heroe_objetivo):
    cola_aux = Cola()
    nombre_encontrado = None

    while not cola_original.esta_vacia():
        personaje = cola_original.desencolar()
        if personaje.nombre_heroe == nombre_heroe_objetivo:
            nombre_encontrado = personaje.nombre_real
        cola_aux.encolar(personaje)

    while not cola_aux.esta_vacia():
        cola_original.encolar(cola_aux.desencolar())

    if nombre_encontrado:
        print(f"El personaje de {nombre_heroe_objetivo} es {nombre_encontrado}.")
    else:
        print(f"No se encontró a {nombre_heroe_objetivo} en la cola.")


# b. Mostrar nombres de superhéroes femeninos


def mostrar_heroínas(cola_original):
    cola_aux = Cola()
    print("Superhéroes femeninos:")
    while not cola_original.esta_vacia():
        personaje = cola_original.desencolar()
        if personaje.genero == "F":
            print(personaje.nombre_heroe)
        cola_aux.encolar(personaje)
    while not cola_aux.esta_vacia():
        cola_original.encolar(cola_aux.desencolar())



# c. Mostrar nombres de personajes masculinos


def mostrar_personajes_masculinos(cola_original):
    cola_aux = Cola()
    print("Personajes masculinos:")
    while not cola_original.esta_vacia():
        personaje = cola_original.desencolar()
        if personaje.genero == "M":
            print(personaje.nombre_real)
        cola_aux.encolar(personaje)
    while not cola_aux.esta_vacia():
        cola_original.encolar(cola_aux.desencolar())


# d. Determinar el superhéroe de un personaje específico


def buscar_heroe_por_personaje(cola_original, nombre_personaje):
    cola_aux = Cola()
    heroe = None
    while not cola_original.esta_vacia():
        personaje = cola_original.desencolar()
        if personaje.nombre_real == nombre_personaje:
            heroe = personaje.nombre_heroe
        cola_aux.encolar(personaje)
    while not cola_aux.esta_vacia():
        cola_original.encolar(cola_aux.desencolar())

    if heroe:
        print(f"El superhéroe de {nombre_personaje} es {heroe}.")
    else:
        print(f"{nombre_personaje} no se encuentra en la cola.")



# e. Mostrar todos los datos de superhéroes o personajes que comienzan con S


def mostrar_nombres_con_S(cola_original):
    cola_aux = Cola()
    print("Personajes o superhéroes que comienzan con 'S':")
    while not cola_original.esta_vacia():
        personaje = cola_original.desencolar()
        if personaje.nombre_real.startswith("S") or personaje.nombre_heroe.startswith("S"):
            print(personaje)
        cola_aux.encolar(personaje)
    while not cola_aux.esta_vacia():
        cola_original.encolar(cola_aux.desencolar())


# f. Buscar si Carol Danvers está y mostrar su héroe


def verificar_carol_danvers(cola_original):
    cola_aux = Cola()
    encontrado = False
    nombre_heroe = ""
    while not cola_original.esta_vacia():
        personaje = cola_original.desencolar()
        if personaje.nombre_real == "Carol Danvers":
            encontrado = True
            nombre_heroe = personaje.nombre_heroe
        cola_aux.encolar(personaje)
    while not cola_aux.esta_vacia():
        cola_original.encolar(cola_aux.desencolar())

    if encontrado:
        print(f"Carol Danvers está en la cola. Su superhéroe es {nombre_heroe}.")
    else:
        print("Carol Danvers no se encuentra en la cola.")



# Cargar personajes MCU


cola_mcu = Cola()
cola_mcu.encolar(Personaje("Tony Stark", "Iron Man", "M"))
cola_mcu.encolar(Personaje("Steve Rogers", "Capitán América", "M"))
cola_mcu.encolar(Personaje("Natasha Romanoff", "Black Widow", "F"))
cola_mcu.encolar(Personaje("Carol Danvers", "Capitana Marvel", "F"))
cola_mcu.encolar(Personaje("Scott Lang", "Ant-Man", "M"))
cola_mcu.encolar(Personaje("Stephen Strange", "Doctor Strange", "M"))
cola_mcu.encolar(Personaje("Shuri", "Black Panther (Shuri)", "F"))


buscar_personaje_por_heroe(cola_mcu, "Capitana Marvel")
print()

mostrar_heroínas(cola_mcu)
print()

mostrar_personajes_masculinos(cola_mcu)
print()

buscar_heroe_por_personaje(cola_mcu, "Scott Lang")
print()

mostrar_nombres_con_S(cola_mcu)
print()

verificar_carol_danvers(cola_mcu)
