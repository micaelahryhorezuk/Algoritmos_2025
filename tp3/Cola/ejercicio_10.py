# Dada una cola con las notificaciones de las aplicaciones de redes sociales de un Smartphone,
# de las cual se cuenta con la hora de la notificación, la aplicación que la emitió y el mensaje,
# resolver las siguientes actividades:

# a. escribir una función que elimine de la cola todas las notificaciones de Facebook;

# b. escribir una función que muestre todas las notificaciones de Twitter, cuyo mensaje incluya

# la palabra ‘Python’, si perder datos en la cola;

# c. utilizar una pila para almacenar temporáneamente las notificaciones producidas entre las 11:43 y las 15:57, y determinar cuántas son.



class Notificacion:
    def __init__(self, hora, aplicacion, mensaje):
        self.hora = hora
        self.aplicacion = aplicacion
        self.mensaje = mensaje

    def __str__(self):
        return f"[{self.hora}] {self.aplicacion}: {self.mensaje}"


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


class Pila:
    def __init__(self):
        self.items = []

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()

    def esta_vacia(self):
        return len(self.items) == 0

    def tamano(self):
        return len(self.items)



# Punto (a): Eliminar notificaciones de Facebook


# Se usa una cola auxiliar para guardar las que NO son de Facebook.
# Luego se devuelve todo a la cola original.
def eliminar_facebook(cola_original):
    cola_aux = Cola()
    while not cola_original.esta_vacia():
        noti = cola_original.desencolar()
        if noti.aplicacion != "Facebook":
            cola_aux.encolar(noti)
    while not cola_aux.esta_vacia():
        cola_original.encolar(cola_aux.desencolar())

# Punto (b): Mostrar notificaciones de Twitter con "Python"

# Se recorre la cola y se muestra sólo si es de Twitter y contiene "Python".
# Se usa una cola auxiliar para no perder los datos.
def mostrar_twitter_con_python(cola_original):
    cola_aux = Cola()
    print("Notificaciones de Twitter que mencionan 'Python':")
    while not cola_original.esta_vacia():
        noti = cola_original.desencolar()
        if noti.aplicacion == "Twitter" and "Python" in noti.mensaje:
            print(noti)
        cola_aux.encolar(noti)
    while not cola_aux.esta_vacia():
        cola_original.encolar(cola_aux.desencolar())

# Punto (c): Usar pila para almacenar notificaciones entre dos horas

# Se apilan las notificaciones que están entre el rango horario dado.
# Se cuenta cuántas hay. Se preserva la cola original.
def notificaciones_entre_horas(cola_original, hora_inicio, hora_fin):
    pila = Pila()
    cola_aux = Cola()

    while not cola_original.esta_vacia():
        noti = cola_original.desencolar()
        if hora_inicio <= noti.hora <= hora_fin:
            pila.apilar(noti)
        cola_aux.encolar(noti)

    while not cola_aux.esta_vacia():
        cola_original.encolar(cola_aux.desencolar())

    print(f"\nCantidad de notificaciones entre {hora_inicio} y {hora_fin}: {pila.tamano()}")
    return pila

cola = Cola()
cola.encolar(Notificacion("11:00", "Facebook", "Tienes un nuevo recuerdo"))
cola.encolar(Notificacion("11:45", "Twitter", "Python es genial"))
cola.encolar(Notificacion("12:30", "Instagram", "Tienes un nuevo seguidor"))
cola.encolar(Notificacion("14:15", "Facebook", "Nueva historia de tu amigo"))
cola.encolar(Notificacion("15:00", "Twitter", "¿Sabías esto de Python?"))
cola.encolar(Notificacion("16:00", "WhatsApp", "Nuevo mensaje de grupo"))


# Punto (a)
print("Antes de eliminar notificaciones de Facebook:")
for noti in cola.items:
    print(noti)

eliminar_facebook(cola)

print("\nDespués de eliminar notificaciones de Facebook:")
for noti in cola.items:
    print(noti)

# Punto (b)
print()
mostrar_twitter_con_python(cola)

# Punto (c)
pila_resultado = notificaciones_entre_horas(cola, "11:43", "15:57")

print("Notificaciones almacenadas en la pila:")
while not pila_resultado.esta_vacia():
    print(pila_resultado.desapilar())
