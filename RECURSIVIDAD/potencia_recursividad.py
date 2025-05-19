#Implementar una función para calcular la potencia dado dos números enteros, el primero representa la base y segundo el exponente.

def potencia(num1, num2):
     if num2 == 0 :
          return 1
     elif num2== 1 :
          return num1
     else : 
         return num1 * potencia (num1, num2-1)


print (potencia(2, 5))