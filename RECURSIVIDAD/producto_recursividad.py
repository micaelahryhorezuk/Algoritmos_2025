#Implementar una función para calcular el producto de dos números enteros dados.

def producto(num1, num2):
     if num2 == 0 :
          return 1
     elif num2 > 0:
         return num1 * producto(num1, num2-1)
print(producto(2,3))
