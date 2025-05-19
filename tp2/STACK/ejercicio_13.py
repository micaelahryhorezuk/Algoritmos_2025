
#Dada una pila con los trajes de Iron Man utilizados en las películas de Marvel Cinematic Uni-
# verse (MCU) de los cuales se conoce el nombre del modelo, nombre de la película en la que se

# usó y el estado en que quedó al final de la película (Dañado, Impecable, Destruido), resolver
# las siguientes actividades:

#A. determinar si el modelo Mark XLIV (Hulkbuster) fue utilizado en alguna de las películas,
#además mostrar el nombre de dichas películas;

#B. mostrar los modelos que quedaron dañados, sin perder información de la pila.

#C. eliminar los modelos de los trajes destruidos mostrando su nombre;

# D. un modelo de traje puede usarse en más de una película y en una película se pueden usar
# más de un modelo de traje, estos deben cargarse por separado;

# E. agregar el modelo Mark LXXXV a la pila, tener en cuenta que no se pueden cargar modelos
# repetidos en una misma película;

# F. mostrar los nombre de los trajes utilizados en las películas “Spider-Man: Homecoming” y
# “Capitan America: Civil War”.

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

class Traje:
    def __init__(self, modelo, pelicula, estado):
        self.modelo = modelo
        self.pelicula = pelicula
        self.estado = estado

    def __str__(self):
        return f"{self.modelo} (Película: {self.pelicula}, Estado: {self.estado})"


# Función para cargar trajes por el usuario
def cargar_trajes(pila):
    cantidad = int(input("¿Cuántos trajes desea cargar? "))
    for _ in range(cantidad): # para cada traje (cantidad que el usario ingresó) 
        modelo = input("Ingrese el modelo del traje: ")
        pelicula = input("Ingrese la película donde se usó el traje: ")
        estado = input("Ingrese el estado del traje (Dañado, Impecable, Destruido): ")

        # Verifica que no se repita el modelo en la misma película
        duplicado = any(t.modelo == modelo and t.pelicula == pelicula for t in pila.ver_items()) 
        if duplicado:
            print("Ese modelo ya está cargado para esa película. No se agregará.")
        else:
            traje = Traje(modelo, pelicula, estado)
            pila.apilar(traje)
            print("Traje agregado")  

# A. Buscar modelo Mark XLIV (Hulkbuster)
def buscar_mark_xliv(pila):
    peliculas = [t.pelicula for t in pila.ver_items() if t.modelo == "Mark XLIV"]
    if peliculas:
        print("Mark XLIV fue usado en las siguientes películas:")
        for p in set(peliculas):
            print("-", p)
    else:
        print("Mark XLIV no fue usado en ninguna película.")

# B. Mostrar los modelos dañados sin perder la pila
def mostrar_dañados(pila):
    print("Modelos dañados: " )
    for t in pila.ver_items():
        if t.estado == "Dañado":
            print("-", t)

# C. Eliminar modelos destruidos y mostrar su nombre
def eliminar_destruidos(pila):
    print(" Modelos destruidos eliminados:")
    nuevos_items = []
    for t in pila.ver_items():
        if t.estado == "Destruido":
            print("-", t.modelo)
        else:
            nuevos_items.append(t)
    pila.items = nuevos_items

# E. Agregar Mark LXXXV sin duplicados en la misma película
def agregar_mark_lxxxv(pila):
    pelicula = input("Ingrese la película en la que se quiere agregar Mark LXXXV: ")
    estado = input("Ingrese el estado del traje: ")
    existe = any(t.modelo == "Mark LXXXV" and t.pelicula == pelicula for t in pila.ver_items())
    if existe:
        print("Mark LXXXV ya existe en esa película. No se agregó.")
    else:
        nuevo_traje = Traje("Mark LXXXV", pelicula, estado)
        pila.apilar(nuevo_traje)
        print("Mark LXXXV agregado.")


# F. Mostrar trajes en Spider-Man: Homecoming y Civil War
def mostrar_trajes_peliculas_especificas(pila):
    peliculas_objetivo = ["Spider-Man: Homecoming", "Capitan America: Civil War"]
    print(" Trajes usados en Spider-Man: Homecoming y Capitán América: Civil War:")
    for t in pila.ver_items():
        if t.pelicula in peliculas_objetivo:
            print("-", t)


def menu():
    pila = Pila()

    while True:
        print("Menú:")
        print("1. Cargar trajes")
        print("2. Buscar Mark XLIV")
        print("3. Mostrar modelos dañados")
        print("4. Eliminar modelos destruidos")
        print("5. Agregar Mark LXXXV")
        print("6. Mostrar trajes de Homecoming y Civil War")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            cargar_trajes(pila)
        elif opcion == "2":
            buscar_mark_xliv(pila)
        elif opcion == "3":
            mostrar_dañados(pila)
        elif opcion == "4":
            eliminar_destruidos(pila)
        elif opcion == "5":
            agregar_mark_lxxxv(pila)
        elif opcion == "6":
            mostrar_trajes_peliculas_especificas(pila)
        elif opcion == "0":
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":  #esto ejecuta el código solo si este archivo es el principal
    menu()
