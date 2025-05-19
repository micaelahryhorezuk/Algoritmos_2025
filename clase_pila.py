


#Esta clase representa un nodo de la pila. Cada nodo tiene:
 #info: la información que guarda el nodo.
 #sig: una referencia al siguiente nodo en la pila (como una lista enlazada).
 #Ambas están inicializadas como None.
class nodoPila(object):                  
    """Clase nodo pila."""
    info, sig = None, None


#Esta clase representa la pila como tal y tiene dos atributos:
#self.cima: apunta al nodo que está en la cima de la pila (es decir, el último que se insertó).
#self.tamanio: lleva la cuenta del número de elementos en la pila.
#El método __init__ es el constructor, y al crear una nueva pila, la inicializa como vacía:
#cima = None: no hay nodos.
#tamanio = 0: tamaño cero.

class Pila(object):
    """Clase Pila."""

    def __init__(self):
        """Crea una pila vacía."""
        self.cima = None
        self.tamanio = 0
