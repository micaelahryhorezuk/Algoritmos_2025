# Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de su nombre y la cantidad de películas de la saga en la que 
#     participó, implementar las funciones necesarias para resolver las siguientes actividades:
#     a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posición uno la cima de la pila;
#     b. determinar los personajes que participaron en más de 5 películas de la saga, además indicar la cantidad de películas en la que aparece;
#     c. determinar en cuantas películas participo la Viuda Negra (Black Widow);
#     d. mostrar todos los personajes cuyos nombre empiezan con C, D y G.

class Pila:
    def __init__(self):
        self.items = []

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        return None

    def esta_vacia(self):
        return len(self.items) == 0

    def ver_items(self):
        return self.items


class Personaje:
    def __init__(self, nombre, cantidad_peliculas):
        self.nombre = nombre
        self.cantidad_peliculas = cantidad_peliculas

    def __str__(self):
        return f"{self.nombre} (Películas: {self.cantidad_peliculas})"


# Función para cargar personajes
def cargar_personajes(pila):
    cantidad = int(input("¿Cuántos personajes desea cargar? "))
    for _ in range(cantidad):
        nombre = input("Nombre del personaje: ")
        cantidad_peliculas = int(input(f"Cantidad de películas de {nombre}: "))
        personaje = Personaje(nombre, cantidad_peliculas)
        pila.apilar(personaje)
        print("Personaje agregado.")


# a. Posición de Rocket Raccoon y Groot desde la cima (1-indexado)
def posicion_rocket_groot(pila):
    print("\na. Posición de Rocket Raccoon y Groot desde la cima:")
    nombres_buscar = ["Rocket Raccoon", "Groot"]
    items = pila.ver_items()[::-1]  # invertir para contar desde la cima
    for nombre in nombres_buscar:
        for i, p in enumerate(items, 1):
            if p.nombre == nombre:
                print(f"{nombre} está en la posición {i}")
                break
        else:
            print(f"{nombre} no está en la pila.")


# b. Personajes en más de 5 películas
def personajes_mas_de_cinco(pila):
    print("Personajes que participaron en más de 5 películas:")
    for p in pila.ver_items():
        if p.cantidad_peliculas > 5:
            print(f"- {p.nombre}: {p.cantidad_peliculas} películas")


# c. Cantidad de películas de Black Widow
def peliculas_black_widow(pila):
    print("Películas en las que participó Black Widow:")
    for p in pila.ver_items():
        if p.nombre.lower() == "black widow":
            print(f"Participó en {p.cantidad_peliculas} películas")
            return
    print("Black Widow no está en la pila.")


# d. Personajes cuyo nombre comienza con C, D o G
def personajes_letras_especificas(pila):
    print("Personajes cuyo nombre comienza con C, D o G:")
    for p in pila.ver_items():
        if p.nombre[0].upper() in {"C", "D", "G"}:
            print("-", p)


# Menú para probar todo
def menu():
    pila = Pila()

    while True:
        print("\nMenú:")
        print("1. Cargar personajes")
        print("2. Posición de Rocket Raccoon y Groot")
        print("3. Personajes con más de 5 películas")
        print("4. Películas de Black Widow")
        print("5. Personajes que empiezan con C, D o G")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            cargar_personajes(pila)
        elif opcion == "2":
            posicion_rocket_groot(pila)
        elif opcion == "3":
            personajes_mas_de_cinco(pila)
        elif opcion == "4":
            peliculas_black_widow(pila)
        elif opcion == "5":
            personajes_letras_especificas(pila)
        elif opcion == "0":
            break
        else:
            print("Opción no válida.")


# Ejecutar
if __name__ == "__main__":
    menu()
