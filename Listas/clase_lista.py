from typing import Any, Optional # esto es para que no de error en el IDE, no es necesario en la terminal

class List(list):

    CRITERION_FUNCTIONS = {}

    def add_criterion(   ## Método para agregar una función de criterio
        self,
        key_criterion: str,
        function,
    ):
        self.CRITERION_FUNCTIONS[key_criterion] = function

    def show( # Método para mostrar los elementos de la lista
        self
    ) -> None:
        for element in self:
            print(element)

    def delete_value( # Método para eliminar un valor de la lista
        self,
        value,
        key_value: str = None,
    ) -> Optional[Any]:
        index = self.search(value, key_value)
        return self.pop(index) if index is not None else index

    # def insert_value(
    #     self,
    #     value: Any,
    # ) -> None:
    #     # list_number.append(2)
    #     # list_number.insert(1, 11)
    #     pass

    def sort_by_criterion( # Método para ordenar la lista según un criterio 
        self,
        criterion_key: str = None,
    ) -> None:
        criterion = self.CRITERION_FUNCTIONS.get(criterion_key)

        if criterion is not None:
            self.sort(key=criterion)
        elif self and  isinstance(self[0], (int, str, bool)):
            self.sort()
        else:
            print('criterio de orden no encontrado')

    def search( # Método para buscar un valor en la lista utilizando búsqueda binaria
        self,
        search_value,
        search_key: str = None,
    ) -> int:
        self.sort_by_criterion(search_key)
        start = 0
        end = len(self) -1
        middle = (start + end) // 2

        while start <= end:
            criterion = self.CRITERION_FUNCTIONS.get(search_key)
            if criterion is None and self and not isinstance(self[0], (int, str, bool)):
                return None

            value = criterion(self[middle]) if criterion else self[middle]
            if value == search_value:
                return middle
            elif value  < search_value:
                start = middle +1
            else:
                end = middle -1
            middle = (start + end) // 2
    
    def count_nodes(self) -> int: # Método para contar la cantidad de nodos en la lista
        count = 0
        for _ in self:
            count += 1
        return count
