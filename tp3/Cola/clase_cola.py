from typing import Any, Optional # esto es para que no de error en el IDE, no es necesario en la terminal

class Queue:

    def __init__(self):# constructor de la clase Queue
        self.__elements = []

    def arrive(self, value: Any) -> None: # método para agregar un elemento a la cola
        self.__elements.append(value)

    def attention(self) -> Optional[Any]: # método para eliminar el primer elemento de la cola y devolverlo
        return (
            self.__elements.pop(0)
            if self.__elements
            else None
        )

    def size(self) -> int:     # método para obtener el tamaño de la cola
        return len(self.__elements)      
    
    def on_front(self) -> Optional[Any]: # método para obtener el primer elemento de la cola sin eliminarlo
        return (
            self.__elements[0]
            if self.__elements
            else None
        )

    def move_to_end(self) -> Optional[Any]: # método para mover el primer elemento al final de la cola y devolverlo
        if self.__elements:
            value = self.attention()
            self.arrive(value)
            return value
    
    def show(self): # método para mostrar los elementos de la cola
        for i in range(len(self.__elements)):
            print(self.move_to_end())
