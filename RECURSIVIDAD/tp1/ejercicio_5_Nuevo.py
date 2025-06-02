def bus_bin_rec(array, value, first, last): #Busqueda binaria recursiva
    if first > last:
        return -1
    middle = (first + last) // 2
    if array[middle][0] == value:
        return array[middle][1]
    elif array[middle][0] > value:
        return bus_bin_rec(array, value, first, middle - 1)
    else:
        return bus_bin_rec(array, value, middle + 1, last)


valores_romanos = [('C', 100), ('D', 500), ('I', 1), ('L', 50), ('M', 1000), ('V', 5), ('X', 10)] #lista de tuplas 
valores_romanos.sort()  # .sort ordena la lista por el primer elemento de cada tupla


def romano_decimal(romano): #Esto es la funcion recursiva que convierte un número romano a decimal
    if not romano:
        return 0
    if len(romano) == 1:
        return bus_bin_rec(valores_romanos, romano, 0, len(valores_romanos)-1)
    else:
        ult = bus_bin_rec(valores_romanos, romano[-1], 0, len(valores_romanos)-1)
        penult = bus_bin_rec(valores_romanos, romano[-2], 0, len(valores_romanos)-1)
        if ult > penult:
            return ult - romano_decimal(romano[:-1])
        else:
            return ult + romano_decimal(romano[:-1])


entrada = input("Ingrese un número romano: ")
print("El número decimal es:", romano_decimal(entrada))
