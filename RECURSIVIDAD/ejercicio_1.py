#Dadas las longitudes de los dos catetos de un triángulo rectángulo, hallar la longitud de la hipotenusa.#

import math

cateto1= float(input("Ingrese la longitud del primer cateto: "))
cateto2= float(input("Ingrese la longitud ddel segundo cateto: "))

hipotenusa= math.sqrt(cateto1**2 + cateto2**2)

print("La longitud de la hipoteusa es: ", hipotenusa)