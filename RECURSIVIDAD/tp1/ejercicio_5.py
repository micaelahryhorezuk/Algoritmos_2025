#Desarrollar una función que permita convertir un número romano en un número decimal.Con recursividad.
#Lee el número romano de derecha a izquierda: 
# Esto es importante porque en los números romanos, a veces una letra resta en lugar de sumar
#Busqueda secuenncial

decimal = input("Ingrese un número romano: ")
# Definición de la función romano_decimal
# La función romano_decimal toma un número romano como entrada y devuelve su valor decimal.
def romano_decimal(romano):
    valores = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    if not romano :   # Si la cadena está vacía, devuelve 0
        return 0
    if len(romano) == 1: # Si la cadena tiene un solo carácter, devuelve su valor decimal
        return valores[romano]
    else:
        if valores[romano[-1]] > valores[romano[-2]]: # Si el valor del último carácter es mayor que el penúltimo
            return valores[romano[-1]] - romano_decimal(romano[:-1]) # Resta el valor del último carácter y llama a la función recursivamente con el resto de la cadena
        else:
            return valores[romano[-1]] + romano_decimal(romano[:-1]) # Suma el valor del último carácter y llama a la función recursivamente con el resto de la cadena
print("El número decimal es:", romano_decimal(decimal))