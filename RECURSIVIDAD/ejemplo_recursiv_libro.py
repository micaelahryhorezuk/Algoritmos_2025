#el algoritmo recursivo e iterativo para resolver un mismo problema, obtener el valor en la sucesión de Fibonacci 
# de un número n dado.

n= int(input("Ingrese un número entero positivo: "))        

def fibonacciR(n):
	# Calculo fibonacci recursivo                      #¿Qué número ocupa la posición 5 en la sucesión de Fibonacci?
                                                        # La sucesión de Fibonacci comienza así:
                                                        #Posición:   0  1  2  3  4  5  6  7 ...
                                                        #Valor:      0  1  1  2  3  5  8  13 ...
	if (n == 0 or n == 1):
		return n 
	else: return fibonacciR(n-1) + fibonacciR(n-2)
# Fin del algoritmo recursivo                         

def fibonacciI(n):
 	# Calculo fibonacci iterativo , Iterativo: Usa un bucle para sumar paso a paso hasta llegar al 5º número.

    n0 = 0
    n1 = 1
    fib = 0
    if (n == 0 or n==1):
     fib=n
    else:
        i = 2
        while i <= n:
            fib = n0 + n1
            n0 = n1
            n1 = fib
            i += 1
    return fib
# Fin del algoritmo iterativo
print('El resultado recursivo es: ', fibonacciR(n))
print('El resultado iterativo es: ', fibonacciI(n))