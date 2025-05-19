#El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u
#otro, el que más le guste) está atrapado, pero muy cerca está su mochila que contiene muchos objetos. 
# Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi “con ayuda de la fuerza” realizar las siguientes actividades:

#a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no
#queden más objetos en la mochila;

#b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sacar para encontrarlo;

#c. Utilizar un vector para representar la mochila.



# #Recorre la mochila de a un objeto por vez, usando recursividad.

# Informa si encontró el sable de luz o no, y cuántos objetos tuvo que sacar.

def usar_la_fuerza(mochila, objetos_sacados=0):
    
    if not mochila:
        return False, objetos_sacados    #si la mochila está vacía, no hay sable de luz

    # si la mochila no está vacía, sacamos el primer objeto
    objeto = mochila.pop(0)  # Sacamos el primer objeto de la mochila
    objetos_sacados += 1     #contador de objetos sacados

    
    if objeto == "sable de luz":
        return True, objetos_sacados  #si encontramos el sable de luz, devolvemos True y el número de objetos sacados
    else:
        # Llamada recursiva con el resto de la mochila
        return usar_la_fuerza(mochila, objetos_sacados)

mochila = ['botella', 'comida', 'mapa', 'sable de luz', 'ropa'] #vector que representa la mochila
encontrado, objetos_sacados = usar_la_fuerza(mochila)

if encontrado:
    print("Encontraste el sable de luz después de sacar objetos", objetos_sacados )
else:
    print("No había ningún sable de luz en la mochila.")




